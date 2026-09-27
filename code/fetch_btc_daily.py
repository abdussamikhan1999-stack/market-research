"""Fetch full BTCUSDT daily OHLC history from Binance's public API (no key
required) and save it as data/btc_daily.json for structure_backtest.py."""
import urllib.request
import json
import time


def fetch(symbol, start_ms, end_ms):
    url = (
        f'https://api.binance.com/api/v3/klines?symbol={symbol}'
        f'&interval=1d&startTime={start_ms}&endTime={end_ms}&limit=1000'
    )
    with urllib.request.urlopen(url) as r:
        return json.load(r)


def fetch_all(symbol='BTCUSDT', start_ms=1502928000000, end_ms=None):
    if end_ms is None:
        end_ms = int(time.time() * 1000)
    all_rows = []
    cur = start_ms
    while cur < end_ms:
        rows = fetch(symbol, cur, end_ms)
        if not rows:
            break
        all_rows.extend(rows)
        cur = rows[-1][0] + 86400000
        time.sleep(0.3)
    return all_rows


if __name__ == '__main__':
    rows = fetch_all()
    print(f'Fetched {len(rows)} daily candles')
    with open('../data/btc_daily.json', 'w') as f:
        json.dump(rows, f)
