# ==========================================
# NESTED CONDITIONAL GATEWAYS
# ==========================================
has_account = True
is_logged_in = False

if has_account:
    if is_logged_in:
        print("Redirecting to Dashboard...")
    else:
        print("Alert: Please login first.")
else:
    print("Redirecting to Registration Page...")