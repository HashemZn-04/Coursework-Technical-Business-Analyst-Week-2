# Smart-Recovery Portal Prototype — README

Lightweight Flask prototype of the Phase 1 To-Be self-service journey. Monochrome (black/white/gray) only, mock login + mock identity verification, in-memory mock data — no database, no real payments.

## Click-through the main path (reviewer quick start)

```
cd submissions/prototype
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

Open `http://127.0.0.1:5000` and follow this exact path:

1. **Landing** → log in with `jdoe` / `password123` (credentials are also shown on-screen).
2. **Identity Verification** → enter code `123456` (also shown on-screen).
3. **Account Summary** → review balance/overdue/history, then click **Promise to Pay**.
4. **Promise to Pay** → enter a date and amount → **Confirm Promise**.
5. **Confirmation** → shows the outcome → **Back to Account Summary**.
6. From the sidebar, also try **Payment Plan** (setup → review/pay), **Pay Upfront**, and **Contact Agent** to see the remaining branches.
7. **Logout** (bottom of sidebar) → returns to Landing and clears the session.

To see the two exception paths:
- **Failed verification**: at step 2, enter any wrong code 3 times → routed to the **Routed to Agent** screen.
- **Ineligible / unsupported case**: log in as `arossi` / `password123` → Account Summary auto-redirects straight to **Routed to Agent** (this account is flagged complex/high-risk and is not eligible for self-service).

## Approach

- **Framework**: Flask, server-rendered Jinja templates, one shared `base.html` layout.
- **Auth (mock only)**: `mock_data.USERS` holds 3 hardcoded accounts (username, password, 6-digit verification code, account data, payment history). No password hashing, no real SMS/email — this is a UI/flow prototype, not a security implementation.
- **Session state**: Flask's signed cookie session tracks `username`, `verified`, and `verify_attempts`. Two decorators in `app.py` guard routes: `require_login` (must be logged in) and `require_verified` (must also have passed identity verification). Hitting any protected URL directly without the right session state redirects back to Landing or Verify.
- **Outcome logging**: `OUTCOME_LOG` (in-memory dict, resets on restart) stands in for the "Portal Outcome Reporting" write-back described in the To-Be process (BPMN node A11) — it's what the Confirmation screen reads from.
- **Sidebar navigation**: `base.html` renders a black, white-text vertical sidebar only when `session['verified']` is true (via a Flask `context_processor` that injects `show_sidebar`). This was not in `docs/wireframe.png` — it was added per stakeholder request so every screen has consistent navigation once a customer is authenticated and verified.
- **Styling**: single `static/style.css`, monochrome CSS variables only (`--black`, `--white`, `--gray-100/300/500/700`) — no other colors are used anywhere in the prototype.

## Scope note (traceability flag)

The approved [phase_1_scope_deliverables.md](../phase_1_scope_deliverables.md) explicitly **excludes** full self-service payment-plan enrollment (OPP-04) from Phase 1, and the BPMN "Customer Selects Action" gateway (A8, see [docs/06-phase-1-to-be.md](../../docs/06-phase-1-to-be.md)) only offers manual payment or promise-to-pay. The stakeholder's screen list for this exercise, however, explicitly asks for a "Promise-to-pay and/or payment-plan flow" screen. Both **Payment Plan** and **Pay Upfront** screens were built to satisfy that explicit ask and to close the wireframe gap identified in Step 1, but they go beyond the currently-approved Phase 1 backlog. This should be flagged to Priya Nair (Product) and Daniel Okoye (Finance/Compliance) before any of this prototype is treated as a build spec — it is not yet a signed-off requirement.

## Stakeholder Q&A (review feedback response)

**1. Payment Plan screens — "Phase 2 preview"**

