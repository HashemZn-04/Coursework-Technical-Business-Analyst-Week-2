# Handoff Document: Legacy Trust Smart-Recovery Initiative
## Complete Week 1 Discovery Package & Stakeholder Context

**Date Prepared**: 2026-08-17  
**Project**: Smart-Recovery Initiative (Debt Collections Transformation)  
**Scope**: Week 1 Discovery findings, stakeholder analysis, automation opportunities, and preparation for change management (ADKAR)

---

## Executive Summary

Legacy Trust Bank is undertaking a digital transformation of its debt recovery operations. Currently, 50+ agents manage 100,000+ delinquent accounts using spreadsheets, email, and a 20-year-old legacy database. This creates a 15% revenue loss from missed follow-ups, duplicated effort, and inconsistent handling. 

**Week 1 completed**:
- Strategic discovery brief mapping current-state problems
- 7 prioritized automation opportunities (OPP-01 to OPP-07) ranked by ROI
- As-Is process map (BPMN) with 15+ documented pain points
- Stakeholder Jobs-to-be-Done analysis (7 top JTBD statements)
- ROI model framework (incomplete: templates exist, values to be filled)

**Next Phase**: Change management planning, starting with ADKAR assessment for 5 stakeholder groups.

**Critical Caveat**: All quantitative findings are derived from **sample data** (3,246 accounts, ~200 activity records). Assumptions for the full 100,000+ population need validation before final funding decisions.

---

## Part 1: Project Context

### The Problem (From Case Study)

**Legacy Trust Bank's Situation**:
- Grew through personal loans, credit cards, auto finance but never modernized debt recovery
- 100,000+ delinquent accounts managed by 50+ agents
- Tools: legacy 20-year-old collections database, spreadsheets, email trails, local workarounds
- Result: missed follow-ups, duplicated activity, inconsistent status updates, 15% revenue loss

**Why It Matters**:
- Operational strain: agents spend hours checking if someone else already contacted a customer, reconciling statuses, manually tracking promises
- Customer experience: repetitive contact journeys push customers to competitors
- Leadership visibility: unclear which follow-ups happened, inconsistent status codes, dependency on individual agent memory
- Scale problem: this model cannot grow with the business

### Strategic Goals (From Discovery)

The Smart-Recovery initiative aims to:
1. **Bring debt recovery into the modern era** with a single, well-understood framework
2. **Build a self-serve portal** to let customers confirm balances, choose payment options, resolve straightforward cases without agent intervention
3. **Provide evidence** to leadership on: where the current process breaks, which journeys can be automated, whether Phase 1 can ROI within 12 months

**End Goal**: Single unified portal handling all debt recovery operations  
**Phase 1 Goal (12 months)**: Deliver core automation to reduce agent workload, enable self-service for straightforward cases, improve recovery rates

---

## Part 2: Stakeholder Landscape

### Overview Table

| Group | Individual Lead | Priority Need | Success Metric | Main Fear | Trust Requires |
|---|---|---|---|---|---|
| **Operations Leadership** | Amina Rahman | Operational efficiency & visibility | Clear process map → inefficiency locations → solutions | Money/resources wasted | Root cause analysis + realistic solutions |
| **Team Leaders & Agents** | Gareth Evans | System that actually works on the ground | Clear agent boundaries, end-to-end handoff mapping | Portal works on paper, agents still have messy handoffs | Honest As-Is documentation |
| **Finance & Compliance** | Daniel Okoye | Measurable, evidence-based savings | Hard savings + revenue uplift linked to actual changes | Transformation theatre that fails when bills arrive | Transparent assumptions + sensitivity testing |
| **Product & Delivery** | Priya Nair | Fully thought-through, buildable requirements | Backlog + prototype that works in production | Missing a requirement that becomes a production problem | Pain points → opportunities → workflows → requirements (traceability) |
| **Customers** | (Not directly represented; proxy from interview notes) | Fast, non-tedious process | Convenient portal + positive reviews | More slow, repetitive contact journeys | User-tested, intuitive interface |

