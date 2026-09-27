"""
Sweep the ADX threshold from structure_adx_backtest.py across several
values instead of just the classic 25, to check whether 25 specifically
was doing something meaningful or whether the first/second-half split
found there holds across the whole range (i.e. is a strength filter
*at all* helpful, regardless of the exact cutoff).
"""
import json
import datetime

with open('../data/btc_daily.json') as f:
    raw = json.load(f)

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

N = 2
ADX_PERIOD = 14


def find_swings(bars):
    highs, lows = {}, {}
    for i in range(N, len(bars) - N):
        window = bars[i - N:i + N + 1]
        h, l = bars[i]['high'], bars[i]['low']
        if h == max(b['high'] for b in window):
            highs[i] = h
        if l == min(b['low'] for b in window):
            lows[i] = l
    return highs, lows


def compute_adx(bars, period=14):
    n = len(bars)
    tr = [0.0] * n
    plus_dm = [0.0] * n
    minus_dm = [0.0] * n
    for i in range(1, n):
        high, low, prev_close = bars[i]['high'], bars[i]['low'], bars[i - 1]['close']
        prev_high, prev_low = bars[i - 1]['high'], bars[i - 1]['low']
        tr[i] = max(high - low, abs(high - prev_close), abs(low - prev_close))
        up_move = high - prev_high
        down_move = prev_low - low
        plus_dm[i] = up_move if (up_move > down_move and up_move > 0) else 0.0
        minus_dm[i] = down_move if (down_move > up_move and down_move > 0) else 0.0

    smoothed_tr = [0.0] * n
    smoothed_plus_dm = [0.0] * n
    smoothed_minus_dm = [0.0] * n
    adx = [None] * n
    dx = [0.0] * n

    smoothed_tr[period] = sum(tr[1:period + 1])
    smoothed_plus_dm[period] = sum(plus_dm[1:period + 1])
    smoothed_minus_dm[period] = sum(minus_dm[1:period + 1])

    for i in range(period + 1, n):
        smoothed_tr[i] = smoothed_tr[i - 1] - (smoothed_tr[i - 1] / period) + tr[i]
        smoothed_plus_dm[i] = smoothed_plus_dm[i - 1] - (smoothed_plus_dm[i - 1] / period) + plus_dm[i]
        smoothed_minus_dm[i] = smoothed_minus_dm[i - 1] - (smoothed_minus_dm[i - 1] / period) + minus_dm[i]

    for i in range(period, n):
        if smoothed_tr[i] == 0:
            continue
        plus_di = 100 * smoothed_plus_dm[i] / smoothed_tr[i]
        minus_di = 100 * smoothed_minus_dm[i] / smoothed_tr[i]
        denom = plus_di + minus_di
        dx[i] = 100 * abs(plus_di - minus_di) / denom if denom != 0 else 0.0

    first_adx_idx = period * 2
    if first_adx_idx < n:
        adx[first_adx_idx] = sum(dx[period + 1:first_adx_idx + 1]) / period
        for i in range(first_adx_idx + 1, n):
            adx[i] = (adx[i - 1] * (period - 1) + dx[i]) / period
    return adx


swing_highs, swing_lows = find_swings(bars)
adx = compute_adx(bars, ADX_PERIOD)


def run_strategy(bars, start_idx, end_idx, threshold):
    position = 0
    last_swing_high = None
    last_swing_low = None
    equity = 1.0
    peak = 1.0
    max_dd = 0.0
    trades = 0

    for i in range(start_idx, end_idx):
        confirmed_idx = i - N
        if confirmed_idx in swing_highs:
            last_swing_high = swing_highs[confirmed_idx]
        if confirmed_idx in swing_lows:
            last_swing_low = swing_lows[confirmed_idx]

        close = bars[i]['close']
        prev_close = bars[i - 1]['close']
        r = (close - prev_close) / prev_close if position == 1 else 0.0
        equity *= (1 + r)
        peak = max(peak, equity)
        max_dd = min(max_dd, (equity - peak) / peak)

        strong_enough = adx[i] is not None and adx[i] > threshold

        if last_swing_high is not None and close > last_swing_high and position == 0:
            if strong_enough:
                position = 1
                trades += 1
        elif last_swing_low is not None and close < last_swing_low and position == 1:
            position = 0
            trades += 1

    n_days = end_idx - start_idx
    ann_return = (equity ** (365 / n_days)) - 1 if n_days > 0 else 0
    return {'ann_return_pct': ann_return * 100, 'max_drawdown_pct': max_dd * 100, 'trades': trades}


n = len(bars)
mid = n // 2
adx_start = ADX_PERIOD * 2 + 1
thresholds = [15, 20, 25, 30, 35, 40, 45]

for label, s, e in [('FULL PERIOD', adx_start, n), ('FIRST HALF', adx_start, mid), ('SECOND HALF', mid, n)]:
    print(f"== {label} ({bars[s]['date']} to {bars[e-1]['date']}) ==")
    for t in thresholds:
        res = run_strategy(bars, s, e, t)
        print(f"  ADX > {t:>2}: {res['ann_return_pct']:6.1f}%/yr, max DD {res['max_drawdown_pct']:6.1f}%, {res['trades']:3} trades")
    print()
