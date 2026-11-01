// POST /api/athletes/logout – removes the session cookie.
import { clearSession, siteUrl } from "../lib/athletes.mjs";

export default async (req, context) => {
  clearSession(context);
  return new Response(null, { status: 303, headers: { location: `${siteUrl(req)}/athletes/members/`, "cache-control": "no-store" } });
};

export const config = { path: "/api/athletes/logout", method: "POST" };
