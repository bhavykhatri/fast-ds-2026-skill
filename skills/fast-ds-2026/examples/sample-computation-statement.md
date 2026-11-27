# SAMPLE — Computation Statement for Declaration in Form 1 (FAST-DS 2026)

> **This is a fictional example.** The person, employer, broker, prices and exchange rates are made up (the SBI TT rates and the 31-3-2026 share prices are illustrative; only the ₹94.6543 RBI/FBIL rate is real). Use the structure, not the numbers. Reproduce the figures with:
> ```
> python scripts/sbi_tt_rate.py --csv examples/sample_sbi_rates.csv --in examples/sample_income.csv
> python scripts/quoted_share_fmv.py --high 420 --low 410 --groups examples/sample_groups.csv
> python scripts/fastds_payable.py --cat1 32878 --cat2 yes --cat2-value 1040960
> ```
> Upload the real statement as a PDF (no internal notes, no review comments) inside both the income ZIP and the asset ZIP.

---

**Foreign Assets of Small Taxpayers – Disclosure Scheme, 2026**
**Statement of computation in support of the declaration in Form 1**
(Finance Act, 2026, Chapter IV, sections 130–144, read with the FAST-DS Rules, 2026)

| | |
|---|---|
| Declarant | A. Sample (PAN: XXXXX0000X) |
| Status | Individual, Resident and Ordinarily Resident in every previous year covered |
| Foreign account | Brokerage account with Example Brokerage LLC, USA (account ending ••••) |
| Valuation date | 31 March 2026 |
| Prepared on | DD-MM-2026 |

## 1. Background
1. The declarant is a salaried employee of an Indian subsidiary of Example Corp., a company listed on NASDAQ (ticker EXMP).
2. Since FY 2021-22 the declarant has received Restricted Stock Units (RSUs) of Example Corp., credited to the brokerage account above. The fair market value of every vest was taxed in India as a perquisite under s.17(2)(vi) and is shown in Form 12BA for each year (Annexure D, items 5–8).
3. The shares were not reported in Schedule FA of the returns filed for AY 2022-23 to AY 2025-26, all filed before 16-08-2026.
4. Cash dividends paid on the shares (US tax withheld at 25%) were not offered to tax in those returns.
5. No proceedings under the Black Money Act have been completed for any of these years, and the assets are not proceeds of crime under the PMLA (s.140).

## 2. Summary of declaration
| Part | Category (s.133 Table) | Item | Amount (₹) |
|---|---|---|---|
| B-2 / Annexure I1 | Sl. No. 1 — undisclosed foreign income | Dividends, FY 2022-23 to FY 2025-26 (Annexure A) | 32,878 |
| B-4 / Annexure A5 | Sl. No. 2(b) — asset acquired from income offered to tax, not declared in Schedule FA | Shares of Example Corp. (Annexure B) | 10,40,960 |

| Test | Limit | This declaration | Result |
|---|---|---|---|
| Category 1 aggregate (s.133 Sl. 1) | ≤ ₹1,00,00,000 | ₹32,878 | Within limit |
| Category 2 aggregate (s.133 Sl. 2) | ≤ ₹5,00,00,000 | ₹10,40,960 | Within limit |

## 3. Amount payable
| | ₹ |
|---|---|
| Tax and additional amount on Category 1: 60% × 32,878 | 19,727 |
| Fee for Category 2 | 1,00,000 |
| **Total payable (Form 1, Part D item 7)** | **1,19,727** |

