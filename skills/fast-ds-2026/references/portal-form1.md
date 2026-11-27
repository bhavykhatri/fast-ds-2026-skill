# Filing Form 1 on the e-Filing portal

Observed on the portal in Oct 2026. The portal changes; re-check labels as you go. **The user logs in and e-verifies; you never do.**

## Setup
- The user logs in at https://www.incometax.gov.in in the browser you're driving. The portal allows **one session at a time** — close other sessions.
- Drafts are saved per section. If the session expires: File Now → Continue → Let's Get Started shows the saved sections.

## Path
e-File → Income Tax Forms → File Income Tax Forms → tab **"Forms as per other Acts"** → **"Foreign Assets of Small Taxpayers Disclosure Scheme 2026 (Form 1 of FADS 2026)"** → File Now → Mode Online, Filing Type Original → Continue → Let's Get Started.

Refiling replaces the earlier Form 1 only until Form 2 is issued (FAQ Q84–86). Treat it as one shot.

## Sections
Sections are buttons, e.g. `getByRole('button', {name: /^Part- B/})`.

### Part A — Basic information
Pre-filled name, address, PAN. Passport is optional (needed only if claiming non-resident status for some year). Save.

### Part B — Type of declaration
Four checkboxes (`#assetOrIncomeCheckbx{1..4}PartB-input`; check with force if hidden):
1. Undisclosed asset located outside India → Cat 1(a)
2. Undisclosed foreign income → Cat 1(b)
3. Asset acquired while non-resident (or RNOR), not declared → Cat 2(a)
4. Asset acquired from income offered to tax, not declared in the Schedule → Cat 2(b)

Save → a warning ("deselecting deletes annexure data") → OK.

### Annexures (one per ticked type)
Categories: A1 bank account, A2 immovable property, A3 jewellery/bullion, A4 art, A5 shares and securities, A6 other, I1 any income (I1 only for types 1–2). Each has a Yes/No radio (in that order; select by index), then **+ Add Details** per row. "Aggregate value as per Rule 3" adds up automatically.

**I1 (income) row:**
- `#annex2IncomeRelPrevYr` — previous year (mat-select, e.g. "2023-24")
- `#annex2IncomeEquResStatus` — residential status
- `#annex2IncomeType` — text, e.g. "Dividend - <issuer> (<broker>)"; keep one row per year × type
- `#annex2IncomeCountry` — e.g. "United States Of America"
- `#annex2IncomeErnAmt` — INR amount
- then **Add**.

**A5(a) quoted shares row:**
- `#annex4QtedIssuerName`, `#annex4QtedShareNum`, `#annex4QtedShareType`, `#annex4QtedShareEstimt` (exchange), `#annex4QtedCountry`, `#annex4QtedHeldName`, `#annex4QtedAquisCost`, `#annex4QtedAquisDate`, `#annex4QtedRelPrevYr`, `#annex4QtedResStatus`, `#annex4QtedDeterVal`, `#annex4QtedValueDate`, `#annex4QtedFairMarkVal`.
- The portal computes "Asset value as per Rule 3 = highest of cost and the market values".
- **Number of shares:** FAQ Q73 says A5 accepts decimal quantities, but in Oct 2026 the field validated integers only (`[0-9]{1,14}`). If decimals are rejected, round to the nearest whole number and put the exact fractional quantity in the description/type field.
- One row per acquisition-year group (FAQ Q93: an asset held over years is reported once, in the earliest year of acquisition). For sold lots (Rule 3(2)), valuation date = sale date.

**A1 bank account row:** bank name and address, country, holders, account number, opening date, **sum of all deposits**, FMV.

### Quirks
- **Hidden duplicate fields** exist — always target `#id:visible`.
- **Dates:** typing and pasting are blocked. Use the calendar: click the input → `.mat-calendar-period-button` → year (page back with `.mat-calendar-previous-button`) → month (e.g. "DEC") → day. Max date 31-Mar-2026. For multi-date groups use 31-Dec of the acquisition year and write "various dates" in the description.
- **Text validation** rejects `> < &` ("Invalid Address Line"). Avoid them.
- **Attachments:** "Attach supporting documents" under I1 and "Attach Valuation report *" (mandatory) under A5. Agent file upload may be blocked — let the user attach. Delete an old attachment (`.attachBox img[alt="delete attachment"]`) before re-uploading.

### Parts C and D (read-only)
`aggreValField4iiPartC`, `aggreVal4vPartC`, `aggrAmtField5PartD`, `totalFeeField6PartD`, `aggreAmtField7PartD`. Check every figure against the workbook: 4(iii) ≤ ₹1 crore, 4(vi) ≤ ₹5 crore, item 5 = 60% of 4(iii), item 6 = ₹1 lakh or nil, item 7 = total payable. Save.

### Verification
Enter the place (`#varUserInputPlace`) → Save → **Preview**. The verification certifies that s.140 exclusions don't apply.

Preview offers Edit / Download / Proceed To E-Verify. Downloads may be blocked in automation — take a full-page screenshot as a record and let the user download. Re-read the preview (totals, attachments, Part B ticks) and then hand over to the user to e-verify (Aadhaar OTP, EVC or DSC).

After filing: **e-File → Income Tax Forms → View Filed Forms → Forms as per other Acts** shows the acknowledgement, the filed form and attachments.
