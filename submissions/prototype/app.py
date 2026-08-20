"""Smart-Recovery self-service portal prototype: mock auth + core journey routes."""

from functools import wraps

from flask import Flask, redirect, render_template, request, session, url_for

from mock_data import BANK_ACCOUNTS, MAX_VERIFICATION_ATTEMPTS, USERS

app = Flask(__name__)
app.secret_key = "prototype-only-not-for-production"

# In-memory outcome log, keyed by account_ref, reset on app restart.
OUTCOME_LOG = {}


def require_login(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("landing"))
        return view(*args, **kwargs)

    return wrapped


def require_verified(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("landing"))
        if not session.get("verified"):
            return redirect(url_for("verify"))
        return view(*args, **kwargs)

    return wrapped


def current_user():
    return USERS[session["username"]]


@app.context_processor
def inject_sidebar_flag():
    return {"show_sidebar": bool(session.get("verified"))}


@app.route("/", methods=["GET", "POST"])
def landing():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        user = USERS.get(username)
        if user and user["password"] == password:
            session.clear()
            session["username"] = username
            session["verify_attempts"] = 0
            return redirect(url_for("verify"))
        error = "Incorrect username or password."
    return render_template("landing.html", error=error)


@app.route("/verify", methods=["GET", "POST"])
@require_login
def verify():
    user = current_user()
    error = None
    if request.method == "POST":
        code = request.form.get("code", "").strip()
        if code == user["verification_code"]:
            session["verified"] = True
            return redirect(url_for("account_summary"))
        session["verify_attempts"] += 1
        remaining = MAX_VERIFICATION_ATTEMPTS - session["verify_attempts"]
        if remaining <= 0:
            return redirect(url_for("routed_to_agent", reason="verification_failed"))
        error = f"Incorrect code. {remaining} attempt(s) remaining."
    return render_template("verify.html", user=user, error=error)


@app.route("/resend-code", methods=["POST"])
@require_login
def resend_code():
    # Prototype only: code is fixed, "resend" just returns to the verify screen.
    return redirect(url_for("verify"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("landing"))


@app.route("/account-summary")
@require_verified
def account_summary():
    user = current_user()
    if not user["eligible_for_self_service"]:
        return redirect(url_for("routed_to_agent", reason="ineligible_case"))
    return render_template("account_summary.html", user=user)


@app.route("/promise-to-pay", methods=["GET", "POST"])
@require_verified
def promise_to_pay():
    user = current_user()
    if request.method == "POST":
        OUTCOME_LOG[user["account_ref"]] = {
            "type": "promise",
            "amount": request.form.get("amount"),
            "date": request.form.get("promise_date"),
        }
        return redirect(url_for("confirmation", outcome_type="promise"))
    return render_template("promise_to_pay.html", user=user)


@app.route("/payment-plan/setup", methods=["GET", "POST"])
@require_verified
def payment_plan_setup():
    user = current_user()
    if request.method == "POST":
        session["plan_installments"] = request.form.get("installments")
        session["plan_interval"] = request.form.get("interval")
        return redirect(url_for("payment_plan_pay"))
    return render_template("payment_plan_setup.html", user=user)


@app.route("/payment-plan/pay", methods=["GET", "POST"])
@require_verified
def payment_plan_pay():
    user = current_user()
    if "plan_installments" not in session:
        return redirect(url_for("payment_plan_setup"))
    if request.method == "POST":
        OUTCOME_LOG[user["account_ref"]] = {
            "type": "plan",
            "installments": session.get("plan_installments"),
            "interval": session.get("plan_interval"),
            "bank_account": request.form.get("bank_account"),
        }
        return redirect(url_for("confirmation", outcome_type="plan"))
    return render_template(
        "payment_plan_pay.html",
        user=user,
        installments=session.get("plan_installments"),
        interval=session.get("plan_interval"),
        bank_accounts=BANK_ACCOUNTS,
    )


@app.route("/pay-upfront", methods=["GET", "POST"])
@require_verified
def pay_upfront():
    user = current_user()
    if request.method == "POST":
        OUTCOME_LOG[user["account_ref"]] = {
            "type": "upfront",
            "amount": user["overdue_amount"],
            "bank_account": request.form.get("bank_account"),
        }
        return redirect(url_for("confirmation", outcome_type="upfront"))
    return render_template("pay_upfront.html", user=user, bank_accounts=BANK_ACCOUNTS)


@app.route("/confirmation")
@require_verified
def confirmation():
    user = current_user()
    outcome_type = request.args.get("outcome_type", "promise")
    outcome = OUTCOME_LOG.get(user["account_ref"], {})
    return render_template(
        "confirmation.html", user=user, outcome_type=outcome_type, outcome=outcome
    )


@app.route("/contact-agent")
@require_verified
def contact_agent():
    user = current_user()
    return render_template("contact_agent.html", user=user)


@app.route("/routed-to-agent")
def routed_to_agent():
    reason = request.args.get("reason", "unsupported_case")
    username = session.get("username")
    user = USERS.get(username) if username else None
    return render_template("routed_to_agent.html", user=user, reason=reason)


if __name__ == "__main__":
    app.run(debug=True)
