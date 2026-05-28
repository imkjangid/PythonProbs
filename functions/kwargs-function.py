# ==========================================
# WORKING WITH **KWARGS (DICTIONARY PACKING)
# ==========================================
# Real-World Example: Creating a student profile card
def print_student_profile(name, **details):
    print(f"\n--- Student: {name} ---")
    print("Under the hood, details are stored as:", type(details)) # Output: <class 'dict'>
    
    # Looping through the collected dictionary items
    for key, value in details.items():
        print(f" -> {key.capitalize()}: {value}")

# Calling the function with varying named details
print_student_profile("XYZ", age=36, city="Ahmedabad", course="Python")
print_student_profile("ABC", city="Jaipur", role="Developer")