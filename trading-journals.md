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

## GBP/USD directional debate (forexfactory.com, Nov 2006)

**The setup**: heading into the week of Nov 20, 2006, four traders
debated cable's direction from around 1.8850-1.8950. Positions taken:
- OP: bullish, target ~1.9050
- AhmedFouad: neutral/disciplined — flat until either 1.8834/36 (support)
  or 1.8965/67 (resistance) broke with a confirmed close
- Qu|cksilver: breakout rule — go long if the market opens above 1.8950
- ghitz: bearish continuation — expected the bounce to be a pullback
  (38% retrace of the prior down-move) before resuming lower, citing a
  50% retrace/stop area near 1.8917-1.9170

**What actually happened** (verified via ECB daily reference rates,
Frankfurter API — `api.frankfurter.app`):

| Date | GBP/USD |
|---|---|
| Fri 2006-11-17 | 1.8852 |
| Mon 2006-11-20 | 1.8973 |
| Tue 2006-11-21 | 1.8989 |
| Wed 2006-11-22 | 1.9093 |
| Thu 2006-11-23 | 1.9147 |
| Fri 2006-11-24 | 1.9320 |
| Mon 2006-11-27 | 1.9351 |
| Tue 2006-11-28 | 1.9441 |
| Wed 2006-11-29 | 1.9512 |
| Thu 2006-11-30 | 1.9577 |

Cable rallied every day with no pullback, clearing 1.8950 immediately on
Monday and blowing well past the OP's 1.9050 target to **1.9577** by
month-end (~4% move in under two weeks).

**Scoring**: OP (bullish) and Qu|cksilver (breakout-long) were both
vindicated — Qu|cksilver's rule would have triggered Monday and ridden
most of the move. AhmedFouad's discipline (wait for a confirmed close
above 1.8967) cost nothing but also captured none of the move — his own
trigger condition was met almost immediately. ghitz's bearish
retrace-and-continuation call was **wrong**: there was no reversal at
all, just a sustained trend.

Caveat: this is ECB's daily reference fixing rate, not intraday OHLC, so
exact intraday stop hits can't be confirmed — only the day-to-day trend.

## vrbnca — "1,234.8% this month" Gold/USD account (forexfactory.com Trade Explorer, Sep 2026)

**The setup**: a Forex Factory profile with a live broker-verified Trade
Explorer (synced directly from an Exness live account, not
self-reported) showing:
- **This month**: +1,234.8% return, 165-166 entries/exits
- **All time**: +158.6% return, 351 total trades

**The red flag**: almost the entire lifetime return of the account
happened in a single recent month — a near-flat/modest history followed
by an explosive one-month spike is a classic signature of either an
extreme lucky bet or a martingale/grid strategy (scaling position size
after losses to force an eventual win), not a repeatable edge.

**Supporting evidence from the visible trade list**: a run of Gold/USD
sell trades in the same session shows small +0.1% wins mixed with much
larger -3.3% and -3.9% losses, all around the same 4,280-4,295 price
zone — consistent with repeatedly re-entering/averaging a losing short as
price ground higher against the position, then closing pieces for small
wins once price ticked back down. This pattern produces a smooth-looking
equity curve right up until a strong enough adverse move causes an
account blowup, since risk compounds with each re-entry instead of
staying fixed.

**Volume**: ~165 of the account's 351 all-time trades (roughly half)
happened in the single most recent month — a sharp, recent shift to much
higher frequency/risk than however the account started.

