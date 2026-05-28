# ==========================================
# MULTI-CONDITION CHAINING (if-elif-else)
# ==========================================
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"  # This block fires, and the rest of the chain is skipped
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Resulting Grade Matrix: {grade}")