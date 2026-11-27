# FAST-DS 2026 — Knowledge base

**Foreign Assets of Small Taxpayers – Disclosure Scheme, 2026** (the e-Filing portal calls it "FADS 2026").
Reference material, not legal advice. Last reviewed against official sources on 27-Nov-2026. Check the official pages below for anything newer.

## 0. Official sources
| # | Source | Covers |
|---|---|---|
| S1 | Finance Act 2026 (Act 4 of 2026), Chapter IV, ss.130–144 | The law |
| S2 | Notification 114/2026 (G.S.R. 732(E), 14-Aug-2026) — FAST-DS Rules 2026: https://incometaxindia.gov.in/documents/d/guest/notification-no-114-2026-pdf | Rules 1–9, valuation (Rule 3), Forms 1–4 |
| S3 | CBDT FAST-DS FAQs Q1–50: https://www.incometaxindia.gov.in/documents/81799/15520974/FAST-DS-FAQs.pdf | Official clarifications |
| S4 | **CBDT Supplementary FAQs Q51–93 (20-Nov-2026)**: https://www.incometaxindia.gov.in/documents/d/guest/supplementary-faqs-fast-ds-pdf | Joint holders, FX rate, refiling, FTC, indexation, multi-year assets |
| S5 | Form 1 user manual: https://www.incometax.gov.in/iec/foportal/newdownloads/form%201%20of%20fads-um | Portal filing |
| S6 | ITNS 289 user manual and FAQs: https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/foreign-assets-small-taxpayers-disclosure-scheme-2026 | Payment |
| S7 | Form 3 user manual: https://www.incometax.gov.in/iec/foportal/newdownloads/form3-um | Intimation of payment |
| S8 | Foreign Assets Information (FAI) user guide (Jul 2026), Compliance portal | Viewing CRS/FATCA data the department holds |

Summaries of S3 and S4 are in `faqs.md`.

## 1. What it is
- A **one-time voluntary disclosure window** to regularise foreign income or foreign assets left out of Indian returns, for a fixed tax or fee, with immunity under the Black Money Act (BMA).
- **Form 1 window:** 16-Aug-2026 to **31-Dec-2026**. Nothing can be filed after that.
- **Valuation date:** 31-Mar-2026.
- **Authority:** Pr. DGIT / DGIT (Systems). Fully online and faceless (FAQ Q5, Q74).
- **Who:** any "person" — individuals, HUFs, firms, companies, LLPs, AOPs, trusts — and a legal heir for a deceased person (FAQ Q90).

## 2. Eligibility [s.131(1)(a); FAQ Q6–11, Q62–63]
- Resident (s.6) in the relevant previous year; **or**
- Non-resident/RNOR in that year but resident in the year the income relates to, or the year the asset was acquired.
- Assets bought while RNOR and not reported after becoming ROR → Category 2(a), selecting the RNOR option in Form 1 Part B (FAQ Q63).

**Grounds [s.132]:** (a) no return filed; (b) a return filed **before commencement (16-Aug-2026)** that omitted the asset or income; (c) escaped assessment (s.147).
**Years:** any previous year up to FY 2025-26.

## 3. The two categories [s.133 Table; FAQ Q12–20, Q51–54, Q66–71, Q82–83]
| | **Category 1 (Table Sl. 1)** | **Category 2 (Table Sl. 2)** |
|---|---|---|
| Covers | (a) undisclosed asset outside India (source unexplained), and/or (b) undisclosed foreign income (chargeable in India, never offered) | Asset outside India with an explained source, not shown in Schedule FA: (a) bought while non-resident from foreign income; (b) bought from income already taxed in India |
| Cap (eligibility) | Aggregate assets (FMV on 31-3-2026) + income ≤ ₹1 crore | Aggregate FMV ≤ ₹5 crore |
| Payable | 30% tax + equal additional amount = **60%** | **₹1,00,000 flat**, once, for all assets and all years |
| Outside the scheme (BMA) | 30% tax + 90% penalty = 120%, plus prosecution risk | ₹10 lakh penalty per asset per year (s.42/43) |

- Caps are per declarant (FAQ Q59). Over the cap → that category isn't available at all (FAQ Q20).
- Declare only what wasn't offered to tax / wasn't in Schedule FA (FAQ Q51–52). Immunity covers only what you declare (FAQ Q53–54).
- Mixed-source assets (any undisclosed money in them) can't use Category 2; use Category 1 if eligible (FAQ Q70).
- An asset in Category 1 isn't repeated in Category 2 (FAQ Q69). Both categories fit in one Form 1 (FAQ Q71).
- Gifted/inherited assets: the donee's cost = the donor's cost; if funded from disclosed money, Category 2 (FAQ Q80).
- An overseas loan receivable is a foreign financial asset that can be declared (FAQ Q81).
- Directors, employees and signatories who must report a company account under BMA s.42/43 can use Category 2 (FAQ Q60–61).
- **No DTAA relief or foreign tax credit** against the Category 1 amount (FAQ Q87). Where significant foreign tax was withheld, compare with ITR-U/revised return (see §10).

