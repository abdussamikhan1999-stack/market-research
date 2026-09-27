# Trading journal case studies

Verifying specific forum trade calls against actual historical price data,
rather than taking claimed setups/results at face value.

## MzansiObi — BTCUSD mean reversion (forex-factory-style forum, Aug 2019)

**The setup**: an experienced trader (5,400+ posts, "Full Time Trader")
started a public BTCUSD journal on 2019-08-12, applying a mean-reversion
approach using Camarilla and Fibonacci pivot levels — new to trading BTC
specifically, not new to trading. Framed explicitly as an open experiment
("will give it the next couple of months to try and see").

**The trade**: buy limit at 11,247.29, stop-loss 11,000, take-profit
12,520 — a ~5:1 reward:risk setup on paper (247 pts risked vs. 1,273 pts
targeted).

**What actually happened** (verified via Binance's public daily BTCUSDT
klines API, not the thread's own claims):

| Date | Open | High | Low | Close |
|---|---|---|---|---|
| 2019-08-12 | 11,539.08 | 11,577.89 | **11,235.32** | 11,396.08 |
| 2019-08-13 | 11,398.35 | 11,456.16 | **10,788.45** | 10,892.71 |

- The buy limit filled same-day (Aug 12 low of 11,235.32 traded through
  the 11,247.29 entry).
- The stop-loss was hit the very next day (Aug 13 low of 10,788.45, well
  through the 11,000 stop) — trade closed for a loss ~1 day after entry,
  never approaching the take-profit.
- Bigger picture: this wasn't just an unlucky stop-out. BTC kept falling
  for the rest of the month, from ~11,400 (Aug 12) down to a low of
  **~9,320 on Aug 29** — an ~18% decline over ~2.5 weeks. The
  mean-reversion buy was positioned against an active downtrend, not a
  temporary dip.

**Takeaway**: a real, transparently-documented trade call from a
legitimate trading journal, checked against actual market data rather
than assumed. It lost, quickly, and for a structural reason (fighting the
trend) rather than bad luck on timing. Worth remembering when reading any
forum trade call, including ones with a track record attached — verify
against real price data before treating the record as evidence of edge.

Source data: Binance public API
(`api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d`).
