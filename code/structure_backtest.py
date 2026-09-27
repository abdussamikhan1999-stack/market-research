"""
Test one well-defined, objectively-codeable "market structure" method:
swing high/low breaks (the core mechanic behind Dow Theory trend
definition and modern "break of structure" / SMC price action).

Method:
  - Swing high/low = local extreme confirmed by N bars on each side
    (5-bar fractal, N=2 — standard Williams fractal definition).
  - Bullish break of structure (BOS): daily close trades above the most
    recent confirmed swing high -> go long (or stay long).
  - Bearish BOS: daily close trades below the most recent confirmed
    swing low -> go flat / go short.
  - This is a pure trend-following breakout system using swing pivots
    instead of a fixed N-day lookback (vs. e.g. Donchian/Turtle rules).

Compared against buy-and-hold on the same instrument, split into two
time halves (this project's/`money-making`'s own walk-forward
convention) rather than reporting one whole-period number.
"""
import json
import statistics
import datetime

with open('../data/btc_daily.json') as f:
    raw = json.load(f)

# [open_time, open, high, low, close, volume, ...]
bars = [
    {
        'date': datetime.datetime.fromtimestamp(r[0] / 1000, datetime.UTC).strftime('%Y-%m-%d'),
        'open': float(r[1]),
        'high': float(r[2]),
        'low': float(r[3]),
        'close': float(r[4]),
    }
    for r in raw
]

N = 2  # bars on each side for fractal confirmation


def find_swings(bars):
    highs = {}
    lows = {}
    for i in range(N, len(bars) - N):
        window = bars[i - N:i + N + 1]
        h = bars[i]['high']
        l = bars[i]['low']
        if h == max(b['high'] for b in window):
            highs[i] = h
        if l == min(b['low'] for b in window):
            lows[i] = l
    return highs, lows


swing_highs, swing_lows = find_swings(bars)


def run_strategy(bars, start_idx, end_idx):
    """Long/flat only (no shorting) — go long on bullish BOS, flat on bearish BOS."""
    position = 0  # 0 = flat, 1 = long
    entry_price = None
    last_swing_high = None
    last_swing_low = None
    equity = 1.0
    peak = 1.0
    max_dd = 0.0
    trades = 0
    daily_returns = []

    for i in range(start_idx, end_idx):
        # a swing pivot at index j is only CONFIRMED (visible to a real-time
        # trader) once the N bars after it exist, i.e. at index j+N — not at
        # j itself. Referencing swing_highs[i] at bar i would be look-ahead.
        confirmed_idx = i - N
        if confirmed_idx in swing_highs:
            last_swing_high = swing_highs[confirmed_idx]
        if confirmed_idx in swing_lows:
            last_swing_low = swing_lows[confirmed_idx]

        close = bars[i]['close']
        prev_close = bars[i - 1]['close']

        # mark-to-market daily return while holding
        if position == 1:
            r = (close - prev_close) / prev_close
        else:
            r = 0.0
        daily_returns.append(r)
        equity *= (1 + r)
        peak = max(peak, equity)
        dd = (equity - peak) / peak
        max_dd = min(max_dd, dd)

        # structure-break signals (confirmed swing must be from the past, no lookahead)
        if last_swing_high is not None and close > last_swing_high and position == 0:
            position = 1
            entry_price = close
            trades += 1
        elif last_swing_low is not None and close < last_swing_low and position == 1:
            position = 0
            entry_price = None
            trades += 1

    n_days = end_idx - start_idx
    total_return = equity - 1
    ann_return = (equity ** (365 / n_days)) - 1 if n_days > 0 else 0
    return {
        'total_return_pct': total_return * 100,
        'ann_return_pct': ann_return * 100,
        'max_drawdown_pct': max_dd * 100,
        'trades': trades,
        'days': n_days,
    }


def buy_and_hold(bars, start_idx, end_idx):
    start_price = bars[start_idx]['close']
    end_price = bars[end_idx - 1]['close']
    total_return = (end_price / start_price) - 1
    n_days = end_idx - start_idx
    ann_return = ((1 + total_return) ** (365 / n_days)) - 1

    peak = start_price
    max_dd = 0.0
    for i in range(start_idx, end_idx):
        peak = max(peak, bars[i]['close'])
        dd = (bars[i]['close'] - peak) / peak
        max_dd = min(max_dd, dd)

    return {
        'total_return_pct': total_return * 100,
        'ann_return_pct': ann_return * 100,
        'max_drawdown_pct': max_dd * 100,
    }


n = len(bars)
mid = n // 2

print(f"Total bars: {n} ({bars[0]['date']} to {bars[-1]['date']})")
print(f"Swing highs found: {len(swing_highs)}, swing lows found: {len(swing_lows)}\n")

for label, s, e in [('FULL PERIOD', N, n), ('FIRST HALF', N, mid), ('SECOND HALF', mid, n)]:
    strat = run_strategy(bars, s, e)
    bh = buy_and_hold(bars, s, e)
    print(f"== {label} ({bars[s]['date']} to {bars[e-1]['date']}, {e-s} days) ==")
    print(f"  Structure-break strategy: {strat['ann_return_pct']:.1f}%/yr, "
          f"max DD {strat['max_drawdown_pct']:.1f}%, {strat['trades']} trades")
    print(f"  Buy & hold:               {bh['ann_return_pct']:.1f}%/yr, "
          f"max DD {bh['max_drawdown_pct']:.1f}%")
    print()