## 4. Valuation (Rule 3) [FAQ Q21–36, Q55, Q58, Q73, Q76–80, Q92–93]
General rule: FMV = **higher of cost of acquisition and market value on 31-3-2026** (backed by a valuer recognised in that country where relevant). If no valuation is carried out, **indexed cost** is the FMV — and then it's final; it can't be replaced later and the 20% tolerance doesn't apply (FAQ Q79).

| Asset | FMV |
|---|---|
| **Quoted shares/securities** | Higher of cost and the **average of the day's lowest and highest price on 31-3-2026** on an established exchange; if not traded that day, the nearest earlier trading day. Fractional quantities: exact fraction × that average (FAQ Q73). No valuer report needed. |
| Unquoted equity | Higher of cost and the book-value formula in the Rules |
| Unquoted other securities, immovable property, bullion, jewellery, art | Higher of cost and open-market value per a recognised valuer; else indexed cost |
| **Bank account** | **Sum of all deposits since opening** up to 31-3-2026 — not the balance. Exclude re-deposits of earlier withdrawals. If declared earlier under BMA Chapter VI, count only later deposits (FAQ Q29–31). |
| Interest in a firm/AOP/LLP | Net assets split by capital contributed, residue by agreement or profit ratio |
| Any other asset | Higher of cost and arm's-length open-market price; else indexed cost |
| Asset **sold before 31-3-2026** | Higher of cost and sale price (FMV on transfer if sold for inadequate consideration) [Rule 3(2)] |
| Jointly held | Split by definite shares, or equally if none; contributions are ignored (FAQ Q58) |
| Acquired before 1-4-2001 | Base cost = higher of actual cost and FMV on 1-4-2001, in foreign currency; index from CII 100 to CII 380 (FY 2025-26) (FAQ Q92) |

- **Indexation example (FAQ Q79–80):** cost × 380 / CII of the acquisition year, in foreign currency, then convert.
- **Reinvestment [Rule 3(3); FAQ Q34, Q72]:** if an old asset/account funded a new asset, reduce the old one's value by the amount reinvested. If undisclosed income funded an asset, reduce the income by the amount invested. No double counting.
- **Currency [Rule 3(4)–(5); FAQ Q35, Q55]:** RBI reference rate on 31-3-2026 for RBI-designated currencies. None was published on 31-3-2026, so **USD converts at ₹94.6543 (30-3-2026)**. Non-designated currencies → USD at the local central bank rate → INR.
- **20% tolerance [Rule 5(2); FAQ Q36, Q76–78]:** for assets valued on a valuer's report (not bank accounts, not indexed cost), the AO's higher value within +20% doesn't void the declaration.
- **Multi-year assets:** report once, in the earliest relevant previous year of acquisition, at FMV on 31-3-2026 (FAQ Q93).

### Income conversion (judgement call — explain to the user)
s.131(1)(k) defines undisclosed foreign income as income "chargeable to tax in India but not offered", so it's computed under the IT Act, i.e. **Rule 115: SBI TT buying rate on the last day of the month before the income**. Rule 3(4)'s RBI rate on the valuation date applies to the "value of the asset" (s.131(1)(l)), and FAQ Q35 sits under "Valuation of Assets". The statutory reading favours Rule 115 for income. Converting all income at the 31-3-2026 rate is a more conservative alternative that usually costs more, and nothing is refundable. The 20% tolerance doesn't cover income, so it must be exact. Record the choice.

## 5. Process and timeline [s.135; Rules 5–8; FAQ Q40–46, Q84–86, Q89, Q91]
| Step | By | Deadline |
|---|---|---|
| **Form 1** declaration | Taxpayer | 16-Aug → 31-Dec-2026; e-verify. Refiling replaces the earlier one **only until Form 2 is issued**; after that, no further Form 1 at all. A rejected Form 1 can be filed afresh. |
| **Form 2** order of amount payable | Department | Within 1 month from the end of the month Form 1 was filed |
| **Payment** (ITNS 289) | Taxpayer | Within **2 months from the end of the month Form 2 is received**; then up to 2 more months at **1% simple interest per month or part**; after that the declaration is void. Part payments allowed. A grievance against Form 2 doesn't extend this. |
| **Form 3** intimation of payment | Taxpayer | Within the payment period; once only |
| **Form 4** certificate of validity and immunity | Department | Within 1 month from the end of the month Form 3 is filed |

