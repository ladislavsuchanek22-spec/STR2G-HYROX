// /api/athletes/photo – the logged-in member's own profile photo.
// The browser crops and resizes it before upload; here we only accept real image bytes up to 1.5 MB.
import { getSessionEmail, findMembership, json } from "../lib/athletes.mjs";
import { profileStore, memberKey, imageType } from "../lib/profiles.mjs";

const MAX_BYTES = 1.5 * 1024 * 1024;

export default async (req, context) => {
  const email = await getSessionEmail(context).catch(() => null);
  if (!email) return json({ error: "not_logged_in" }, 401);

  const store = profileStore(context);
  const key = `${await memberKey(email)}/photo`;

  if (req.method === "GET") {
    const entry = await store.getWithMetadata(key, { type: "arrayBuffer" });
    if (!entry) return new Response("Not found", { status: 404, headers: { "cache-control": "no-store" } });
    return new Response(entry.data, {
      headers: {
        "content-type": entry.metadata?.contentType || "image/jpeg",
        "cache-control": "private, no-cache",
        "x-content-type-options": "nosniff",
      },
    });
  }

  if (req.method === "DELETE") {
    await store.delete(key);
    return json({ ok: true });
  }

  // PUT
  const membership = await findMembership(email).catch(() => null);
  if (!membership) return json({ error: "no_membership" }, 403);

  const declared = Number(req.headers.get("content-length") || 0);
  if (declared > MAX_BYTES) return json({ error: "too_large" }, 413);
  const bytes = new Uint8Array(await req.arrayBuffer());
  if (bytes.length === 0) return json({ error: "empty" }, 400);
  if (bytes.length > MAX_BYTES) return json({ error: "too_large" }, 413);
  const type = imageType(bytes);
  if (!type) return json({ error: "not_an_image" }, 415);

  const updatedAt = new Date().toISOString();
  await store.set(key, bytes.buffer, { metadata: { contentType: type, updatedAt } });
  return json({ ok: true, photoVersion: updatedAt });
};

export const config = {
  path: "/api/athletes/photo",
  method: ["GET", "PUT", "DELETE"],
  rateLimit: { action: "rate_limit", aggregateBy: ["ip", "domain"], windowSize: 60, windowLimit: 30 },
};