Recommendation: **label as "Phase 2 preview," don't hide.** Both Payment Plan screens (and the sidebar link) now show a visible `Phase 2 preview` badge, and each screen states in-page that OPP-04 is excluded from the approved Phase 1 scope. Reasoning:
- Hiding the screens entirely would silently drop something the stakeholder's own brief asked to be sketched ("Promise-to-pay and/or payment-plan flow"), which risks looking like the ask was ignored rather than deliberately sequenced.
- Labeling keeps the traceability visible end-to-end (screen → scope doc → backlog) instead of requiring a side conversation to explain what leadership is looking at.
- It directly prevents the leadership-assumption risk you raised: nobody can walk through the demo and mistake this for a committed Phase 1 feature, because the badge and in-page note are on the screen itself, not just in this README.

**2. US-13 (customer abandonment / idle-timeout detection) — deferred or out of prototype scope?**

**Out of prototype scope entirely, not deferred.** US-13 and BPMN node A16 describe a *backend/session-lifecycle* concern (a boundary timer on A4/A7/A8 that logs an abandoned session and flags it for optional agent follow-up) — per [docs/03-wireframe-annotation-guide.md](../../docs/03-wireframe-annotation-guide.md), abandonment is an exception path to document, not a customer-facing screen. A real idle-timeout would need client-side JS timers plus a server-side "last screen viewed" log, which adds meaningful complexity for a click-through UI prototype whose purpose is demonstrating the happy path and the two customer-visible exception outcomes (failed verification, ineligible case). This was an intentional scoping decision for the prototype artifact, not a signal that US-13 itself is deprioritized in the backlog.

**3. US-17 (Operations Manager real-time dashboard) — intentional exclusion?**

**Yes, intentional.** Per [docs/06-phase-1-to-be.md](../../docs/06-phase-1-to-be.md), the Operations Manager dashboard lives in a separate BPMN pool ("Operations Manager") connected to the customer-facing pool only through a shared data store — it is a distinct, internal-facing application with its own audience (Amina Rahman / Operations), not a screen in the Smart-Recovery customer portal. This prototype's scope is the customer self-service journey (Pool 1) only, so US-17 correctly has no representation here. It would be a separate prototype if leadership wants one demoed.

## Screen-by-screen notes

Format follows the annotation convention in [docs/03-wireframe-annotation-guide.md](../../docs/03-wireframe-annotation-guide.md). Story IDs reference [docs/07-user-story-guide.md](../../docs/07-user-story-guide.md).

### Landing (`GET/POST /`) — `templates/landing.html`
- **Story:** US-01 (Customer opens self-service portal session)
- **Data:** username, password (mock-only, plaintext compare against `mock_data.USERS`)
- **Rule:** incorrect credentials re-render the form with an inline error; correct credentials reset the session and set `verify_attempts = 0`
- **Next step:** redirect to Identity Verification

### Identity Verification (`GET/POST /verify`) — `templates/verify.html`
- **Story:** US-02 (Verify customer identity via SMS/email); exception handling maps to US-12 (Handle failed identity verification)
- **Data:** 6-digit code compared against `mock_data.USERS[user]['verification_code']`
- **Rule:** 3 attempts maximum (`MAX_VERIFICATION_ATTEMPTS`); each wrong code shows "N attempt(s) remaining"; on the 3rd failure, redirect to Routed to Agent with `reason=verification_failed`; "Resend code" re-renders the same mock code (no real resend)
- **Next step:** success → Account Summary; exhausted attempts → Routed to Agent

### Account Summary (`GET /account-summary`) — `templates/account_summary.html`
- **Story:** US-06 (Display account summary) and US-07 (Present available self-service actions)
- **Data:** name, account reference, total balance, overdue amount, due date, delinquency status, last payment history
- **Rule:** only rendered after `require_verified` passes; if the account is flagged `eligible_for_self_service = False` (e.g. `arossi`), the request is redirected to Routed to Agent before this template ever renders
- **Next step:** customer chooses Promise to Pay, Payment Plan, Pay Upfront, or Contact Agent

