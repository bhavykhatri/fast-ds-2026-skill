#!/usr/bin/env python3
"""Rule 115 rate lookup: SBI TT buying rate (USD/INR) on the last day of the
month preceding each income date (nearest earlier published date if that day
has no rate).

Data: https://github.com/sahilgupta/sbi-fx-ratekeeper (csv_files/SBI_REFERENCE_RATES_USD.csv)

Usage
  python sbi_tt_rate.py 2024-06-13 2024-09-12            # downloads the CSV
  python sbi_tt_rate.py --csv rates.csv 2024-06-13        # use a local copy
  python sbi_tt_rate.py --csv rates.csv --in items.csv --out items_inr.csv
      items.csv columns: date (YYYY-MM-DD), amount_usd [, any others]
"""
import argparse
import calendar
import csv
import datetime as dt
import io
import sys
import urllib.request

URL = ("https://raw.githubusercontent.com/sahilgupta/sbi-fx-ratekeeper/main/"
       "csv_files/SBI_REFERENCE_RATES_USD.csv")


def load_rates(path=None):
    if path:
        text = open(path, encoding="utf-8").read()
    else:
        with urllib.request.urlopen(URL, timeout=30) as r:
            text = r.read().decode("utf-8")
    rates = {}
    for row in csv.DictReader(io.StringIO(text)):
        d = (row.get("DATE") or row.get("Date") or "").strip()[:10]
        v = (row.get("TT BUY") or row.get("TT_BUY") or "").strip()
        try:
            day = dt.date.fromisoformat(d)
            val = float(v)
        except ValueError:
            continue
        if val > 0:
            rates[day] = val  # last value of the day wins
    if not rates:
        sys.exit("No rates parsed - check the CSV columns (expected DATE, TT BUY).")
    return rates


def rule115_date(income_date: dt.date) -> dt.date:
    first = income_date.replace(day=1)
    return first - dt.timedelta(days=1)


def lookup(rates, income_date: dt.date):
    target = rule115_date(income_date)
    d = target
    for _ in range(15):
        if d in rates:
            return target, d, rates[d]
        d -= dt.timedelta(days=1)
    raise KeyError(f"No SBI TT buying rate within 15 days before {target}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("dates", nargs="*", help="Income dates YYYY-MM-DD")
    p.add_argument("--csv", help="Local copy of SBI_REFERENCE_RATES_USD.csv")
    p.add_argument("--in", dest="inp", help="CSV with date, amount_usd columns")
    p.add_argument("--out", help="Output CSV (with rate and INR)")
    a = p.parse_args()
    rates = load_rates(a.csv)

    if a.inp:
        rows = list(csv.DictReader(open(a.inp, encoding="utf-8")))
        for r in rows:
            target, used, rate = lookup(rates, dt.date.fromisoformat(r["date"]))
            r["rule115_date"], r["rate_date_used"], r["sbi_tt_buy"] = target, used, rate
            r["amount_inr"] = round(float(r["amount_usd"]) * rate, 2)
        out = open(a.out, "w", newline="", encoding="utf-8") if a.out else sys.stdout
        w = csv.DictWriter(out, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
        return

    for s in a.dates:
        target, used, rate = lookup(rates, dt.date.fromisoformat(s))
        note = "" if used == target else f" (no rate on {target}, used {used})"
        print(f"{s}: Rule 115 date {target}, SBI TT buy {rate}{note}")


if __name__ == "__main__":
    main()