### Individual Stakeholder Profiles

**Amina Rahman — Head of Debt Recovery Operations**
- **Sees**: Daily strain on teams. Agents checking if someone else already called. Status reconciliation across files. Manual promise tracking.
- **Believes**: Straightforward cases should not be tangled with complex ones requiring judgment
- **Wants**: Proof of where the process breaks down + which automations save the most time + realistic future workflows agents can follow
- **Will Challenge**: Any recommendation that looks good on paper but leaves messy handoffs in reality

**Daniel Okoye — Finance & Compliance Director**
- **Sees**: 15% revenue loss from delayed actions and inconsistent follow-ups across all systems
- **Believes**: Skeptical until evidence is provided; has seen transformation fail when numbers don't materialize
- **Wants**: Which automation opportunities create measurable savings? Which improve collections? What assumptions is leadership being asked to trust?
- **Will Challenge**: Transparent assumptions + sensible sensitivity testing + separation of hard savings from hoped-for uplift

**Gareth Evans — Senior Collections Team Leader (15+ years in collections)**
- **Sees**: The cracks appearing as his team scales. Knows the current system but sees where it breaks
- **Believes**: Documentation should be honest, not aspirational
- **Wants**: As-Is process mapped honestly. Future-state workflow must show exactly where agent work begins and ends
- **Will Challenge**: Any recommendation that hides difficult cases or implies they'll disappear

**Priya Nair — Product Manager**
- **Sees**: First project in new role. Responsible for ensuring discovery becomes a buildable backlog
- **Believes**: "Well enough" is how Legacy Trust got into this situation
- **Wants**: Everything fully documented and traceable. Pain point → opportunity → workflow → requirement
- **Will Challenge**: Loose reasoning, untraceable assumptions, or lack of traceability between discovery findings and delivery requirements

**Customer Perspective** (From interview notes, not a single stakeholder)
- **Wants**: Fast resolution, transparency, control, minimal repetition
- **Fears**: More slow, tedious contact journeys; being treated inconsistently
- **Motivators**: Ability to self-serve, clear communication history, fair payment options

---

## Part 3: Current State Findings (As-Is Analysis)

### Pain Points Identified (From As-Is Process Map & Interview Analysis)

**System & Data Issues**:
| Pain Point | Location | JTBD | Impact |
|---|---|---|---|
| Manual worklist, unclear ownership | Queue assignment | SN-037 | Multiple agents pick up same case; duplicated effort |
| Agents search for information | Case lookup | SN-087, SN-094 | 10+ minutes per case wasted on data hunting |
| Information scattered across systems | Legacy DB + spreadsheet + email | SN-037, SN-038 | Inconsistent version of truth; agents confused on current status |
| Spreadsheet conflicts & version control | Status tracking | SN-062 | Data conflicts; manual reconciliation needed |
| No unified communication history | Multiple contact channels | SN-002, SN-036 | Customers repeat their story; agents lack context |

**Process & Workflow Issues**:
| Pain Point | Location | JTBD | Impact |
|---|---|---|---|
| Repeated customer contact attempts | Contact sequencing | SN-028 | Customers frustrated; avoidable agent contact |
| Customers unaware of application stage | Multi-channel communication | SN-036 | Customer confusion; lower trust; more follow-ups needed |
| Missed follow-ups fall between shifts | Follow-up enforcement | SN-040 | Promises to call customers not kept |
| Cases stuck in "pending callback" | Follow-up tracking | SN-053, SN-118 | Work bottleneck; customers waiting indefinitely |
| Manual promise tracking | Promise recording | (SN-112) | Error-prone; relies on agent memory |
| No escalation rules | Routing logic | SN-005 | Inconsistent treatment; complex cases not routed correctly |
| Manual status reconciliation for reporting | End-of-period | SN-043 | Managers see lag, not real-time status; late decisions |
| Inconsistent status codes | Status standardization | SN-085, SN-122 | Different agents use different codes; chaos in reporting |

