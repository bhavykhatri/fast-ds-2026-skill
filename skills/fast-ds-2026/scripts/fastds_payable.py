#!/usr/bin/env python3
"""FAST-DS 2026: amount payable and payment timeline.

Examples
  # Compute payable from category totals (INR)
  python fastds_payable.py --cat1 250000 --cat2 yes

  # Timeline for a Form 2 order (amount from Form 2 row 6)
  python fastds_payable.py --form2-date 2026-11-15 --payable 250000

  # Both, plus interest if paying on a given date
  python fastds_payable.py --cat1 500000 --cat2 no --form2-date 2026-11-30 --pay-date 2027-02-03

Rules (Finance Act 2026 s.133, s.135; FAST-DS Rules 2026 Rule 7; CBDT FAQ Q41-44):
  * Category 1 (Table Sl. 1): 30% tax + equal additional amount = 60% of value; cap Rs 1 crore.
  * Category 2 (Table Sl. 2): flat fee Rs 1,00,000 for all such assets; cap Rs 5 crore.
  * Pay within 2 months from the end of the month Form 2 is received.
  * Up to 2 further months at 1% simple interest per month or part of a month.
  * After that the declaration is void.
Not legal advice. Verify against Form 2 and the official texts.
"""
import argparse
import calendar
import datetime as dt

CAT1_CAP = 1_00_00_000
CAT2_CAP = 5_00_00_000
CAT2_FEE = 1_00_000


def end_of_month(d: dt.date, add_months: int = 0) -> dt.date:
    y, m = d.year, d.month + add_months
    y += (m - 1) // 12
    m = (m - 1) % 12 + 1
    return dt.date(y, m, calendar.monthrange(y, m)[1])


def months_late(due: dt.date, paid: dt.date) -> int:
    """Number of months or part thereof after `due` (month-end based)."""
    if paid <= due:
        return 0
    n = 0
    boundary = due
    while paid > boundary:
        n += 1
        boundary = end_of_month(due, n)
    return n


def inr(x: int) -> str:
    s = str(int(x))
    if len(s) <= 3:
        return "Rs " + s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return "Rs " + ",".join(parts) + "," + tail


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--cat1", type=float, help="Category 1 total in INR (assets FMV + undisclosed income)")
    p.add_argument("--cat2", choices=["yes", "no"], help="Any Category 2 asset declared?")
    p.add_argument("--cat2-value", type=float, help="Category 2 aggregate FMV in INR (for the cap check)")
    p.add_argument("--payable", type=float, help="Amount in Form 2 row 6 (overrides computed value)")
    p.add_argument("--form2-date", help="Date Form 2 was received, YYYY-MM-DD")
    p.add_argument("--pay-date", help="Planned payment date, YYYY-MM-DD")
    a = p.parse_args()

    payable = None
    if a.cat1 is not None or a.cat2 is not None:
        cat1 = a.cat1 or 0
        # Form 2 rounds the 60% figure once; split it for display only.
        sixty = round(cat1 * 0.60)
        tax = round(cat1 * 0.30)
        additional = sixty - tax
        fee = CAT2_FEE if a.cat2 == "yes" else 0
        payable = sixty + fee
        print("Amount payable")
        print(f"  Category 1 value        {inr(round(cat1))}")
        if cat1 > CAT1_CAP:
            print("  !! Category 1 exceeds Rs 1 crore: Category 1 is NOT available.")
        print(f"  Tax 30%                 {inr(tax)}")
        print(f"  Additional amount 100%  {inr(additional)}")
        print(f"  Category 2 fee          {inr(fee)}")
        if a.cat2_value and a.cat2_value > CAT2_CAP:
            print("  !! Category 2 exceeds Rs 5 crore: Category 2 is NOT available.")
        print(f"  TOTAL                   {inr(payable)}")
        print("  Challan ITNS 289 breakup: (a) Tax = 60% amount, (b) Fee = Category 2 fee, (c) Interest")
        print()

    if a.payable is not None:
        payable = a.payable

    if a.form2_date:
        f2 = dt.date.fromisoformat(a.form2_date)
        due = end_of_month(f2, 2)
        print(f"Payment timeline (Form 2 received {f2:%d-%b-%Y})")
        print(f"  No interest:            pay by {due:%d-%b-%Y}")
        for k in (1, 2):
            d = end_of_month(f2, 2 + k)
            extra = f"  interest {inr(round(payable * 0.01 * k))}" if payable else ""
            print(f"  With {k}% interest:       pay by {d:%d-%b-%Y}{extra}")
        void = end_of_month(f2, 4)
        print(f"  After {void:%d-%b-%Y}: declaration void, nothing refundable")
        if a.pay_date:
            pd = dt.date.fromisoformat(a.pay_date)
            n = months_late(due, pd)
            if n > 2:
                print(f"  Paying on {pd:%d-%b-%Y} is TOO LATE (outer limit {void:%d-%b-%Y}).")
            elif payable:
                interest = round(payable * 0.01 * n)
                print(f"  Paying on {pd:%d-%b-%Y}: {n} month(s) late, interest {inr(interest)}, total {inr(round(payable) + interest)}")
            else:
                print(f"  Paying on {pd:%d-%b-%Y}: {n} month(s) late (interest 1% x {n} of the outstanding amount)")


if __name__ == "__main__":
    main()
