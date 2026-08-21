# Coursework Technical Business Analyst Week 2
Hashem Znati


## ADKAR Assessment
[Click here to view table](<./ADKAR Assessment (Legacy Trust).xlsx>)

## Phase 1 Scope

## System aspects and capabilities
Identity Verification
Justification
While it is not a specified automation opportunity, it is required for the implementation of OPP-02 (Self-service balance and payment portal) because without identity verification the system cannot show payment and balance data safely. This is tied to Daniel’s audit concern as well as the compliance


Account Summary
Justification
This is the skeleton for OPP-02 (self-service balance and payment portal) and is echoed by SN-001 and SN-002 from stakeholder notes which allow for a transparent view of summarised account details.

Caveat: OPP-02 has a negative base-case ROI and is included because it has a 40% scope of all cases and saves 8 minutes on average.

Unified customer profile and history (OPP-01)
Justification
This is the highest-performing automation opportunity and is the foundation that many other opportunities build on. SN-037’s pain points can be summed as scattered systems and version conflicts. This will be foundational to phase 1 despite potential ADKAR risks because the benefits far outweigh.
This also includes defining data governance and conflict-resolution logic like which source being favoured over the other when the DB, spreadsheet and email have conflicting data.


Automated communication logging (OPP-03)
Justification
SN-038 details a demand for a single source of truth. This also answers Daniel’s (Finance) audit requirement for measurable and evidence-based savings, while also satisfying Finance’s manual status reconciliation pain point.


Promise-to-pay capture
Justification
By automating follow-up scheduling. While its base-case ROI is negative, when including uplift it provides significant savings while also saving time on follow-ups (average of 3 minutes). This is reinforced by SN-045 and SN-112’s pain points as well as Gareth (Senior Team Leader). To keep phase 1’s scope focused, this does not include auto-escalation discussed for OPP-05 which is higher risk, and rather just the capture aspect.

Portal Outcome Reporting
Justification
This is a functional requirement for OPP-02. Including identity verification and account summary allows clients to view their account, and portal outcome reporting allows for every self-service action like balance viewing and manual payments by the client to be written back to their profile (OPP-01) and their communication logs (OPP-03).


### Exclusions
Hardship Assessment
Justification
This has been segmented as high-risk and complex because late delinquency, high-balance accounts are highly difficult to automate and require extensive agent judgement. This is reinforced by Amina’s beliefs that straightforward cases must not be tangled with complex cases.

Legal escalation workflow
Justification
Automation of legal escalation is not any of the automation opportunities, this is similar to the reasoning applied for Hardship Assessment as legal/high-risk cases must stay manual especially for phase 1.
Full self-service payment plan enrollment (OPP-04)

Justification
In documentation, this was specifically stated as a phase 2 deliverable due to OPP-04 having a negative base-case ROI. Its 30% uplift increase is low-confidence as it is pilot-dependent (being phase 1) where OPP-01 and OPP-02 must be proven first.

Proactive contact outreach algorithm
Justification
This has been detailed as a phase 3 deliverable because it depends on OPP-01’s data quality and OPP-01’s implementation will also determine if its 4-6% uplift is attainable as it is currently low confidence.
Complete follow-up auto-escalation (OPP-05 second half)
Justification
As discussed in the promise-to-pay capture, excluding auto-escalation from scope allows for validating if uplift is attainable for OPP-05, this is also because OPP-05 is partially uplift-dependent for success.


## Assumptions
The legacy data needed from the legacy DB, spreadsheets and emails for the new portal’s account summary page must be complete and accessible enough for phase 1. It is highly unlikely the data will be fully complete.

Our current operations must be able to support a phased rollout for this new system, where phase 1 brings only the core functionality for user acceptance testing.

OPP-02’s scope of 40% being straightforward cases relies on a 3,426 account sample, and may not reflect the true rates of the 100,000+ Legacy Trust client accounts.

The governance rules stated for OPP-01 must be accepted quickly enough by Operations and Finance such that it does not delay the development of OPP-01 and subsequent steps.


## Dependencies and Constraints
The identity verification is currently classified as an SMS/Email verification for end-users. Currently for phase 1, we only have this lightweight approach. There are no existing IAM or KYS systems identified in discovery. Therefore, identity verification needs confirmation with IT if this can integrate with the existing customer authentication system or needs a new build.

Additionally, due to Daniel’s finance mandate, any identity check that is end-user-based needs a compliance sign-off. This has not yet been scoped as a timeline item, and it should be added in the backlog as a dependency instead of a user story.

OPP-02 cannot start in development until OPP-01 finished, thus making OPP-01 a critical path. Because the entire purpose of OPP-02 is to pull data from the unified customer profile.


## Why the scope is credible
This scope is credible because for phase 1, only the top ranked automation opportunities are considered that grant the highest time saving and ROI benefits, as well as the core functionalities required for these top automation opportunities.

They will create measurable value and performance metrics within weeks that can allow us to assess their predicted success rate overtime as well as extrapolating the performance to the lower-ranked automation opportunities.

Opportunities 1,2, and 3 are chosen as they are also the easiest to implement, with 1 and 3 being quick wins that can be completed in the first half of phase 1. Additionally, it also means that these opportunities carry the least change and adoption risk for agents as they are end-user focused, taking manual work away from agents and giving more control to the clients.

## Deliverables
[Click here to view table](<./Deliverables (Legacy Trust).xlsx>)
