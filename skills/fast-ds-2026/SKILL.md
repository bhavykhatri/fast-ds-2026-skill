---
name: fast-ds-2026
description: Guide an Indian taxpayer end to end through FAST-DS 2026 (Foreign Assets of Small Taxpayers Disclosure Scheme, "FADS 2026" on the e-Filing portal) — eligibility, Category 1 vs 2 classification, Rule 3 valuation, Form 1 filing, ITNS 289 payment, Form 3 and Form 4. Use when someone has unreported foreign assets or income (RSU/ESPP, US brokerage, foreign bank account, foreign dividends) and asks about FAST-DS, FADS, Form 1/2/3/4, or regularising Schedule FA omissions before 31-Dec-2026.
---

# FAST-DS 2026 — end-to-end filing skill

A one-time Indian disclosure scheme (Finance Act 2026, Chapter IV, ss.130–144; FAST-DS Rules 2026, Notification 114/2026). Form 1 window: **16-Aug-2026 → 31-Dec-2026**. Valuation date: **31-Mar-2026**.

**Read first, every time:**
- `references/knowledge-base.md` — the law, categories, valuation, timelines, immunity, exclusions.
- `references/faqs.md` — CBDT FAQs Q1–50 and the **Supplementary FAQs Q51–93 (20-Nov-2026)**, summarised with links. Quote these; don't rely on memory. Check the official pages for anything newer than this skill.

Other references, load when you reach that phase:
- `references/computation.md` — FX rules, capital gains, ESPP/RSU cost, workbook design, reconciliation.
- `references/evidence-pack.md` — what to upload, ZIP structure, PDF handling.
- `references/portal-form1.md` — Form 1 on the e-Filing portal, field by field, with automation selectors.
- `references/after-filing.md` — Form 2, ITNS 289 payment, Form 3, Form 4, and future ITRs.
- `examples/sample-computation-statement.md` — a fully worked **fictional** computation statement (income + RSU shares) to copy the structure from; `examples/*.csv` reproduce its numbers with the scripts.

Scripts (Python 3, stdlib + optional `requests`, `pymupdf`):
- `scripts/fastds_payable.py` — amount payable and the full payment timeline (due dates, interest, void date) from a Form 2 date.
- `scripts/sbi_tt_rate.py` — Rule 115 SBI TT buying rate lookup (last day of the preceding month) from the public SBI reference-rate CSV.
- `scripts/quoted_share_fmv.py` — Rule 3(1)(c) value of quoted shares: higher of cost and the average of the day's high and low on 31-3-2026.
- `scripts/compress_pdf.py` — merge, decrypt and compress PDFs under the portal's 5 MB limit.

## Hard rules
1. **You are not a CA or lawyer.** Say so once, at the start. Recommend a professional where the case has judgement calls (mixed-source assets, pending proceedings, non-resident years, amounts near the caps).
2. **Never e-verify, submit, or pay on the user's behalf.** Fill drafts, stop at Preview, and hand off. The user e-verifies and pays.
3. **Nothing paid is refundable** (s.138), and **a payment under the wrong minor head can't be corrected**. Double-check before every payment.
4. **A false material particular voids the declaration at any stage** (s.134(3)). Declare from complete records, not from memory or the AIS alone.
5. **One Form 1 per person.** It can be refiled before Form 2 is issued (the latest one counts), but **after Form 2 no further Form 1 is possible**, even for omissions (FAQ Q84–86). File once, after the full review.
6. **Form 3 can be filed only once** and only after the full payment shows on the portal.
7. Keep personal data (PAN, account numbers, DOB, passwords) out of anything you publish, log or share. Delete temporary extracts when done.

## Workflow
Create a task list with these phases and tick them off.

### Phase 1 — Facts and eligibility
1. Residential status for every relevant year (s.131(1)(a)). Non-residents/RNORs qualify only through a resident year of income or acquisition (FAQ Q6–8, Q62–63).
2. Ground for declaring (s.132): no return; a return filed **before 16-Aug-2026** that left the asset or income out; or escaped assessment.
3. Exclusions (s.140, FAQ Q50, Q64–65, Q88): PMLA proceeds of crime; an AY with a **completed** Black Money Act (BMA) assessment or concluded BMA penalty. Pending proceedings, searches and surveys don't exclude. Ask the user to confirm; Form 1's verification certifies it.
4. Inventory every foreign asset and income source, year by year: what each ITR reported (Schedule FA, OS dividends, CG, FSI); how each asset was funded (salary already taxed such as RSU/ESPP perquisites in Form 12BA; income earned as a non-resident; gifts/inheritance; or unexplained). Ask explicitly about other bank, broker, crypto, insurance, loans receivable (FAQ Q81) and jointly held assets (FAQ Q56–59).
5. Pull **AIS → Compliance portal → Reports → Foreign Assets Information** (CY2022 onwards) and reconcile it, but declare from the user's own complete records.
6. Decide whether FAST-DS is needed at all: assets already in Schedule FA and income already offered need nothing (FAQ Q51–52). A small account (≤ ₹20 lakh at all times) funded from taxed money may not need a declaration (FAQ Q67). A former NR may be better served by a revised/updated return (FAQ Q68). Compare with ITR-U for income-only cases. See `knowledge-base.md` §10.

