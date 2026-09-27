# GME (GameStop)

## Price

~$22.76 as of 2026-09-21 (most recent found), prev close $22.64, day range
$22.52–$23.11, 52-week range $17.79–$28.10. No more recent tick surfaced
(Nasdaq/GameStop IR pages are JS-rendered and didn't return data via
automated fetch).

## Short interest metrics (from search/aggregator snippets, not a single
authoritative live source — cross-check before acting on these)

- **Short interest % of float**: ~20% as of late July 2026 (up from
  ~16.35% / 66.88M shares short in March 2026)
- **Days to cover**: ~9.4 days (as of 2026-04-15; 62M shares short ÷
  6.61M avg daily volume)
- **Borrow rate**: <1% annualized (reported ~0.4-0.48%, several million
  shares available to borrow) — a low/easy-to-borrow reading

For comparison, GME's 2021 peak short interest was reported at **226% of
float**, with borrow fees spiking into the hundreds of percent at the
extreme. Today's numbers are a completely different, unremarkable order
of magnitude.

## Failure-to-deliver (FTD) — SEC primary source

Pulled directly from SEC.gov's `cnsfails` fails-to-deliver data files
(`cnsfails202608a.zip` / `cnsfails202608b.zip`, first/second half of
August 2026), filtered to symbol GME. Raw data: [`data/gme_ftd_august_2026.csv`](data/gme_ftd_august_2026.csv).

| Settlement Date | FTD Shares | Price |
|---|---|---|
| 2026-08-03 | 15,411 | $21.72 |
| 2026-08-04 | 590,586 | $19.06 |
| 2026-08-05 | 1,886 | $19.21 |
| 2026-08-06 | 54,733 | $19.01 |
| 2026-08-10 | 166,186 | $19.16 |
| 2026-08-11 | 28,026 | $18.79 |
| 2026-08-17 | 56,718 | $18.66 |
| 2026-08-21 | 21,091 | $18.04 |
| 2026-08-24 | 37,185 | $18.21 |
| 2026-08-25 | 93,558 | $18.04 |
| 2026-08-27 | 102 | $17.97 |
| 2026-08-28 | 57,727 | $18.25 |
| 2026-08-31 | 575 | $17.87 |

**August 2026 total: ~1,123,784 shares failed to deliver**, heavily
concentrated in one day (Aug 4 alone = 590,586, over half the month's
total). Against ~6-7M average daily trading volume, even the largest
single day is under 10% of one day's volume — this is a normal range for
a moderately liquid stock, not a pattern that would put GME on the SEC's
Reg SHO threshold list.

## Note on community narrative

The /GME/ "general" thread this research responds to frames the stock
around a "MOASS" (mother of all short squeezes) thesis — claiming shorts
"never closed" and naked shorting has created more synthetic shares than
real ones, treated as settled fact ("Unfuddable"). None of the actual
regulatory data above (short interest, days-to-cover, borrow rate, FTDs)
supports that framing as of Sept 2026 — it's a real, legal short position
at an unremarkable level, not evidence of an imminent extraordinary event.
