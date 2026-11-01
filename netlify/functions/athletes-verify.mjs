// GET /api/athletes/verify?t=... – the link from the login email. Sets the session cookie and opens the members area.
import { verify, setSession, siteUrl } from "../lib/athletes.mjs";

export default async (req, context) => {
  const token = new URL(req.url).searchParams.get("t");
  const payload = await verify(token, "link").catch(() => null);
  const base = siteUrl(req);
  if (!payload) {
    return new Response(null, { status: 302, headers: { location: `${base}/athletes/members/?login=expired`, "cache-control": "no-store" } });
  }
  await setSession(context, payload.e);
  return new Response(null, { status: 302, headers: { location: `${base}/athletes/members/`, "cache-control": "no-store" } });
};

export const config = { path: "/api/athletes/verify", method: "GET" };