Rule 7 illustration: Form 2 dated 22-Sep → pay by 30-Nov without interest; by 31-Dec at +1%; by 31-Jan at +2%; after 31-Jan, void. FAQ Q89: Form 1 on 31-Dec-2026 → Form 2 by 31-Jan-2027 → payment with interest possible up to 31-May-2027.

## 6. Effect and immunity [ss.136–139; FAQ Q47–49, Q74–75, Q89]
- Immunity from further **tax, penalty and prosecution under the BMA** for what is declared.
- Declared income/investment is **not included in total income** under the IT Act or BMA.
- No rectification, revision, set-off or relief on assessments already made; **nothing paid is refundable**.
- Pending assessments: the AO must take the declaration into account. Tell the AO and pay early (FAQ Q89).
- Declarations are confidential (s.138 of the IT Act applies) (FAQ Q75). Scrutiny selection is separate and risk-based (FAQ Q74).
- **Void** if any material particular is false or a condition is breached, at any stage (s.134(3)); undervaluation beyond the tolerance goes to s.141.
- The express immunity is under the BMA. IT Act consequences are handled by the "not included in total income" rule; get professional advice if an IT Act notice is already pending.

## 7. Where the scheme doesn't apply [s.140; FAQ Q50, Q64–65, Q88]
- Proceeds of crime with PMLA proceedings started or pending.
- An AY with a **completed** BMA assessment (even if under appeal), or assets already penalised under BMA s.42/43.
- Searches, surveys and pending notices **don't** exclude.

## 8. Payment details [S6]
- e-File → e-Pay Tax → **Income-tax Act, 1961** → New Payment → tile **"Foreign Assets of Small Taxpayers Disclosure Scheme, 2026 (ITNS 289)"**.
- AY 2026-27 pre-filled and locked. Major head 0021 + minor head **116** for non-corporate PANs; 0020 + **115** for companies.
- The challan has three fields: **(a) Tax** (s.133 Table Sl. 1), **(b) Fee** (Table Sl. 2), **(c) Interest** (s.135(3)). One challan for the whole amount.
- Modes: net banking, debit card, payment gateway (UPI/credit card), NEFT/RTGS mandate, bank counter. UPI for tax is allowed up to ₹5 lakh but many banks cap lower.
- Wrong minor head = no correction, no refund.

## 9. Foreign Assets Information (FAI) in AIS [S8]
- CRS/FATCA data received from other countries. **AIS → Compliance portal → Reports → Foreign Assets Information** → calendar year (CY2022+) → download PDF.
- PDF password: PAN in lowercase + date of birth as DDMMYYYY.
- Fields: reporting institution, account, currency, dividends, interest, gross proceeds, other payments, balance.
- Feedback per transaction is possible after download. It won't be complete — declare from your own records.

## 10. Related routes and rules
- **BMA ₹20 lakh carve-out** (from 1-10-2024; prosecution side extended in 2026): no s.42/43 penalty or prosecution in a year where aggregate non-immovable foreign assets are ≤ ₹20 lakh. For bank accounts ≤ ₹20 lakh funded from disclosed sources, no FAST-DS declaration is needed (FAQ Q67). Schedule FA is still mandatory under the IT Act.
- **ITR-U (s.139(8A)):** up to 48 months after the AY; additional tax of 25/50/60/70% of tax+interest; foreign tax credit possible (file Form 67 first); **no BMA immunity**. Often cheaper for income where foreign tax was withheld. A common combination: ITR-U for missed income + FAST-DS Category 2 for the asset.
- **Revised return** for FY 2025-26 (AY 2026-27) up to 31-3-2027 adding Schedule FA counts as BMA compliance for a returning NR's post-tax account (FAQ Q68).
- **Schedule FA** in future ITRs: calendar-year basis (1 Jan–31 Dec); SBI TT buying rate for peak/closing values; ITR-1/ITR-4 can't be used with foreign assets.

## 11. Decision checklist before declaring
1. Classify: undisclosed (Cat 1) or only not reported (Cat 2)? Any mixed funding?
2. Value under Rule 3 and convert correctly (assets at ₹94.6543/USD; income at Rule 115 rates).
3. Test the caps (₹1 cr / ₹5 cr), per declarant.
4. Check the ₹20 lakh carve-out year by year, and whether a revised return/ITR-U route is better for some items.
5. Check exclusions (s.140).
6. Compare costs: 60% vs BMA 120% + interest; ₹1 lakh vs ₹10 lakh per asset per year; FAST-DS vs ITR-U with foreign tax credit.
7. Reconcile with AIS Foreign Assets Information, then file once, well before 31-Dec-2026.