### Case Segmentation (From Self-Service Candidates Analysis)

| Segment | % of Portfolio | Characteristics | Automation Suitability |
|---|---|---|---|
| **Straightforward** | 38% | Early delinquency (5-28 days), low/medium balance, no risk flags | **HIGH** — ideal for self-service & automation |
| **Engaged** | 15% | Customer already in contact, showed willingness to resolve | **HIGH** — responding to communication |
| **Complex/High-Risk** | 22% | Late delinquency (>60 days), high balance, risk flags, legal watch | **LOW** — requires agent judgment |
| **Unresponsive** | 20% | No response cycle, missing contact data | **MEDIUM** — needs targeted outreach |
| **Incomplete Data** | 5% | Missing contact info, conflicting records | **LOW** — cannot route safely without data cleanup |

**Time Savings Opportunity by Segment**:
- Straightforward: 40–50 min/case saved (via OPP-01, 02, 03, 04, 06)
- Engaged: 25–30 min/case saved (via OPP-01, 03, 05, 06)
- Complex: 8–15 min/case saved (via OPP-01, 03 only)
- Unresponsive: 15–25 min/case saved (via OPP-01, 05, 06, 07)
- Incomplete Data: 5–10 min/case saved (via OPP-01 only)

**Blended Average**: ~25 minutes per case

---

## Part 4: JTBD Priority Statements

### Top 3 Priority JTBD (Ranked by Frequency, Business Impact, Portal Relevance)

**SN-001 — "I want transparency and control over what I owe"** ⭐ **HIGH PRIORITY**
- **Stakeholder**: Amina Rahman (Operations); Customer perspective
- **Statement**: When a customer receives a recovery notice, I want complete visibility and control over what I owe, so I can make informed payment decisions and build trust with the organization.
- **Why Now**: Customers currently experience slow, repetitive contact journeys (15% revenue loss driver). Transparency directly addresses this.
- **Evidence**: SN-065 ("Customers pay more readily with transparency"), SN-081 ("Portal works because it gives control")
- **Addresses Stakeholder Need**: Customers — intuitive interface + self-control; Finance — recovery conversion uplift
- **Linked Opportunity**: OPP-02 (Self-Service Portal)

**SN-002 — "I want a record of previous conversations"** ⭐ **HIGH PRIORITY**
- **Stakeholder**: Daniel Okoye (Finance); Customer perspective
- **Statement**: When a customer needs to follow up on a recovery conversation, I want a record of what was discussed in previous calls, so I can avoid repeating information and progress faster toward resolution.
- **Why Now**: Customers calling back 3+ times due to lack of communication history is duplicated activity at scale.
- **Evidence**: SN-036 ("Customers transferred, repeat situation"), SN-028 ("No way to prevent re-contact")
- **Addresses Stakeholder Need**: Operations — eliminates duplicated calls; Product — creates single source of truth
- **Linked Opportunity**: OPP-01 (Unified Customer Profile), OPP-06 (Duplicate Contact Prevention), OPP-03 (Auto-Logging)

**SN-037 — "I want first-contact context"** ⭐ **HIGH PRIORITY**
- **Stakeholder**: Gareth Evans (Operations); Agent perspective (first-contact optimization)
- **Statement**: When an agent contacts a customer for the first time, I want them to access complete customer history and context, so I can receive a tailored conversation that addresses my specific situation.
- **Why Now**: First-contact optimization reduces callback cycles and improves resolution rates. Currently agents lack context.
- **Evidence**: SN-087 ("Agents pay to hunt for info"), SN-094 ("More time reading notes than calling customers")
- **Addresses Stakeholder Need**: Operations — reduces duplicate work; Agents — faster, clearer work
- **Linked Opportunity**: OPP-01 (Unified Customer Profile & History)

### Additional High-Priority JTBD

