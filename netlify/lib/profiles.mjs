// STR2G Athletes – member profiles and photos, stored privately in Netlify Blobs.
// Every read and write goes through a function that checks the member's session; nothing is public.
import { getStore } from "@netlify/blobs";

// EU region: members' personal data (incl. body weight) stays in the EU.
const REGION = "eu-central-1";

// Deploy previews and branch deploys get their own store, so testing never touches real members' data.
export function profileStore(context) {
  const live = context?.deploy?.context === "production";
  return getStore({ name: live ? "athletes-profiles" : "athletes-profiles-preview", region: REGION, consistency: "strong" });
}

// Storage key derived from the email with a secret, so keys reveal nothing about who the member is.
export async function memberKey(email) {
  const secret = Netlify.env.get("ATHLETES_SESSION_SECRET");
  const key = await crypto.subtle.importKey("raw", new TextEncoder().encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const sig = new Uint8Array(await crypto.subtle.sign("HMAC", key, new TextEncoder().encode("profile:" + email)));
  return Array.from(sig.slice(0, 16), (b) => b.toString(16).padStart(2, "0")).join("");
}

export const CLUBS = ["", "prague", "brno", "ostrava", "other"];
export const DIVISIONS = ["", "open", "pro", "doubles", "relay"];

const str = (v, max) => {
  if (v === undefined || v === null) return "";
  const s = String(v).replace(/[\u0000-\u001f\u007f]/g, " ").trim();
  if (s.length > max) throw new Error(`too_long:${max}`);
  return s;
};

const kg = (v, field) => {
  if (v === undefined || v === null || v === "") return null;
  const n = Number(String(v).replace(",", "."));
  if (!Number.isFinite(n) || n < 30 || n > 250) throw new Error(`invalid:${field}`);
  return Math.round(n * 10) / 10;
};

const raceTime = (v, field) => {
  const s = str(v, 8);
  if (!s) return "";
  if (!/^\d{1,2}:[0-5]\d:[0-5]\d$/.test(s)) throw new Error(`invalid:${field}`);
  return s;
};

const date = (v) => {
  const s = str(v, 10);
  if (!s) return "";
  if (!/^\d{4}-\d{2}-\d{2}$/.test(s) || Number.isNaN(Date.parse(s))) throw new Error("invalid:nextRaceDate");
  return s;
};

// https link, optionally limited to one site (and its subdomains)
const link = (v, field, host) => {
  const s = str(v, 300);
  if (!s) return "";
  let u;
  try {
    u = new URL(s);
  } catch {
    throw new Error(`invalid:${field}`);
  }
  if (u.protocol !== "https:") throw new Error(`invalid:${field}`);
  if (host && !(u.hostname === host || u.hostname.endsWith("." + host))) throw new Error(`invalid:${field}`);
  return u.href;
};

const pick = (v, list, field) => {
  const s = str(v, 20);
  if (!list.includes(s)) throw new Error(`invalid:${field}`);
  return s;
};

// Validates and cleans what the member sent. Throws "invalid:<field>" or "too_long:<n>".
export function cleanProfile(input) {
  const i = input && typeof input === "object" ? input : {};
  const handle = str(i.instagram, 31).replace(/^@/, "");
  if (handle && !/^[A-Za-z0-9._]{1,30}$/.test(handle)) throw new Error("invalid:instagram");
  return {
    displayName: str(i.displayName, 60),
    city: str(i.city, 60),
    club: pick(i.club ?? "", CLUBS, "club"),
    division: pick(i.division ?? "", DIVISIONS, "division"),
    bio: str(i.bio, 300),
    instagram: handle,
    weightKg: kg(i.weightKg, "weightKg"),
    goalWeightKg: kg(i.goalWeightKg, "goalWeightKg"),
    pbTime: raceTime(i.pbTime, "pbTime"),
    goalTime: raceTime(i.goalTime, "goalTime"),
    nextRace: str(i.nextRace, 80),
    nextRaceDate: date(i.nextRaceDate),
    goal: str(i.goal, 200),
    roxfitUrl: link(i.roxfitUrl, "roxfitUrl", "roxfit.com"),
    resultsUrl: link(i.resultsUrl, "resultsUrl", "hyrox.com"),
    otherUrl: link(i.otherUrl, "otherUrl"),
  };
}

// Recognises real image bytes, whatever the browser claims.
export function imageType(bytes) {
  if (bytes.length > 3 && bytes[0] === 0xff && bytes[1] === 0xd8 && bytes[2] === 0xff) return "image/jpeg";
  if (bytes.length > 8 && bytes[0] === 0x89 && bytes[1] === 0x50 && bytes[2] === 0x4e && bytes[3] === 0x47) return "image/png";
  if (bytes.length > 12 && String.fromCharCode(...bytes.slice(0, 4)) === "RIFF" && String.fromCharCode(...bytes.slice(8, 12)) === "WEBP") return "image/webp";
  return null;
}
