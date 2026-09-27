# Chart structure analysis: methods and one honest backtest

## The landscape

Most "chart structure" methods trace back to one core idea, just with
different vocabulary layered on top:

- **Dow Theory** (1900s, the origin): an uptrend is a sequence of higher
  highs and higher lows; a downtrend is lower highs and lower lows. Trend
  continues until that pattern breaks.
- **Swing structure / "Break of Structure" (BOS) & "Change of Character"
  (CHoCH)** — today's retail "Smart Money Concepts"/ICT vocabulary, but
  mechanically identical to Dow Theory: mark swing highs/lows, trade
  breaks in the trend direction (BOS = continuation), flag breaks against
  it (CHoCH = possible reversal).
- **Wyckoff Method** (1930s): overlays volume onto structure —
  accumulation/distribution ranges, "springs" (fake breakdowns that trap
  sellers) and "upthrusts" (fake breakouts that trap buyers), used to
  infer institutional positioning from price/volume behavior at range
  extremes.
- **Elliott Wave Theory**: claims markets move in fractal 5-wave impulse
  / 3-wave corrective patterns. Not tested here — the wave count is
  subjective enough that two Elliott analysts routinely disagree on the
  same chart; there's no unambiguous rule to code.
- **Volume Profile / Market Profile**: structure defined by *where
  volume traded*, not just price — Point of Control (highest-volume
  price) and Value Area act as dynamic support/resistance.
- **Classical chart patterns** (head-and-shoulders, triangles, flags):
  the oldest retail method. Lo, Mamaysky & Wang (2000) found some
  statistical information content in these patterns academically, but
  nothing that clearly survived transaction costs — consistent with the
  finding below.

Only the swing-structure/BOS mechanic is objectively codeable without
subjective judgment calls, which is why it's the one tested here.

## The test: swing-structure breaks on 8 years of real BTC data

**Method** (`code/structure_backtest.py`): 5-bar Williams fractal swing
highs/lows on daily BTCUSDT (Binance, 2017-08 to 2025-09, 2,967 days,
fetched via `code/fetch_btc_daily.py`). Go long on a confirmed close
above the last swing high, go flat on a confirmed close below the last
swing low. Split into two halves, same walk-forward convention used
elsewhere in this repo.

**A look-ahead bug worth naming**: the first pass let the strategy "see"
a swing high/low the moment it printed — but a swing pivot isn't
confirmed until N bars *after* it forms (you need the following bars to
stay lower to know it was a peak). That inflated the first-half return
from 58.5%/yr to a false 99%/yr. Fixed before trusting any number — see
the `confirmed_idx = i - N` comment in the code.

**Honest results (look-ahead bias removed):**

| Period | Strategy | Buy & hold |
|---|---|---|
| Full (2017-2025) | 39.3%/yr, **-69.6%** max DD, 138 trades | 50.4%/yr, **-83.2%** max DD |
| First half | 58.5%/yr, -69.6% max DD, 73 trades | 81.9%/yr, -83.2% max DD |
| Second half | 23.0%/yr, -51.4% max DD, 64 trades | 25.0%/yr, -76.6% max DD |

**Verdict**: the method does **not** beat raw buy-and-hold on total
return in either half — expected, since it's competing against holding
through one of the strongest bull markets in financial history, a nearly
impossible bar for any timing system to clear. But it consistently cuts
max drawdown by 12-25 percentage points in both halves, and roughly
matches buy-and-hold's return in the more recent, less-trending half.

**Takeaway**: structure-based exits are a risk-management tool here, not
an alpha source — matching how the traders who actually use this stuff
(ICT/SMC/Wyckoff practitioners) describe it themselves: an entry-timing
and risk-definition framework layered onto a broader thesis, not a
standalone edge. This test also doesn't subtract trading costs (138
trades x real spread/fees would erode the thin edge further), so treat
even this modest result as an upper bound. Single instrument (BTC only),
not cross-validated against other assets.

## Follow-up: does filtering "structure" by "strength" (ADX) help?

"Structure" (the swing high/low shape above) and "strength" (how much
conviction is behind a move) are different things. The plain version
above takes every structure break literally, with no regard for whether
the breakout has real momentum behind it. This follow-up
(`code/structure_adx_backtest.py`) adds a Wilder ADX(14) filter: only
take a bullish break-of-structure entry if ADX > 25 (the classic
"trending, not choppy" threshold) at the time of the break. Exits on a
bearish break stay unconditional — risk management shouldn't wait on a
filter to get out.

Note: the ADX warm-up period shifts the test's start date slightly later
than the plain-only test above, so the "Plain structure" column here is
recomputed over the identical (shorter) window as "ADX-filtered," not
copy-pasted from the numbers above — they differ slightly for that
reason, not because of any change to the underlying logic.

**Results:**

| Period | Plain structure | ADX-filtered (>25) | Buy & hold |
|---|---|---|---|
| Full (2017-2025) | 41.7%/yr, -69.6% DD, 136 trades | 36.9%/yr, **-55.8%** DD, 92 trades | 53.1%/yr, -83.2% DD |
| First half | 64.4%/yr, -69.6% DD | **78.8%/yr, -47.2%** DD (better on both) | 89.1%/yr, -83.2% DD |
| Second half | 23.0%/yr, -51.4% DD | **5.9%/yr**, -51.1% DD (worse return, same DD) | 25.0%/yr, -76.6% DD |

**Verdict: the filter is not a consistent improvement — it's
regime-dependent, and that inconsistency is the real finding.**

- **First half** (strongly trending bull market): the ADX filter worked
  exactly as the theory predicts — higher return AND much lower
  drawdown, achieved by skipping 72 "weak" signals. Filtering out
  low-conviction breakouts helped when the underlying market was
  genuinely trending.
- **Second half** (choppier, more range-bound): the filter backfired —
  return dropped from 23% to 5.9%, while drawdown barely improved
  (-51.1% vs -51.4%, essentially no difference). It skipped 114 signals
  here, and evidently some of those were genuinely good moves, not just
  noise — ADX>25 doesn't reliably distinguish "real trend" from
  "fakeout" when the underlying regime itself is less trend-driven.

Averaged across the full period this looks like a rough wash on return
with a real drawdown improvement — but that full-period number is really
just the first half's strong result diluted by the second half's poor
one, which would be easy to miss without splitting the halves out
explicitly. "Strength filtering improves structure trading" is not a
universal truth here; it's conditional on being in a genuinely trending
regime, which isn't knowable in advance without hindsight.
