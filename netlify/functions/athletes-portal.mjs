// POST /api/athletes/portal – opens the Stripe customer portal (change plan, card, cancel).
import { getSessionEmail, findMembership, stripePost, siteUrl } from "../lib/athletes.mjs";

export default async (req, context) => {
  const base = siteUrl(req);
  const email = await getSessionEmail(context).catch(() => null);
  if (!email) return new Response(null, { status: 303, headers: { location: `${base}/athletes/members/` } });

  try {
    const membership = await findMembership(email);
    if (!membership) return new Response(null, { status: 303, headers: { location: `${base}/athletes/#plans` } });
    const session = await stripePost("billing_portal/sessions", {
      customer: membership.customerId,
      return_url: `${base}/athletes/members/`,
    });
    return new Response(null, { status: 303, headers: { location: session.url, "cache-control": "no-store" } });
  } catch (err) {
    console.error("portal:", err.message);
    // Deploy previews pass the reason along to help testing; production never does.
    const preview = context?.deploy?.context && context.deploy.context !== "production";
    const reason = preview ? `&reason=${encodeURIComponent(err.message.slice(0, 200))}` : "";
    return new Response(null, { status: 303, headers: { location: `${base}/athletes/members/?portal=error${reason}` } });
  }
};

export const config = { path: "/api/athletes/portal", method: "POST" };
