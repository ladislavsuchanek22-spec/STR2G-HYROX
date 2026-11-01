// POST /api/athletes/login – sends a one-time login link to a member's email.
// Always answers the same way, so nobody can find out who is a member by trying emails.
import { findMembership, linkToken, normalizeEmail, sendLoginEmail, siteUrl, json } from "../lib/athletes.mjs";

export default async (req, context) => {
  let email = null;
  try {
    const ct = req.headers.get("content-type") || "";
    const data = ct.includes("application/json") ? await req.json() : Object.fromEntries(await req.formData());
    email = normalizeEmail(data.email);
  } catch {
    email = null;
  }
  if (!email) return json({ ok: false, error: "invalid_email" }, 400);

  const started = Date.now();
  let debug = "";
  try {
    const membership = await findMembership(email);
    if (membership) {
      const token = await linkToken(email);
      const link = `${siteUrl(req)}/api/athletes/verify?t=${encodeURIComponent(token)}`;
      await sendLoginEmail(email, link);
      console.log("login: link sent");
      debug = "sent";
    } else {
      console.log("login: no active membership for this email");
      debug = "no_membership";
    }
  } catch (err) {
    console.error("login failed:", err.message);
    debug = "error: " + err.message;
  }

  // Same answer and roughly the same timing for members and non-members,
  // so nobody can find out who is a member by trying emails.
  const wait = 1500 - (Date.now() - started);
  if (wait > 0) await new Promise((r) => setTimeout(r, wait));
  // Deploy previews show the outcome to help testing; production never does.
  const preview = context?.deploy?.context && context.deploy.context !== "production";
  return json(preview ? { ok: true, debug } : { ok: true });
};

export const config = {
  path: "/api/athletes/login",
  method: "POST",
  rateLimit: { action: "rate_limit", aggregateBy: ["ip", "domain"], windowSize: 60, windowLimit: 5 },
};
