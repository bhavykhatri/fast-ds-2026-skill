# After Form 1: Form 2, payment, Form 3, Form 4

## Form 2 — order of amount payable
- Issued within 1 month from the end of the month Form 1 was filed (often on the last day of that following month). It's a system-generated order, not a form you file, so it doesn't appear under "View Filed Forms" or e-Proceedings — download and keep the PDF when it arrives. The portal pre-fills its details in Form 3.
- Check: Part B lists each income and asset row; row 3 = 60% of Category 1; row 5 = ₹1 lakh or nil; **row 6 = total payable**.
- Apparent errors: raise a grievance on the portal (FAQ Q91). **The payment clock keeps running.**
- No further Form 1 after Form 2 (FAQ Q84).

## Deadlines
Run `python scripts/fastds_payable.py --form2-date YYYY-MM-DD --payable <row 6>`.
- **Initial due date** = last day of the 2nd month after the month Form 2 was received. Pay by then → no interest.
- Then up to 2 more months: interest 1% simple per month or part on the outstanding amount.
- After that → the declaration is void (deemed never made).
- Part payments are allowed; each is tracked in Form 3.

Example: Form 2 received 31-Oct → no interest until 31-Dec; with 1% until 31-Jan; with 2% until 28/29-Feb; then void.

## Payment — challan ITNS 289
1. e-File → **e-Pay Tax** → select **Income-tax Act, 1961** (not 2025) → Continue → **+ New Payment**.
2. Tile **"Foreign Assets of Small Taxpayers Disclosure Scheme, 2026 (Challan No. ITNS 289)"** → Proceed. (Pre-login: Home → e-Pay Tax → PAN + mobile OTP.)
3. AY **2026-27** pre-filled; minor head **116** for non-corporate PANs (115 for companies). Verify before paying — **wrong head = no correction, no refund**.
4. Enter the breakup:
   - **(a) Tax (s.133 Table Sl. No. 1)** = Form 2 row 3 (the 60% amount)
   - **(b) Fee (s.133 Table Sl. No. 2)** = Form 2 row 5 (₹1,00,000 or 0)
   - **(c) Interest (s.135(3))** = 0 if paid by the initial due date
   - Total must equal Form 2 row 6 (+ interest).
5. Choose a mode: net banking, debit card, payment gateway (UPI/credit card), NEFT/RTGS mandate, or bank counter. No beneficiary setup is needed for UPI/net banking. UPI for tax is allowed up to ₹5 lakh, but many banks cap at ₹1 lakh — use net banking/debit card for larger amounts rather than splitting.
6. Download the receipt: **e-Pay Tax → Payment History → ⋮ → Download**. Note the **BSR code, challan serial number ("Challan No"), date of deposit and amount**. If the bank debited but no receipt shows, check Payment History/Generated Challans before trying again — never pay twice.

## Form 3 — intimation of payment
- Path: e-File → Income Tax Forms → File Income Tax Forms → **Forms as per other Acts** → FADS 2026 **Form 3** → File Now → Online / Original → Continue → Let's Get Started.
- **Only once per PAN; no revision or withdrawal.** File only after full and final payment.
- **Part A:** pre-filled.
- **Part B:** pre-filled from Form 2 — 2(i) date of receipt, 2(ii) amount payable, 2(iii) initial due date, 2(iv) paid by that date, 2(v) outstanding; row 3 months of delay and interest.
- **Part C:** challans (BSR, date, serial, amount) appear automatically once the payment syncs. Totals must match 2(ii) + interest, or the portal blocks submission.
- Opening Form 3 **before paying** shows "Outstanding Amount Mismatch … Kindly pay the balance amount" — expected; close it without submitting, pay, then return.
- The challan can take from ~30 minutes to a couple of working days to appear. Don't pay again; if it's missing after 2 working days, contact the e-Filing helpdesk (1800 103 0025 / 1800 419 0025) with PAN, challan details and the Form 1 acknowledgement number.
- Declaration: enter place → Preview → Proceed to e-Verify (user).

## Form 4 — certificate
- Issued within 1 month from the end of the month Form 3 is filed (in practice it can arrive within minutes). Found under View Filed Forms → Forms as per other Acts, with Forms 1–3 annexed.
- It certifies the amount paid, that Form 1 is valid, and grants immunity under the BMA for what was declared.
- "Signature Not Verified" in a PDF reader just means the department's certificate isn't installed locally.
- **Archive permanently:** Forms 1–4, acknowledgement, challans, the computation statement, ZIPs and workbook.

## Going forward (every ITR from now)
- **Schedule FA** for every foreign account and holding (calendar-year basis; SBI TT buying rate for peak/closing values; ITR-2/ITR-3, not ITR-1/4).
- Foreign dividends in Schedule OS, foreign share gains in Schedule CG (foreign shares are long-term only after 24 months), FSI and TR schedules.
- **Form 67 before the ITR** to claim credit for foreign tax withheld.
- Set "foreign assets/income" = Yes in Part B-TTI.
