// Shared helpers for STR2G Athletes membership functions.
// Stripe is called over its REST API with fetch, so the site needs no npm build step.

export const FOUNDING_CAP = 100;

// Membership prices in Stripe (not secret). Can be overridden in Netlify env vars.
export const PRICE_MONTHLY = () => Netlify.env.get("ATHLETES_PRICE_MONTHLY") || "price_1UWucEQfZhqdUYaiKHtFbVse";
export const PRICE_ANNUAL = () => Netlify.env.get("ATHLETES_PRICE_ANNUAL") || "price_1UWucIQfZhqdUYaiM1bGoITd";

const SESSION_COOKIE = "str2g_athlete";
const SESSION_DAYS = 30;
const LINK_MINUTES = 20;

// ---------- Stripe ----------

function stripeKey() {
  const key = Netlify.env.get("STRIPE_SECRET_KEY");
  if (!key) throw new Error("STRIPE_SECRET_KEY is not set");
  return key;
}

export async function stripeGet(path, params = {}) {
  const url = new URL("https://api.stripe.com/v1/" + path);
  for (const [k, v] of Object.entries(params)) {
    if (Array.isArray(v)) v.forEach((x) => url.searchParams.append(k, x));
    else if (v !== undefined && v !== null) url.searchParams.set(k, String(v));
  }
  const res = await fetch(url, { headers: { Authorization: `Bearer ${stripeKey()}` } });
  const body = await res.json();
  if (!res.ok) throw new Error(`Stripe ${path}: ${body?.error?.message || res.status}`);
  return body;
}

