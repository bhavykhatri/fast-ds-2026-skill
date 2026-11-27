# FAST-DS 2026 filing skill for AI agents

An [Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) that walks an Indian taxpayer through **FAST-DS 2026** — the *Foreign Assets of Small Taxpayers Disclosure Scheme* ("FADS 2026" on the e-Filing portal) — from eligibility to the final Form 4 certificate.

It's aimed at salaried people with RSUs/ESPP in a US brokerage, foreign dividends, or a foreign bank account that never made it into Schedule FA, but it covers the whole scheme.

> **Deadline: Form 1 must be filed by 31 December 2026.**

> ⚠️ **Not legal or tax advice.** This is a structured checklist built from the official texts, CBDT FAQs (Q1–93, including the Supplementary FAQs of 20-Nov-2026) and hands-on use of the portal. Rules and portal screens change. Check the official sources and consult a Chartered Accountant for judgement calls. Nothing paid under the scheme is refundable.

## What's inside
```
.claude-plugin/                # Claude Code plugin + marketplace manifests
skills/fast-ds-2026/
  SKILL.md                     # the workflow the agent follows (7 phases)
  references/
    knowledge-base.md          # law, categories, Rule 3 valuation, timelines, immunity, exclusions
    faqs.md                    # CBDT FAQs Q1-50 + Supplementary FAQs Q51-93, summarised with links
    computation.md             # FX rules, capital gains, ESPP/RSU cost, workbook design, reconciliation
    evidence-pack.md           # what to upload, ZIP layout, PDF handling
    portal-form1.md            # Form 1 on the portal, field by field (with automation selectors)
    after-filing.md            # Form 2, ITNS 289 payment, Form 3, Form 4, future ITRs
  examples/
    sample-computation-statement.md  # fully worked FICTIONAL statement to copy the format from
    sample_*.csv               # inputs that reproduce the sample's numbers with the scripts
  scripts/
    fastds_payable.py          # amount payable + payment deadlines and interest
    sbi_tt_rate.py             # Rule 115 SBI TT buying rate lookup
    quoted_share_fmv.py        # Rule 3 value of quoted shares on 31-3-2026
    compress_pdf.py            # merge/decrypt/compress PDFs under 5 MB
agents/
  fast-ds-reviewer.md          # optional Claude Code subagent: blind recomputation + compliance review
```

## The scheme in one table
| | Category 1 | Category 2 |
|---|---|---|
| For | Undisclosed foreign income, or foreign assets with an unexplained source | Foreign assets bought from taxed income (e.g. RSU/ESPP) or while non-resident, missing from Schedule FA |
| Cost | 60% of value (30% tax + equal amount) | ₹1,00,000 flat for all such assets |
| Cap | ≤ ₹1 crore | ≤ ₹5 crore |

Form 1 (by 31-Dec-2026) → Form 2 (amount payable) → pay via challan ITNS 289 → Form 3 (intimation of payment) → Form 4 (certificate and Black Money Act immunity).

## Install

**Claude Code (plugin — easiest)**
```
/plugin marketplace add bhavykhatri/fast-ds-2026-skill
/plugin install fast-ds-2026@fast-ds-2026
```

**Claude Code (manual copy)**
```bash
git clone https://github.com/bhavykhatri/fast-ds-2026-skill.git
mkdir -p ~/.claude/skills ~/.claude/agents
cp -r fast-ds-2026-skill/skills/fast-ds-2026 ~/.claude/skills/
cp fast-ds-2026-skill/agents/fast-ds-reviewer.md ~/.claude/agents/   # optional
```
Then ask: *"Help me file FAST-DS for my unreported RSUs"*.

**Claude apps (claude.ai / desktop)** — zip the `skills/fast-ds-2026` folder and upload it under **Settings → Capabilities → Skills**.

**Other agents** — point the agent at `skills/fast-ds-2026/SKILL.md`; it's plain Markdown.

## Using the scripts
```bash
# Amount payable and deadlines
python skills/fast-ds-2026/scripts/fastds_payable.py --cat1 250000 --cat2 yes --form2-date 2026-11-30

# Rule 115 rates for income dates
python skills/fast-ds-2026/scripts/sbi_tt_rate.py 2024-06-13 2025-03-13

# Quoted-share value on 31-3-2026 (groups.csv: label,quantity,cost_inr)
python skills/fast-ds-2026/scripts/quoted_share_fmv.py --ticker AAPL --groups groups.csv
```

## Safety rules the skill follows
- It never e-verifies, submits or pays for you — it fills drafts and stops at Preview.
- It flags irreversible steps: one Form 1 after Form 2 is issued, one Form 3, no refunds, wrong minor head can't be fixed.
- It keeps your PAN, account numbers and passwords out of anything it shares.

## Official sources
- Finance Act 2026, Chapter IV (ss.130–144)
- [FAST-DS Rules 2026 — Notification 114/2026](https://incometaxindia.gov.in/documents/d/guest/notification-no-114-2026-pdf)
- [CBDT FAQs Q1–50](https://www.incometaxindia.gov.in/documents/81799/15520974/FAST-DS-FAQs.pdf)
- [CBDT Supplementary FAQs Q51–93 (20-Nov-2026)](https://www.incometaxindia.gov.in/documents/d/guest/supplementary-faqs-fast-ds-pdf)
- [Form 1 user manual](https://www.incometax.gov.in/iec/foportal/newdownloads/form%201%20of%20fads-um) · [Form 3 user manual](https://www.incometax.gov.in/iec/foportal/newdownloads/form3-um) · [ITNS 289 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/foreign-assets-small-taxpayers-disclosure-scheme-2026)

## Contributing
Corrections are welcome — especially portal changes and new CBDT clarifications. Please cite the official source in your PR, and never include anyone's personal or financial details.

## License
MIT — see [LICENSE](LICENSE).