**SN-005 — "I want to manage my recovery plan myself"**
- **Stakeholder**: Tracy Field; Customer perspective
- **Statement**: When a customer receives a collections notice, I want the opportunity to manage my recovery plan myself, so I can resolve the situation at my own pace and regain control.
- **Why Now**: Current lack of self-control option forces customers through agent-dependent workflows; reduces speed and engagement.
- **Linked Opportunity**: OPP-04 (Self-Service Payment Plan Enrollment)

**SN-038 — "I want a single source of truth for actions"**
- **Stakeholder**: Sylvia Turner; Agent perspective
- **Statement**: When an agent takes action on a customer case, I want a single source of truth for all actions already taken, so agents can focus on next steps instead of verifying past work.
- **Why Now**: Manual errors, status discrepancies, and duplicate actions are direct efficiency blockers.
- **Linked Opportunity**: OPP-03 (Automated Communication Logging)

**SN-045 — "I want proactive, optimized contact timing"**
- **Stakeholder**: Amina Rahman; Operations/Business perspective
- **Statement**: When managing our debt recovery portfolio, I want to contact customers proactively at optimal times, so we can increase recovery rates and customer willingness to engage.
- **Why Now**: Current random contact sequencing misses recovery windows; planned outreach increases conversion.
- **Linked Opportunity**: OPP-07 (Proactive Contact Outreach Strategy)

**SN-043 — "I want to measure the impact of improvements"**
- **Stakeholder**: Simon Burns; Governance perspective
- **Statement**: When we implement a recovery improvement, I want to measure the actual impact on agent workload and efficiency, so we can justify the investment and prioritize future improvements.
- **Why Now**: Without clear measurement, it's impossible to defend further investment or optimize the roadmap.
- **Linked Opportunity**: OPP-05 (Auto Follow-Up Enforcement), OPP-06 (Duplicate Contact Prevention)

---

## Part 5: Seven Automation Opportunities (OPP-01 to OPP-07)

### Opportunity Map Summary

| Rank | OPP | Automation | Scope | Time Saved | 12mo ROI | JTBD Link | Phase |
|---|---|---|---|---|---|---|---|
| 1 | OPP-01 | Unified Customer Profile & History | 100% | 10–14 min/case | **✓ Positive** | SN-037 | Quick Win (Wks 1-4) |
| 2 | OPP-03 | Automated Communication Logging | 100% | 4–6 min/case | **✓ Positive** | SN-038 | Quick Win (Wks 1-4) |
| 3 | OPP-02 | Self-Service Balance & Payment Portal | 40% | 8–14 min avoided | **✗ Negative Base-Case** | SN-001, SN-002 | Phase 1 (Wks 5-12) |
| 4 | OPP-04 | Self-Service Payment Plan Enrollment | 25% straightforward | 8–12 min avoided | **✗ Negative (Uplift-Dependent)** | SN-005 | Phase 2 (Wks 13-20) |
| 5 | OPP-05 | Automated Follow-Up Scheduling & Enforcement | 100% | 3–5 min/follow-up | **✗ Negative (Uplift-Dependent)** | SN-045, SN-043 | Phase 1 (Wks 5-12) |
| 6 | OPP-06 | Duplicate Contact Prevention | 100% | 2 attempts prevented | *Embedded in OPP-01* | SN-028 | Phase 2 (Wks 13-20) |
| 7 | OPP-07 | Proactive Contact Outreach Strategy | 60% | 5–10 min + 4–6% recovery uplift | **✗ Negative (Uplift-Dependent)** | SN-045 | Phase 3 (Wks 21-28) |

### OPP-01: Unified Customer Profile & History (RANK 1)

**What**: Consolidate legacy DB, spreadsheet, email, CRM into single unified customer record. Finance DB = source of truth.

**Scope**: 100% of cases | High-volume | Repeatable | Low risk

**Time Saved**: 10–14 min/case (eliminates data lookup + cross-check work)

**Why It Ranks First**:
- Positive base-case ROI (pure time savings, no uplift needed)
- Dependency enabler: unlocks quality for OPP-02, OPP-04, OPP-05
- De-risks downstream automation by ensuring data quality
- Directly addresses SN-037 (first-contact context), SN-087 (agent time hunting), SN-094 (agent reading notes)