export async function stripePost(path, form) {
  const res = await fetch("https://api.stripe.com/v1/" + path, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${stripeKey()}`,
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams(form),
  });
  const body = await res.json();
  if (!res.ok) throw new Error(`Stripe ${path}: ${body?.error?.message || res.status}`);
  return body;
}

// All subscriptions on one price that give access right now.
async function listLiveSubscriptions(price) {
  const out = [];
  for (const status of ["active", "trialing", "past_due"]) {
    let starting_after;
    do {
      const page = await stripeGet("subscriptions", { price, status, limit: 100, starting_after });
      out.push(...page.data);
      starting_after = page.has_more ? page.data[page.data.length - 1].id : undefined;
    } while (starting_after);
  }
  return out;
}

// Number of distinct members with a live membership.
export async function countMembers() {
  const subs = [
    ...(await listLiveSubscriptions(PRICE_MONTHLY())),
    ...(await listLiveSubscriptions(PRICE_ANNUAL())),
  ];
  return new Set(subs.map((s) => s.customer)).size;
}

const LIVE = new Set(["active", "trialing", "past_due"]);

// Finds the best live membership for an email. Annual beats monthly.
export async function findMembership(email) {
  const customers = await stripeGet("customers", { email, limit: 10 });
  let best = null;
  for (const c of customers.data) {
    const subs = await stripeGet("subscriptions", { customer: c.id, status: "all", limit: 20 });
    for (const s of subs.data) {
      if (!LIVE.has(s.status)) continue;
      for (const item of s.items.data) {
        const priceId = item.price.id;
        const plan = priceId === PRICE_ANNUAL() ? "annual" : priceId === PRICE_MONTHLY() ? "monthly" : null;
        if (!plan) continue;
        const candidate = {
          plan,
          customerId: c.id,
          name: c.name || null,
          renews: item.current_period_end || s.current_period_end || null,
          cancelAtPeriodEnd: Boolean(s.cancel_at_period_end),
        };
        if (!best || (best.plan === "monthly" && plan === "annual")) best = candidate;
      }
    }
  }
  return best;
}

// ---------- signed tokens (magic link + session cookie) ----------

const enc = new TextEncoder();

function b64url(bytes) {
  let s = "";
  for (const b of new Uint8Array(bytes)) s += String.fromCharCode(b);
  return btoa(s).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

function b64urlToString(str) {
  const pad = str.length % 4 ? "=".repeat(4 - (str.length % 4)) : "";
  return atob(str.replace(/-/g, "+").replace(/_/g, "/") + pad);
}

async function hmac(data) {
  const secret = Netlify.env.get("ATHLETES_SESSION_SECRET");
  if (!secret || secret.length < 32) throw new Error("ATHLETES_SESSION_SECRET is missing or too short");
  const key = await crypto.subtle.importKey("raw", enc.encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  return b64url(await crypto.subtle.sign("HMAC", key, enc.encode(data)));
}

function safeEqual(a, b) {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

export async function sign(payload) {
  const body = b64url(enc.encode(JSON.stringify(payload)));
  return `${body}.${await hmac(body)}`;
}

export async function verify(token, purpose) {
  if (!token || typeof token !== "string" || !token.includes(".")) return null;
  const [body, sig] = token.split(".");
  if (!safeEqual(sig, await hmac(body))) return null;
  let payload;
  try {
    payload = JSON.parse(b64urlToString(body));
  } catch {
    return null;
  }
  if (payload.p !== purpose) return null;
  if (!payload.exp || Date.now() > payload.exp) return null;
  return payload;
}

export function linkToken(email) {
  return sign({ p: "link", e: email, exp: Date.now() + LINK_MINUTES * 60_000 });
}

export async function setSession(context, email) {
  const token = await sign({ p: "session", e: email, exp: Date.now() + SESSION_DAYS * 86_400_000 });
  context.cookies.set({
    name: SESSION_COOKIE,
    value: token,
    path: "/",
    httpOnly: true,
    secure: true,
    sameSite: "Lax",
    expires: new Date(Date.now() + SESSION_DAYS * 86_400_000),
  });
}

export async function getSessionEmail(context) {
  const payload = await verify(context.cookies.get(SESSION_COOKIE), "session");
  return payload ? payload.e : null;
}

export function clearSession(context) {
  context.cookies.delete({ name: SESSION_COOKIE, path: "/" });
}

// ---------- misc ----------

export function normalizeEmail(value) {
  const email = String(value || "").trim().toLowerCase();
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) && email.length <= 254 ? email : null;
}

export function siteUrl(req) {
  return Netlify.env.get("ATHLETES_SITE_URL") || new URL(req.url).origin;
}

export function json(data, status = 200, extra = {}) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store", ...extra },
  });
}

export async function sendLoginEmail(to, link) {
  const apiKey = Netlify.env.get("RESEND_API_KEY");
  const from = Netlify.env.get("ATHLETES_MAIL_FROM") || "STR2G Athletes <athletes@str2g.com>";
  if (!apiKey) throw new Error("RESEND_API_KEY is not set");
  const html = `<!doctype html><html><body style="margin:0;background:#050505;color:#F2F0E8;font-family:Arial,Helvetica,sans-serif">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td align="center" style="padding:40px 16px">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:480px">
<tr><td style="font-size:28px;font-weight:900;font-style:italic">STR<span style="color:#C9A950">2</span>G <span style="font-size:12px;letter-spacing:3px;color:#C9A950;font-style:normal">ATHLETES</span></td></tr>
<tr><td style="padding:28px 0 12px;font-size:17px;line-height:1.6">Here is your login link to the STR2G Athletes members area. It works for ${LINK_MINUTES} minutes.</td></tr>
<tr><td style="padding:12px 0 28px"><a href="${link}" style="display:inline-block;background:#C9A950;color:#050505;text-decoration:none;font-weight:bold;padding:14px 28px;text-transform:uppercase">Open members area</a></td></tr>
<tr><td style="font-size:13px;line-height:1.5;color:#9A978F">Didn't ask for this? Ignore this email. Nobody can log in without the link.<br><br>Stronger together. · str2g.com</td></tr>
</table></td></tr></table></body></html>`;
  const res = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${apiKey}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      from,
      to: [to],
      subject: "Your STR2G Athletes login link",
      html,
      text: `Your STR2G Athletes login link (valid ${LINK_MINUTES} minutes):\n${link}\n\nDidn't ask for this? Ignore this email.`,
    }),
  });
  if (!res.ok) throw new Error(`Resend: ${res.status} ${await res.text()}`);
}
