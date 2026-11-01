// GET /api/athletes/count – live number of active STR2G Athletes memberships for the Founding counter.
import { countMembers, FOUNDING_CAP } from "../lib/athletes.mjs";

export default async () => {
  try {
    const members = await countMembers();
    const taken = Math.min(members, FOUNDING_CAP);
    return new Response(JSON.stringify({ members, cap: FOUNDING_CAP, spotsLeft: FOUNDING_CAP - taken }), {
      headers: {
        "content-type": "application/json; charset=utf-8",
        "cache-control": "public, max-age=0, must-revalidate",
        // Cache on Netlify's CDN for 60 s so Stripe is not called on every page view.
        "netlify-cdn-cache-control": "public, durable, max-age=60, stale-while-revalidate=300",
      },
    });
  } catch (err) {
    console.error(err);
    return new Response(JSON.stringify({ error: "unavailable" }), {
      status: 503,
      headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" },
    });
  }
};

export const config = { path: "/api/athletes/count", method: "GET" };
