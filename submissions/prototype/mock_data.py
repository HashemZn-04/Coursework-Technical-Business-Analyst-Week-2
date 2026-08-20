"""Hardcoded mock data for the Smart-Recovery portal prototype (no DB/CSV)."""

USERS = {
    "jdoe": {
        "password": "password123",
        "verification_code": "123456",
        "name": "Jane Doe",
        "account_ref": "LT-100234",
        "balance": 842.50,
        "overdue_amount": 210.00,
        "due_date": "2026-08-28",
        "delinquency_status": "Early delinquency (12 days)",
        "eligible_for_self_service": True,
        "payment_history": [
            {"date": "2026-07-15", "amount": 150.00, "method": "Bank transfer"},
            {"date": "2026-06-15", "amount": 150.00, "method": "Bank transfer"},
        ],
    },
    "mchen": {
        "password": "password123",
        "verification_code": "654321",
        "name": "Marcus Chen",
        "account_ref": "LT-100589",
        "balance": 3120.75,
        "overdue_amount": 980.00,
        "due_date": "2026-08-22",
        "delinquency_status": "Engaged (contacted, willing to resolve)",
        "eligible_for_self_service": True,
        "payment_history": [
            {"date": "2026-07-20", "amount": 200.00, "method": "Card"},
        ],
    },
    "arossi": {
        "password": "password123",
        "verification_code": "111222",
        "name": "Amara Rossi",
        "account_ref": "LT-100812",
        "balance": 15400.00,
        "overdue_amount": 6200.00,
        "due_date": "2026-08-10",
        "delinquency_status": "Complex/high-risk (74 days, legal watch)",
        "eligible_for_self_service": False,
        "payment_history": [],
    },
}

BANK_ACCOUNTS = [
    {"id": "acc-checking", "label": "Checking Account ****4821"},
    {"id": "acc-savings", "label": "Savings Account ****9037"},
]

MAX_VERIFICATION_ATTEMPTS = 3