### Phase 2 — Classification (s.133)
| Situation | Category | Cost |
|---|---|---|
| Foreign income chargeable in India but never offered (dividends, interest, capital gains) | 1(b) undisclosed foreign income | 60% (30% tax + equal amount) |
| Asset with an unexplained source, or funded wholly/partly from undisclosed income | 1(a) undisclosed asset | 60% of FMV on 31-3-2026 |
| Asset bought from income already taxed in India, missing from Schedule FA (e.g. RSU/ESPP) | 2(b) | ₹1 lakh flat for all such assets |
| Asset bought while non-resident (or RNOR), not reported after becoming resident | 2(a) | ₹1 lakh flat |

- Caps are **eligibility** limits, per declarant: Cat 1 total ≤ ₹1 crore; Cat 2 total ≤ ₹5 crore. Over a cap = that category is unavailable.
- **Never put an asset funded from taxed salary (RSU/ESPP) in Category 1.** But an asset with *any* undisclosed money in it can't use Category 2 (FAQ Q70).
- Both categories can go in one Form 1 (FAQ Q71). An asset in Cat 1 isn't repeated in Cat 2 (FAQ Q69).
- **Category 2 scope = assets omitted from returns filed before commencement.** Exclude lots first reportable in a Schedule FA already filed, or whose return isn't due yet.
- **Tracing (Rule 3(3), FAQ Q72):** if undisclosed income was reinvested, the asset bought is Cat 1(a) and the income is reduced by the same amount. Check whether dividends were reinvested or swept to a money-market fund.
- Show the user the BMA comparison (FAQ Q66) and the ₹20 lakh carve-out year by year so they understand what the scheme removes.

### Phase 3 — Computation
Follow `references/computation.md`. Key points:
- **Income** is computed under the IT Act (s.131(1)(k)): each item at the **Rule 115 SBI TT buying rate on the last day of the preceding month**, gross, with **no foreign tax credit** (FAQ Q87). Split rows by previous year and income type.
- **Assets** (Rule 3): quoted shares = higher of cost and average of the day's high/low on 31-3-2026, applied per acquisition-year group; fractional quantities are allowed (FAQ Q73). Sold before 31-3-2026 = higher of cost and sale price, lot by lot (Rule 3(2)). Bank account = sum of all deposits since opening, excluding re-deposits (FAQ Q29–30). Others: see knowledge base.
- **FX for assets:** RBI/FBIL reference rate on 31-3-2026. None was published that day, so use **₹94.6543 per USD (30-3-2026)** — confirmed by FAQ Q55.
- **An asset held over several years is reported once**, in the earliest relevant previous year of acquisition, at FMV on 31-3-2026 (FAQ Q93). Separate lots acquired in different years can be grouped by acquisition year.
- Payable = round(60% × Cat 1 total) + (₹1,00,000 if any Cat 2 asset). Use `scripts/fastds_payable.py`.
- Build a workbook with live formulas (sheet list in `computation.md`) and reconcile every calendar year to three independent sources.

### Phase 4 — Review (always, before filing)
1. Line-by-line pass against the source documents.
2. **Blind recomputation** by an independent agent working only from the PDFs (use `agents/fast-ds-reviewer.md` in Claude Code, or a fresh session elsewhere). Diff line by line and resolve every difference.
3. Rules-compliance checklist: eligibility and s.140; Category 2 scope; income vs asset FX basis; Rule 3(3) tracing; Rule 3(2) sold lots; income-type labels; Form 1 per-item fields; caps; single-filing and immunity scope.
4. Record the user's decisions (basis chosen, estimates accepted, confirmations) in a review log.

### Phase 5 — Evidence pack
Follow `references/evidence-pack.md`: an entry guide, a formal computation statement with annexures (model it on `examples/sample-computation-statement.md`), and proof files grouped into the income ZIP and the asset ZIP, each ≤ 5 MB. Every Category 2 row needs acquisition, sale (if any) and valuation proof inside the asset ZIP.

### Phase 6 — Form 1 on the portal
Follow `references/portal-form1.md`. The user logs in themselves. Fill each part, verify Part C/D totals against the workbook, stop at Preview, re-read it, and hand off for e-verification. The user downloads the acknowledgement and filed form.

### Phase 7 — After filing
Follow `references/after-filing.md`:
1. **Form 2** arrives within a month after the end of the filing month. Check the amount against the workbook; for obvious errors raise a portal grievance, but that **doesn't extend the deadline** (FAQ Q91).
2. **Pay** through e-Pay Tax → Income-tax Act, 1961 → New Payment → FAST-DS 2026 (ITNS 289): AY 2026-27, minor head 116 (non-corporate). The challan splits **Tax / Fee / Interest** — enter Form 2's 60% amount as Tax and the ₹1 lakh as Fee. Due 2 months from the end of the month Form 2 was received; up to 2 more months at 1% per month or part; then void.
3. **Form 3** once the challan appears on the portal (minutes to a couple of working days). The portal pre-fills Part B and lists challans in Part C; totals must match before it lets you submit. Opening it before paying shows an "Outstanding Amount Mismatch" error — that's expected.
4. **Form 4** (certificate of validity and immunity) follows, often within minutes or days. Archive Forms 1–4, challans and the pack permanently.
5. From now on every ITR must carry Schedule FA, foreign income, FSI/TR and Form 67.

## Output style
- Be concrete: dates, amounts, the exact portal path, and the specific FAQ or rule number behind each statement.
- Ask before anything irreversible or expensive to redo. Present the computation for the user's sign-off before Form 1.
- When the law is unclear, say so, show both readings and the cost of each, and let the user decide (record it in the review log).
