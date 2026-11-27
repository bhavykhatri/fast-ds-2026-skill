# Computation guide

Build the numbers in a workbook with **live formulas** so every figure traces to an input. Recalculate in Excel (or LibreOffice) and require zero formula errors before using any figure.

## 1. Income — Category 1(b)
Basis: s.131(1)(k) → income "chargeable to tax in India" → computed under the IT Act.

- **Exchange rate:** Rule 115 — **SBI TT buying rate on the last day of the month before** the income date. If that day has no rate (holiday), use the nearest earlier date. Public CSV: `https://github.com/sahilgupta/sbi-fx-ratekeeper` → `csv_files/SBI_REFERENCE_RATES_USD.csv`. Use `scripts/sbi_tt_rate.py`.
- **Gross amounts.** No credit for foreign tax withheld (FAQ Q87).
- **One row per previous year × income type** (dividends, interest/money-market income, short-term gains, long-term gains, other). Form 1's I1 annexure asks for type, country, previous year, residential status and amount.
- Alternative basis (all income at ₹94.6543 on 31-3-2026): more conservative, usually costs more, non-refundable. Present both if the user wants, and record the choice.

### Capital gains on foreign shares
- Short-term if held **24 months or less**, else long-term. Net gains and losses within each year.
- **RSU cost** = FMV at vest (taxed as a perquisite).
- **ESPP cost** = FMV on the purchase date, because the discount was taxed as a perquisite (s.49(2AA)). Broker statements often show the discounted price: FMV = price paid ÷ (1 − discount). Check the plan's discount (commonly 10% or 15%) on **every** purchase against the year-end report's "purchase date FMV". Don't confuse the payroll contribution rate with the discount.
- Cross-check perquisite values against **Form 12BA** for each year.

### Reconciliation
Reconcile every calendar year to three independent sources: the broker's transaction history = the year-end "income summary" ≈ US Form **1042-S** (whole dollars). Brokers' online transaction search often goes back only ~5 years; recover older months from year-end reports, estimate any split, and label it as an estimate. Scanned 1042-S forms may need rendering and reading visually.

## 2. Assets — Category 1(a) / Category 2
- **Quoted shares held on 31-3-2026:** higher of cost and **average of the day's high and low on 31-3-2026** (Rule 3(1)(c)). Apply **per acquisition-year group** — cost may exceed market for recent lots. Derive groups from year-end share counts plus sales. Cross-check the total quantity against the broker's 31-3-2026 holding statement. Fractions are allowed (FAQ Q73). Use `scripts/quoted_share_fmv.py`.
- **Sold before 31-3-2026:** higher of cost and sale price, **lot by lot** (Rule 3(2)). Valuation date = sale date.
- **Bank account:** sum of all deposits since opening, excluding re-deposits (FAQ Q29–31).
- **Money-market / cash sweep funded by undisclosed dividends:** if still held on 31-3-2026 it's a Category 1(a) asset and the income is reduced by the same amount (net nil, Rule 3(3)). If withdrawn before then, nothing to declare as an asset.
- **FX for assets:** **₹94.6543 per USD** (RBI/FBIL reference rate of 30-3-2026; none published on 31-3-2026 — FAQ Q55).
- **20% tolerance** applies only to valuer-report assets, not bank accounts, indexed cost or income.
- **Multi-year assets** are reported once in the earliest relevant previous year (FAQ Q93).

## 3. Amount payable
`payable = round(0.60 × (Cat1 assets + Cat1 income)) + (100000 if any Cat 2 asset else 0)`

Run `python scripts/fastds_payable.py --cat1 <amount> --cat2 yes --form2-date YYYY-MM-DD` to get the amount and the due-date/interest table.

Caps: Cat 1 total ≤ ₹1,00,00,000; Cat 2 total ≤ ₹5,00,00,000, per declarant.

## 4. BMA ₹20 lakh test
For each calendar/previous year, compute the aggregate value of non-immovable foreign assets and compare with ₹20 lakh. Show the user which years carry BMA s.42/43 exposure (₹10 lakh per asset per year) — that's what the ₹1 lakh fee buys out.

## 5. Suggested workbook sheets
| Sheet | Purpose |
|---|---|
| Summary | Categories, caps test, payable |
| Compliance_Checklist | Eligibility, s.140, scope, decisions |
| Inputs | FX rates (with source and retrieval time), prices, constants |
| Cat1_Income | One row per income item: date, USD, Rule 115 rate, INR, previous year, type |
| Cat1_CapitalGains | Lot-level gains: acquisition date/cost, sale date/price, holding period |
| Form1_I1_Draft | Rows exactly as they'll be entered in Form 1 |
| Cat1_ByFY | Totals per previous year and type |
| Cat2_AssetValuation | Groups/lots: quantity, cost, 31-3-2026 hi/lo average or sale price, FMV |
| Cat2_HeldByYear | Holdings by acquisition year, reconciled to statements |
| Reconciliation | Broker vs year-end report vs 1042-S, per year |
| BMA_20L_Test | Yearly aggregate vs ₹20 lakh |
| Assumptions_Sources | Every assumption and source with a link |
| Review_Log | User decisions, review findings and how they were resolved |