**Takeaway**: broker-verified trade history is a real trust signal
(confirms the numbers aren't fabricated), but verified is not the same as
sustainable. Look past the top-line return to position sizing and
win/loss structure before treating any short monthly track record —
especially one this extreme — as evidence of skill.

## IMforex — three linked accounts, one already blown up (forexfactory.com Trade Explorer, 2026)

**The setup**: one trader (IMforex, ThinkMarkets broker) running three
separate live-linked accounts simultaneously, all trading GBP/USD:

| Account | History | All-Time Return | This Year | This Month |
|---|---|---|---|---|
| $50 (original) | 71 months, 4,482 trades | -38.4% | **-97.5%** | — |
| $50 II | started Mar 2026, 484 trades | -51.4% | +11.3% | **+118.7%** |
| $1000 | started Jun 2026, 393 trades | -17.2% | -18.9% | **+317.6%** |

**The key finding**: the account with by far the longest real history
(71 months, 4,482 trades) is sitting at a balance of **$1** after a
-97.5% year, on top of an all-time return that was already negative
(-38.4%) before this year's collapse. Meanwhile the two newer accounts
are having spectacular months. Anyone looking only at the newer accounts'
headline "This Month" figures would see a trader on a hot streak; the
original account shows what this trading style eventually does given
enough time.

**Evidence it's one strategy, not three**: the $50 II and $1000 accounts'
"Latest Closed Trades" show identical entries/exits — same GBP/USD
prices, same days (e.g. both bought 1.3213 → 1.3237 "44 hr ago") — just
scaled lot sizes (0.04 vs 0.35, ~8.75x). This is one EA/signal run in
parallel across differently-sized accounts, not independent strategies,
so the two "hot month" data points are really one data point counted
twice.

**Trade style**: very high frequency (4,482 trades / 71 months ≈
63/month on the oldest account), all GBP/USD, small lot sizes, large
percentage swings per trade (individual scalps showing -30% to -60%
return on that trade's margin) — tight, leveraged scalping rather than
position trading.

**Takeaway**: this is the vrbnca pattern's actual endpoint, from the same
trader's own longer-running account rather than inferred risk. Enough
time running a high-frequency, highly-leveraged style eventually turns a
"+317% this month" narrative into "-97.5% this year, balance $1" — the
three accounts side by side make that trajectory visible in one dataset
instead of requiring speculation about what might happen later.

## Contrast: what disciplined process looks like (~/repos/money-making)

The vrbnca and IMforex case studies above show what happens *without*
guardrails against luck, curve-fitting, and compounding risk. A private
NSE/Kite quant-research project on this same machine
(`~/repos/money-making`) is a useful contrast — not a forum thread, but a
working example of a process built specifically to catch these failure
modes before they reach real capital:

- **Walk-forward split as a hard gate**: every one of 87 tested trading
  mechanisms is split into two time halves; a strategy only "passes" if
  *both* halves are net-positive with no drawdown-halt. Most fail — "0/216
  passed," "2/12 passed," "3/12 passed" are typical results throughout
  the project's log, the mirror image of the forum accounts treating one
  good month as proof.
- **Honest multiple-comparisons correction**: p-values are tracked across
  the whole project and checked against a Bonferroni-corrected threshold
  that gets stricter as more strategies are tested — a result with
  p=0.0002 (the pre-holiday effect) is still explicitly logged as
  *failing* the corrected bar, rather than being cherry-picked as a win.
- **Survivorship-bias stress tests**: findings are re-run with real
  historical stock blowups (e.g. JETAIRWAYS, DHFL) added back into the
  universe, specifically to check whether the edge only exists because
  the dataset quietly excludes companies that went to zero — the same
  blind spot that made IMforex's newer accounts look great in isolation.
- **Fixed risk sizing, tested for breaking points**: position sizing is
  tested explicitly (`--risk-per-trade-pct`), and the log repeatedly
  documents where *increasing* leverage breaks a strategy ("2% breaks
  it — drawdown-halted") rather than treating bigger size as free
  upside — the opposite instinct from a martingale/grid approach.
- **A hard drawdown ceiling used to reject, not bypass**: a
  `RiskManager` drawdown-from-peak breaker disqualifies any strategy that
  breaches it during testing, rather than being something to "ride
  through" as IMforex's oldest account effectively did on the way to a
  $1 balance.

**Current status**: 87 mechanisms tested, exactly one ("IBS rotation," a
diversified 5-stock rotation) is a standing finding, running in a live
*paper*-tracker (no real capital, no leverage) — and even that is
explicitly marked "nothing is declared tradable" pending further
validation. No martingale/grid patterns, no single-month hype, no
undiagnosed survivorship bias found in this project — it's built to
surface exactly those problems before they become losses, which is the
gap that was missing in the vrbnca and IMforex accounts above.
