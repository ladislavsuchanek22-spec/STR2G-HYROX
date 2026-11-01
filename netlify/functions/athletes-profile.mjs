// /api/athletes/profile – the logged-in member's own profile.
// GET reads it, PUT saves it, DELETE removes the profile and photo for good.
import { getSessionEmail, findMembership, json } from "../lib/athletes.mjs";
import { profileStore, memberKey, cleanProfile } from "../lib/profiles.mjs";

export default async (req, context) => {
  const email = await getSessionEmail(context).catch(() => null);
  if (!email) return json({ error: "not_logged_in" }, 401);

  const store = profileStore(context);
  const key = await memberKey(email);

  if (req.method === "DELETE") {
    await store.delete(`${key}/profile`);
    await store.delete(`${key}/photo`);
    return json({ ok: true });
  }

  let membership;
  try {
    membership = await findMembership(email);
  } catch (err) {
    console.error("profile:", err.message);
    return json({ error: "unavailable" }, 503);
  }
  if (!membership) return json({ error: "no_membership" }, 403);

  if (req.method === "GET") {
    const entry = await store.getWithMetadata(`${key}/profile`, { type: "json" });
    const photo = await store.getMetadata(`${key}/photo`);
    return json({
      profile: entry?.data || null,
      hasPhoto: Boolean(photo),
      photoVersion: photo?.metadata?.updatedAt || null,
    });
  }

  // PUT
  let profile;
  try {
    const body = await req.json();
    profile = cleanProfile(body);
  } catch (err) {
    const reason = String(err.message || "");
    return json({ error: reason.startsWith("invalid:") || reason.startsWith("too_long:") ? reason : "invalid_body" }, 400);
  }
  profile.updatedAt = new Date().toISOString();
  await store.setJSON(`${key}/profile`, profile);
  return json({ ok: true, profile });
};

export const config = {
  path: "/api/athletes/profile",
  method: ["GET", "PUT", "DELETE"],
  rateLimit: { action: "rate_limit", aggregateBy: ["ip", "domain"], windowSize: 60, windowLimit: 30 },
};
