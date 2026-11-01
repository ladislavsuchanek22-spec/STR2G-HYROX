// GET /api/athletes/me – who is logged in, which plan they have right now, and the members content.
// Discount codes are only ever sent to annual members.
import { getSessionEmail, findMembership, json } from "../lib/athletes.mjs";
import { CONTENT } from "../lib/athletes-content.mjs";

export default async (req, context) => {
  const email = await getSessionEmail(context).catch(() => null);
  if (!email) return json({ loggedIn: false }, 401);

  let membership;
  try {
    membership = await findMembership(email);
  } catch (err) {
    console.error("me:", err.message);
    return json({ error: "unavailable" }, 503);
  }

  if (!membership) return json({ loggedIn: true, email, plan: null });

  const annual = membership.plan === "annual";
  return json({
    loggedIn: true,
    email,
    name: membership.name,
    plan: membership.plan,
    renews: membership.renews ? new Date(membership.renews * 1000).toISOString() : null,
    cancelAtPeriodEnd: membership.cancelAtPeriodEnd,
    codes: annual
      ? {
          training: Netlify.env.get("ATHLETES_TRAINING_CODE") || "STR2G-ANNUAL15",
          programs: Netlify.env.get("ATHLETES_STRIVEE_CODE") || null,
        }
      : null,
    content: CONTENT,
  });
};

export const config = { path: "/api/athletes/me", method: "GET" };
