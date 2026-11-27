#!/usr/bin/env python3
"""Rule 3(1)(c) value of quoted shares for FAST-DS 2026.

FMV per group = max(cost in INR, quantity x average(high, low) on 31-3-2026 x FX)
FX default: Rs 94.6543 per USD (RBI/FBIL reference rate of 30-3-2026; none was
published on 31-3-2026 - CBDT FAQ Q55).

Usage
  python quoted_share_fmv.py --ticker AAPL --groups groups.csv
  python quoted_share_fmv.py --high 390.10 --low 381.25 --groups groups.csv

groups.csv columns: label, quantity, cost_inr
  (one row per acquisition-year group; fractional quantities allowed - FAQ Q73)

If no trade on 31-3-2026, use the nearest earlier trading day (FAQ Q25).
Price source (when --ticker is used): Yahoo Finance chart API. Save the
output and the price evidence with your valuation pack.
"""
import argparse
import csv
import datetime as dt
import json
import urllib.request

FX_DEFAULT = 94.6543
VAL_DATE = dt.date(2026, 3, 31)


def fetch_hi_lo(ticker: str):
    start = int(dt.datetime(2026, 3, 20, tzinfo=dt.timezone.utc).timestamp())
    end = int(dt.datetime(2026, 4, 2, tzinfo=dt.timezone.utc).timestamp())
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
           f"?period1={start}&period2={end}&interval=1d")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    data = json.load(urllib.request.urlopen(req, timeout=30))
    res = data["chart"]["result"][0]
    tz = dt.timezone(dt.timedelta(seconds=res["meta"].get("gmtoffset", 0)))
    q = res["indicators"]["quote"][0]
    best = None
    for i, ts in enumerate(res["timestamp"]):
        day = dt.datetime.fromtimestamp(ts, tz).date()
        if day <= VAL_DATE and q["high"][i] is not None:
            best = (day, q["high"][i], q["low"][i])
    if not best:
        raise SystemExit("No trading data on or before 31-3-2026")
    return best


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--ticker")
    p.add_argument("--high", type=float)
    p.add_argument("--low", type=float)
    p.add_argument("--fx", type=float, default=FX_DEFAULT)
    p.add_argument("--groups", required=True)
    a = p.parse_args()

    if a.ticker:
        day, hi, lo = fetch_hi_lo(a.ticker)
        print(f"{a.ticker} on {day}: high {hi:.4f}, low {lo:.4f}")
    elif a.high is not None and a.low is not None:
        hi, lo = a.high, a.low
    else:
        raise SystemExit("Give --ticker or both --high and --low")
    avg = (hi + lo) / 2
    print(f"Average of high and low: {avg:.4f} USD; FX {a.fx}\n")

    total = 0
    print(f"{'group':<20}{'qty':>12}{'market INR':>16}{'cost INR':>16}{'FMV INR':>16}  basis")
    for r in csv.DictReader(open(a.groups, encoding="utf-8")):
        qty = float(r["quantity"])
        cost = float(r["cost_inr"])
        mkt = round(qty * avg * a.fx)
        fmv = max(mkt, round(cost))
        total += fmv
        basis = "market" if mkt >= cost else "cost"
        print(f"{r['label']:<20}{qty:>12.4f}{mkt:>16}{round(cost):>16}{fmv:>16}  {basis}")
    print(f"\nTotal FMV under Rule 3: Rs {total}")


if __name__ == "__main__":
    main()