**Implementation**: Camunda phase B2 | ETL/API consolidation | Data governance rules

**JTBD Addressed**: SN-001, SN-002, SN-037, SN-038

---

### OPP-02: Self-Service Balance & Payment Portal (RANK 3)

**What**: Customers view balance, history, payment options. Avoids agent contact for ~40% of cases.

**Scope**: 40% of cases | High-volume | Repeatable | Low risk

**Time Saved**: 8–14 min agent call (inquiry cases)

**Base-Case ROI**: Negative on time savings alone (customer self-service reduces billable agent time)

**Strategic Rationale**: Core platform for scale. Enables OPP-04 (plan enrollment). Addresses customer JTBD (transparency, control).

**Features**:
- Account summary (balance, due date, payment history)
- Communication history (all interactions logged)
- Payment options (manual payment, plan selection)
- SMS/email verification for identity

**Implementation**: Camunda phase B4 | Pulls data from OPP-01 (unified record)

**JTBD Addressed**: SN-001 (transparency), SN-002 (history), SN-005 (self-control)

**Uplift Sensitivity** (Optional—low confidence):
- If uplift proven in pilot: recovery conversion +40% on 40% of cases = material upside
- Requires pilot evidence before broad funding

---

### OPP-03: Automated Communication Logging (RANK 2)

**What**: Outcome logged once (structured form) → auto-written to unified record, portal, audit log. Eliminates manual re-entry.

**Scope**: 100% of cases | Structured outcome codes | Validation (date/amount)

**Time Saved**: 4–6 min/case (eliminates manual re-entry duplicate work)

**Why It Ranks Second**:
- Positive base-case ROI (direct time savings)
- Low complexity to implement
- Immediate control + data quality gain
- Directly addresses SN-038 (single source of truth), SN-002 (communication record)

**Agent Task**: Select outcome code, enter structured fields (date, amount, next action), save once. System propagates.

**Implementation**: Camunda phase B7 | Single API write | Transactional integrity

**JTBD Addressed**: SN-038 (source of truth), SN-002 (record)

---

### OPP-04: Self-Service Payment Plan Enrollment (RANK 4)

**What**: Eligible customers select from pre-approved plans in portal; auto-activates if within parameters. Avoids agent negotiation for ~25% of straightforward cases.

**Scope**: 25% of straightforward cases | ~9,500 annual cases

**Time Saved**: 8–12 min (avoids agent negotiation)

