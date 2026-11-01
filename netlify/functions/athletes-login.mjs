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

  const work = (async () => {
    const membership = await findMembership(email);
    if (!membership) return; // not a member: silently do nothing
    const token = await linkToken(email);
    const link = `${siteUrl(req)}/api/athletes/verify?t=${encodeURIComponent(token)}`;
    await sendLoginEmail(email, link);
  })().catch((err) => console.error("login:", err.message));

  // Send the answer straight away; the Stripe lookup and email finish in the background.
  context.waitUntil(work);
  return json({ ok: true });
};

export const config = {
  path: "/api/athletes/login",
  method: "POST",
  rateLimit: { action: "rate_limit", aggregateBy: ["ip", "domain"], windowSize: 60, windowLimit: 5 },
};
