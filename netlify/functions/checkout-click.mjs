// /api/checkout-click – anonymous count of clicks on Strivee checkout links ("klik na koupit").
// No cookies, no IP, no IDs: one tiny record per click (day, program, language, traffic source,
// whether tracking consent was given). Shows how many buy clicks the Meta/Google pixels miss
// because the visitor did not accept cookies.
//   POST (navigator.sendBeacon from i18n/tracking.html) -> stores one record
//   GET  /api/checkout-click?days=30                      -> daily totals (counts only)
import { getStore } from "@netlify/blobs";

// Same EU region as the Athletes stores.
const REGION = "eu-central-1";

// Deploy previews and branch deploys get their own store, so testing never touches real numbers.
function clickStore(context) {
  const live = context?.deploy?.context === "production";
  return getStore({ name: live ? "checkout-clicks" : "checkout-clicks-preview", region: REGION, consistency: "strong" });
}

const clean = (v, n) => String(v || "").toLowerCase().replace(/[^a-z0-9 ._-]/g, "").trim().slice(0, n);
const day = (msAgo = 0) => new Date(Date.now() - msAgo).toISOString().slice(0, 10);

export default async (req, context) => {
  const store = clickStore(context);

  if (req.method === "POST") {
    let d = {};
    try { d = JSON.parse((await req.text()) || "{}"); } catch { /* ignore junk */ }
    const rec = { p: clean(d.p, 60) || "unknown", l: clean(d.l, 5) || "?", src: clean(d.src, 12) || "other", c: d.c ? 1 : 0 };
    await store.setJSON(`${day()}/${crypto.randomUUID()}`, rec);
    return new Response(null, { status: 204, headers: { "cache-control": "no-store" } });
  }

  const url = new URL(req.url);
  const days = Math.min(parseInt(url.searchParams.get("days") || "30", 10) || 30, 120);
  const out = {};
  for (let i = 0; i < days; i++) {
    const d = day(i * 864e5);
    const { blobs } = await store.list({ prefix: `${d}/` });
    if (!blobs.length) continue;
    const t = { total: 0, withConsent: 0, bySource: {}, byProgram: {}, byLang: {} };
    for (const b of blobs) {
      const r = await store.get(b.key, { type: "json" });
      if (!r) continue;
      t.total++;
      t.withConsent += r.c ? 1 : 0;
      t.bySource[r.src] = (t.bySource[r.src] || 0) + 1;
      t.byProgram[r.p] = (t.byProgram[r.p] || 0) + 1;
      t.byLang[r.l] = (t.byLang[r.l] || 0) + 1;
    }
    out[d] = t;
  }
  return Response.json(out, { headers: { "cache-control": "no-store", "x-robots-tag": "noindex" } });
};

export const config = { path: "/api/checkout-click", method: ["GET", "POST"] };
