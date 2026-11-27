# Evidence pack for Form 1

Form 1 asks for supporting documents for income (I1) and a valuation report/proof for assets (A1–A6). Each upload must be a PDF or ZIP **≤ 5 MB** (the portal shows sizes in binary MB).

## Suggested files
| # | File | Contents |
|---|---|---|
| 00 | Entry guide | Field-by-field values to type into Form 1 (internal; not uploaded) |
| 01 | Computation statement | Formal statement, no internal notes. Annexures: A income items, B capital-gain lots, C sold lots (Rule 3(2)), D inputs and sources. See `../examples/sample-computation-statement.md` |
| 02 | Holdings evidence | Broker year-end reports per year + holding statement as at 31-3-2026 |
| 03 | Transaction summaries | Dividends, purchases, sales for the years in scope |
| 04 | Tax forms | US 1042-S (or the relevant foreign tax statements) |
| 05 | Perquisite proof | Form 16 / Form 12BA showing RSU/ESPP perquisites taxed in India (for Category 2(b)) |
| 06 | AIS foreign report | AIS Foreign Assets Information PDFs |
| 07 | Valuation evidence | 31-3-2026 high/low prices, FX rate with source, note of non-published dates, retrieval timestamp |
| 08 | Sale proof | Confirmations for lots sold before 31-3-2026 |

## ZIPs
- **Income ZIP (I1 "Attach supporting documents"):** 01, 03, 04, 06.
- **Asset ZIP (A5 "Attach valuation report", mandatory):** 01, 02, 03, 05, 07, 08.
- Every Category 2 row must have acquisition, sale (if any) and valuation proof **inside the asset ZIP**.

## PDF handling (pymupdf)
- Merge, decrypt (Form 16/12BA passwords are commonly the PAN in uppercase; AIS uses lowercase PAN + DOB DDMMYYYY), and compress with `scripts/compress_pdf.py`.
- Before upload, audit both ZIPs: they open, nothing is encrypted, text is present, and every row is covered.
- Redact nothing the department needs, but don't add unrelated personal documents.

## Windows tips
- Write scripts to files rather than piping them through PowerShell here-strings: characters like ₹ × ÷ – become "?", and `$1` inside double-quoted PowerShell strings gets expanded.
- Set `PYTHONUTF8=1` / `PYTHONIOENCODING=utf-8` when scripts print ₹.
