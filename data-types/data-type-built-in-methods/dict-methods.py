# ==========================================
# ADVANCED KEY-VALUE EXTRACTION
# ==========================================
user_session = {"user_id": 101, "role": "admin", "status": "Active"}

# Safe retrieval using .get() to prevent explicit KeyError crashes
# Syntax: .get(key, default_value)
print("Role Resolved:", user_session.get("role", "Guest"))
print("Token Check (Fallback):", user_session.get("auth_token", "NOT_FOUND"))

# Fetching isolated dynamic view loops
print("Dictionary Keys View:", list(user_session.keys()))
print("Dictionary Values View:", list(user_session.values()))

# Merging dictionaries using .update()
user_session.update({"status": "Suspended", "flagged": True})
print("Updated Dictionary Payload:", user_session)