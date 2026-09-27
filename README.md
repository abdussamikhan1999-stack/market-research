# market-research

Ad-hoc market/asset research pulled from live sources on 2026-09-27. Each
note pulls from primary or near-primary sources where possible (SEC data,
exchange sites, block explorers) rather than relying on forum claims.

- [`precious-metals.md`](precious-metals.md) — gold/silver spot prices, gold-silver ratio, 10-year context
- [`gme.md`](gme.md) — GME short interest, days to cover, borrow rate, and raw SEC failure-to-deliver data
- [`crypto.md`](crypto.md) — BTC, XRP, and Monero price/network data
- [`stock-market-overview.md`](stock-market-overview.md) — snapshot of index futures and market sentiment
- [`trading-journals.md`](trading-journals.md) — forum trade calls checked against actual historical price data
- [`forum-notes.md`](forum-notes.md) — forum conventions/rules that affect how much to trust a claimed trade call
- [`data/gme_ftd_august_2026.csv`](data/gme_ftd_august_2026.csv) — raw GME fails-to-deliver data, parsed from SEC.gov's `cnsfails` files for August 2026

## Caveats

- Prices/figures are a point-in-time snapshot (weekend of 2026-09-27, US
  markets closed) and will be stale quickly.
- Several sites blocked automated fetches (403s) or only render data via
  JS, so some figures come from search-result snippets rather than a
  direct pull — noted inline where that's the case.
- Where a note references a claim from a forum/community (e.g. GME
  short-squeeze thesis, XRP "lore"), it's explicitly marked as
  unverified narrative, not fact.