### Promise to Pay (`GET/POST /promise-to-pay`) — `templates/promise_to_pay.html`
- **Story:** US-09 (Capture promise-to-pay details)
- **Data:** promised payment date, promised amount (pre-filled with the current overdue amount)
- **Rule:** structured date + numeric amount fields only, no free text, matching the "capture only, no auto-escalation" note in [docs/06-phase-1-to-be.md](../../docs/06-phase-1-to-be.md) (node A10); Cancel returns to Account Summary without writing an outcome
- **Next step:** Confirm → outcome written to `OUTCOME_LOG` → Confirmation (`outcome_type=promise`)

### Payment Plan — Setup (`GET/POST /payment-plan/setup`) — `templates/payment_plan_setup.html`
- **Story:** none in the approved Phase 1 backlog — see Scope note above; included for the stakeholder's screen list, not the signed-off scope doc; labeled with an on-screen `Phase 2 preview` badge (sidebar link and page heading) per the stakeholder Q&A recommendation
- **Data:** number of installments, payment interval
- **Rule:** selections are held in `session` (not yet committed) until the review step is completed; Cancel returns to Account Summary
- **Next step:** Continue → Payment Plan — Review & Pay

### Payment Plan — Review & Pay (`GET/POST /payment-plan/pay`) — `templates/payment_plan_pay.html`
- **Story:** none in the approved Phase 1 backlog — see Scope note above; also labeled `Phase 2 preview`
- **Data:** installments/interval carried over from Setup, total overdue amount, mock bank account to pay from
- **Rule:** direct navigation here without completing Setup redirects back to Setup (`session['plan_installments']` must exist); this is the review/confirm step missing from the original wireframe
- **Next step:** Confirm Plan → outcome written to `OUTCOME_LOG` → Confirmation (`outcome_type=plan`)

### Pay Upfront (`GET/POST /pay-upfront`) — `templates/pay_upfront.html`
- **Story:** closest approved analog is US-08 (Process manual payment) — "pay upfront" is this prototype's manual-payment equivalent
- **Data:** overdue amount due, mock bank account to pay from
- **Rule:** this screen did not exist in `docs/wireframe.png` even though "pay upfront" was listed as a text-only option on Account Summary; Cancel returns to Account Summary
- **Next step:** Pay → outcome written to `OUTCOME_LOG` → Confirmation (`outcome_type=upfront`)

### Confirmation (`GET /confirmation`) — `templates/confirmation.html`
- **Story:** customer-facing manifestation of US-10 (Write self-service outcome to unified record and communication log)
- **Data:** outcome type + details read back from `OUTCOME_LOG` for the current account
- **Rule:** did not exist anywhere in the original wireframe; every action path (promise, plan, upfront) must pass through here before returning to Account Summary
- **Next step:** Back to Account Summary (end of the self-service loop for this session)

### Contact Agent (`GET /contact-agent`) — `templates/contact_agent.html`
- **Story:** general support access, not tied to a specific Phase 1 automation story
- **Data:** static mock phone numbers (general inquiries, debt assistance, dispute/hardship)
- **Rule:** available at any time from the sidebar; does not change account/session state
- **Next step:** customer calls or returns to Account Summary

### Routed to Agent (`GET /routed-to-agent`) — `templates/routed_to_agent.html`
- **Story:** US-11 (Route ineligible cases to an agent), US-12 (Handle failed identity verification), and US-14 (Agent reviews pre-loaded unified profile on handoff)
- **Data:** routing reason (`verification_failed` or `ineligible_case`), account reference (shown as the "context preserved" reference number)
- **Rule:** this screen did not exist in `docs/wireframe.png` (only a generic "Contact Agent" list did); it is reached automatically, never chosen by the customer
- **Next step:** Return to Login (session ends; in the real system, an agent picks up the case with full context per US-14)

## Known limitations (prototype only)
- No password hashing, no real SMS/email delivery, no persistence across restarts (`OUTCOME_LOG` and sessions reset when the Flask process restarts).
- No CSRF protection, no input sanitization beyond basic HTML form types — not production-hardened, for review purposes only.