## 4. Basis of computation
1. **Undisclosed foreign income (s.131(1)(k))** is income chargeable to tax in India and is therefore computed under the Income-tax Act. Each dividend is taken gross (before US withholding; no foreign tax credit is claimed — CBDT FAQ Q87) and converted at the SBI telegraphic transfer buying rate on the last day of the month preceding the month of receipt (Rule 115 of the Income-tax Rules, 1962). Where no rate was published on that day, the rate of the nearest earlier day is used.
2. **Shares (Rule 3(1)(c))** are valued at the higher of cost of acquisition and the average of the lowest and highest price on NASDAQ on 31-03-2026, applied separately to each acquisition-year group. Cost of RSUs is their fair market value at vest, as taxed in India (s.49(2AA)).
3. **Currency conversion for assets (Rule 3(4); CBDT FAQ Q55):** the RBI/FBIL reference rate for USD was not published on 31-03-2026; the last available rate, ₹94.6543 per USD of 30-03-2026, is used.
4. An asset held across several years is reported once, in the earliest relevant previous year of acquisition of each group (CBDT FAQ Q93). Fractional shares are valued at their exact quantity (CBDT FAQ Q73).
5. Dividends were received in cash and withdrawn; none was reinvested in the shares, so no adjustment under Rule 3(3) arises.

## Annexure A — Undisclosed foreign income (dividends)
| # | Date received | Previous year | Gross USD | Rule 115 date | SBI TT buy (₹) | INR |
|---|---|---|---|---|---|---|
| 1 | 09-06-2022 | 2022-23 | 90.00 | 31-05-2022 | 77.40 | 6,966 |
| 2 | 08-06-2023 | 2023-24 | 100.00 | 31-05-2023 | 82.30 | 8,230 |
| 3 | 13-06-2024 | 2024-25 | 100.00 | 31-05-2024 | 83.10 | 8,310 |
| 4 | 12-06-2025 | 2025-26 | 110.00 | 30-05-2025 * | 85.20 | 9,372 |
| | | | **400.00** | | | **32,878** |

\* 31-05-2025 was a non-publication day; rate of 30-05-2025 used.

Form 1 Annexure I1 rows (one per previous year and type): 2022-23 Dividend ₹6,966 · 2023-24 Dividend ₹8,230 · 2024-25 Dividend ₹8,310 · 2025-26 Dividend ₹9,372. Country: United States of America. Status: Resident.

## Annexure B — Shares held on 31-03-2026 (Rule 3(1)(c))
Price on 31-03-2026: high USD 420.00, low USD 410.00, average **USD 415.00**. FX ₹94.6543.

| Group (previous year of acquisition) | Quantity | Cost (₹) | Market value: qty × 415.00 × 94.6543 (₹) | Value under Rule 3 (₹) | Basis |
|---|---|---|---|---|---|
| 2021-22 | 12.0000 | 2,80,000 | 4,71,378 | 4,71,378 | Market |
| 2022-23 | 8.5000 | 2,40,000 | 3,33,893 | 3,33,893 | Market |
| 2023-24 | 6.0000 | 2,30,000 | 2,35,689 | 2,35,689 | Market |
| **Total** | **26.5000** | **7,50,000** | | **10,40,960** | |

Reconciliation: 26.5000 shares = holding statement of Example Brokerage as at 31-03-2026 (Annexure D, item 2). No shares vested after FY 2023-24 and none were sold. The declarant holds no other asset outside India.

## Annexure C — Assets transferred before 31-03-2026 (Rule 3(2))
None in this example. Where shares were sold, list each lot: acquisition date, quantity, cost, sale date, sale price, and value = higher of cost and sale consideration.

## Annexure D — Documents relied on
| # | Document | In ZIP |
|---|---|---|
| 1 | This computation statement | Income, Asset |
| 2 | Brokerage holding statement as at 31-03-2026 | Asset |
| 3 | Brokerage year-end reports, CY2021–CY2025 | Asset |
| 4 | Brokerage transaction summaries (dividends, vests), FY 2021-22 to FY 2025-26 | Income, Asset |
| 5–8 | Form 12BA, FY 2021-22 to FY 2024-25 (RSU perquisites taxed) | Asset |
| 9 | Form 1042-S, CY2022–CY2025 | Income |
| 10 | AIS — Foreign Assets Information, CY2022 onwards | Income |
| 11 | Price evidence for 31-03-2026 (high/low) and RBI/FBIL USD rate of 30-03-2026, with retrieval date | Asset |
| 12 | SBI TT buying rates used (Annexure A) with source | Income |

## Declaration
I declare that the particulars above are true and complete to the best of my knowledge, and are computed from the documents listed in Annexure D.

Place: ________  Date: ________  Signature: A. Sample