**Base-Case ROI**: Negative (time savings don't cover implementation cost)

**Uplift Rationale** (Low-confidence):
- Manual plan conversion: 165 successes / 1,405 attempts = 11.74%
- Portal plan conversion: 225 successes / 546 attempts = 41.21%
- Gap: ~30 percentage points (uplift potential if behavior holds at scale)
- Base-case model excludes this gap; treats as pilot-dependent upside

**Eligibility**: Balance ≤£2,000 | No prior breaches | Risk = Low | Early/mid-stage delinquency

**Pre-Approved Plans**:
- 3-month (higher payment)
- 6-month (lower payment)
- Hardship (structured, longer term)

**Out-of-Scope**: Balances >£2,000 or high-risk accounts → escalate to agent

**Implementation**: Camunda phase B4b | Rules engine | Portal integration

**JTBD Addressed**: SN-005 (customer self-control)

**Recommendation**: Pilot with high-confidence segment. Unlock broader funding only if uplift is evidenced.

---

### OPP-05: Automated Follow-Up Scheduling & Enforcement (RANK 5)

**What**: Promised payment date triggers timer. Day-before: SMS reminder + agent callback task. No payment by date+2 days → auto-escalate.

**Scope**: 100% of cases with promises

**Time Saved**: 3–5 min per follow-up (eliminates missed callbacks, manual reminders)

**Base-Case ROI**: Negative on time savings alone

**Uplift Rationale** (Low-confidence):
- Finance assumes 2.5% uplift in recovery rate if promises are kept better
- Requires evidence that timer → better promise adherence

**De-Duplication Rule**: Check "contacted in past 5 days?" before creating agent callback task

**Implementation**: Camunda phase B8c | Timer event | Auto-escalation logic

**JTBD Addressed**: SN-045 (proactive), SN-038 (single source)

**Recommendation**: Treat as conditional upside. Validate effect on promise-keeping outcomes before scaling.

---

### OPP-06: Duplicate Contact Prevention (RANK 6)

**What**: Check contact history before agent initiates. Warn if customer contacted within 3–7 days. Suggest optimal retry date. Agent can override (logged).

**Scope**: 100% of contact attempts | De-duplication logic

**Time Saved**: Prevents ~2 wasted attempts per case (~20% efficiency gain on outbound)

**Implementation**: Camunda phase B6 | Pop-up banner | Logging of overrides

**Logic Example**:
- No reply on 2026-02-01 → suggest retry 2026-02-05
- If spoke to customer → 7-day window before re-contact
- Agent can override if business justifies

**JTBD Addressed**: SN-028 (prevent repeated contacts), SN-037 (optimize agent time)

---

### OPP-07: Proactive Contact Outreach Strategy (RANK 7)

**What**: Daily algorithm identifies cases due for contact (promised date, callback, no contact >10 days). Scores by recovery likelihood. Assigns prioritized worklist.

**Scope**: 60% of active cases | Scoring: amount + days past due + risk + historical fulfillment rate

**Time Saved**: 5–10 min (strategic vs. random sequencing)

**Uplift**: 4–6% recovery rate improvement (from optimized timing)

**Implementation**: Camunda phase B10 | Batch job daily | Dashboard visibility | Configurable weights

**JTBD Addressed**: SN-045 (proactive contact)

---

## Part 6: Process Map & Handoff Insights

### As-Is Process (BPMN Model: `as-is-model.bpmn`)

**Three Swimlanes**:
1. **System Queue** — Account enters delinquency, joins manual worklist
2. **Collections Agent** — Core workflow: receive case, look up info, contact customer, record outcome, track follow-up
3. **Operations Manager** — Oversees status, reconciles data

**Major Pain Points Marked on Map**:

| Step | Pain Point | JTBD |
|---|---|---|
| Case assignment | Manual worklist, unclear ownership | SN-087 |
| Agent reads history | Time spent searching + reading notes | SN-094 |
| Data lookup | Scattered across systems | SN-037 |
| Contact sequencing | Random, not optimized | SN-045 |
| Promise tracking | Manual, error-prone | SN-112 |
| Status updates | Duplicated across systems | SN-038, SN-111 |
| Follow-up enforcement | Missed callbacks, shift gaps | SN-040, SN-053 |
| Escalation routing | No clear rules | SN-005 |
| Reconciliation | Manual, end-of-period | SN-043 |
| Status codes | Inconsistent across agents | SN-085, SN-122 |

### To-Be Process (Sketch — Camunda Phases B2–B10)

**Phases**:
- **B2**: Unified Customer Profile (OPP-01) — Data consolidation complete
- **B4**: Self-Service Portal (OPP-02) — Customers can self-serve 40% of cases
- **B4b**: Payment Plan Enrollment (OPP-04) — Portal enables customer-driven plans
- **B6**: Duplicate Contact Prevention (OPP-06) — De-dup engine prevents re-contact
- **B7**: Auto-Logging (OPP-03) — Single entry point, system propagates
- **B8c**: Follow-Up Enforcement (OPP-05) — Timer-based promises, auto-reminders
- **B10**: Proactive Outreach (OPP-07) — Daily prioritized worklist by recovery likelihood

---

## Part 7: Financial Modeling & ROI

### Baseline Metrics & Assumptions (From Templates & Finance Data)

**Key Assumptions**:

| ID | Assumption | Value | Unit | Source | Confidence |
|---|---|---|---|---|---|
| A-01 | Agent hourly cost | £22 | GBP/hr | Finance workbook | High |
| A-02 | Working days per month | 21 | days | Finance | High |
| A-03 | Straightforward case share | 38% | ratio | Operations estimate | Medium |
| A-04 | Avg straightforward handling (current) | 18 | min | Operations leadership | Medium |
| A-05 | Target straightforward handling (future) | 10 | min | Operations target | Medium |
| A-06 | Missed follow-up rate | 14% | ratio | Activity tracker analysis | Medium |
| A-07 | Recovery uplift (payment plan) | 4% | ratio | Finance estimate | Low |
| A-08 | Recovery uplift (promise capture) | 2.5% | ratio | Finance estimate | Low |
| A-09 | Monthly recovery baseline | £8,000,000 | GBP | Finance workbook | Medium |
| A-10 | Implementation cost (low complexity) | £45,000 | GBP | Product delivery | Medium |
| A-11 | Implementation cost (medium complexity) | £85,000 | GBP | Product delivery | Medium |

**Baseline Data Volumes** (From Sample):

| Metric | Sample Value | Extrapolation Rule | Population Estimate |
|---|---|---|---|
| Accounts in sample dataset | 3,246 | Not yet validated; sample ≠ monthly flow | 100,000+ (stock at point in time) |
| Activity records in sample | ~200 | Insufficient to establish monthly pattern | Unknown monthly volume |
| Straightforward % in sample | 38% | Assumed representative | 38,000 accounts straightforward |
| Engaged % in sample | 15% | Assumed representative | 15,000 accounts engaged |
| Complex % in sample | 22% | Assumed representative | 22,000 accounts complex |

**Annual Calculations** (Using Sample-Derived Percentages):

- **Straightforward annual volume**: 38,000 × 12 = 456,000 cases (annualization of current stock)
- **Time savings OPP-01**: 456,000 × (18-10) min / 60 min/hr × £22/hr = **£2,736,000**
- **Blended average (all segments)**: 100,000 × 12 × 25 min / 60 / £22 = **~£9,166,667 potential**

### Ranking Methodology

**Weighted Scoring** (50% Financial + 30% Strategic + 20% Feasibility):
- **Financial (50%)**: 12-month ROI, payback speed, hard vs. soft savings
- **Strategic (30%)**: Dependency impact, enables other opportunities, reduces execution risk
- **Feasibility (20%)**: Complexity, delivery risk, adoption difficulty

**Base-Case Rule**: Only operational time/cost savings count in 12-month ROI. Uplift shown separately as low-confidence upside.

### Opportunity Scores & Ranking

| Opportunity | Financial (50%) | Strategic (30%) | Feasibility (20%) | Weighted Score | Rank | Base-Case 12mo ROI |
|---|---|---|---|---|---|---|
| OPP-01 | 5.0 | 5.0 | 3.0 | **4.60** | **1** | **✓ Positive** |
| OPP-03 | 4.0 | 4.0 | 4.0 | **4.00** | **2** | **✓ Positive** |
| OPP-02 | 2.0 | 4.5 | 3.0 | **2.95** | **3** | ✗ Negative |
| OPP-04 | 1.5 | 3.0 | 3.0 | **2.25** | **4** | ✗ Negative (Uplift-Dep.) |
| OPP-05 | 1.5 | 2.5 | 3.0 | **2.10** | **5** | ✗ Negative (Uplift-Dep.) |
| OPP-06 | 2.5 | 3.5 | 3.5 | **3.10** | **6** | Embedded in OPP-01 |
| OPP-07 | 1.8 | 2.8 | 2.5 | **2.25** | **7** | ✗ Negative (Uplift-Dep.) |

### Sensitivity Analysis (Conservative vs. Optimistic)

**Conservative Band**:
- OPP-01: 10 min saved, full implementation cost, slower adoption
- OPP-02: 40% scope, 8 min saved, no uplift
- OPP-03: 4 min saved, partial form compliance
- OPP-04: 25% of straightforward, 8 min saved, no uplift
- OPP-05: Base promise rate, 3 min/follow-up, no uplift

**Optimistic Band**:
- OPP-01: 14 min saved, faster rollout, full adoption
- OPP-02: 50–60% scope, 14 min saved, lower call deflection lag
- OPP-03: 6 min saved, high compliance
- OPP-04: 35% of straightforward, 12 min saved, uplift proven
- OPP-05: Higher promise coverage, 5 min/follow-up, uplift proven

**Key Finding**: OPP-01 and OPP-03 resilient in both bands. OPP-02, OPP-04, OPP-05 uplift-dependent and should be piloted before full funding.

---

## Part 8: Critical Gaps & Assumptions (IMPORTANT FOR ADKAR PLANNING)

### The Sample Data Caveat ⚠️

**What We Have**:
- Sample delinquent account extract: 3,246 accounts (point-in-time)
- Activity tracker: ~200 sample records
- Finance assumptions: baseline £8m/month recovery

**What We Don't Have**:
- Validation that 38% straightforward in sample = 38% in full 100,000 portfolio
- Monthly inflow/outflow rates (sample is a stock snapshot, not a cohort)
- Proof that activity tracker patterns scale linearly
- Sensitivity analysis on sample representativeness

**Risk to ADKAR**:
- Finance (Daniel) will ask: "How do you know your 38% straightforward holds for all 100,000 accounts?"
- Operations (Amina) will ask: "If this breaks down at scale, what's our fallback?"
- Agents (Gareth) will ask: "Are you changing my job based on a sample that might not match my actual work?"

**Recommendation for ADKAR Prep**:
- **Transparently flag this assumption in all stakeholder communications**
- **Commit to validation plan** (e.g., "We will validate segment distribution on full population in Week 2")
- **Define sensitivity triggers** (e.g., "If straightforward drops below 30%, OPP-02 ROI turns negative")

---

### Incomplete Templates & Unfinished Deliverables

**ROI Model Spreadsheet**: 
- Templates exist in `templates/roi-model/`:
  - `01-assumptions.csv` — All rows marked TODO; no populated values
  - `02-baseline-metrics.csv` — All rows marked TODO; no populated values
  - `03-opportunities.csv` — All rows marked TODO; no populated values
  - `04-roi-summary.csv` — Template only; no calculations
- **Status**: Framework in place; values to be filled with validated data

**Process Map Verification**:
- As-Is map (BPMN) complete and marked with pain points
- To-Be map sketched in submission text; not formalized as Camunda BPMN yet
- **Recommendation**: Create formal To-Be BPMN before change rollout (needed for agent training, system design)

---

### Key Assumptions Needing Validation

1. **Straightforward case rate (38%)**: Validate on full 100,000 portfolio. If <30%, OPP-02/OPP-04 ROI flips negative.
2. **Portal adoption rate**: Assumed 40–60% for OPP-02. Pilot required before full build.
3. **Promise-keeping uplift (2.5–4%)**: Finance projection. Pilot required to validate.
4. **Agent productivity (target 10 min vs. current 18 min)**: Depends on tool quality + change adoption. Pilot needed.
5. **Monthly account inflow/outflow**: Sample is stock; cohort behavior unknown. Need monthly flow data.

---

## Part 9: Traceability Matrix (Pain Point → JTBD → Opportunity → Requirement)

**Purpose**: Link every stakeholder concern to a future system requirement so that Priya (Product) can build a traceable backlog.

| Stakeholder Evidence | Concern | JTBD | Pain Point | Automation Opportunity | Likely Requirement |
|---|---|---|---|---|---|
| SN-001, SN-065, SN-081 | Payment transparency | SN-001 | No visibility of balances | OPP-02 (Portal) | Portal must show real-time balance, payment history, options |
| SN-002, SN-028, SN-036 | Prevent re-contact | SN-002, SN-028