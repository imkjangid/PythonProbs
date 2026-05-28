# ==========================================
# WORKING WITH *ARGS (TUPLE PACKING)
# ==========================================
# Real-World Example: Adding items to a shopping cart
def calculate_total_items(*items):
    print("Under the hood, items are stored as:", type(items)) # Output: <class 'tuple'>
    print("Items list:", items)
    
    total = len(items)
    return f"Total items in your shopping cart: {total}"

# Calling the same function with different number of inputs
print(calculate_total_items("Book", "Pen"))          # Passing 2 inputs
print(calculate_total_items("Laptop", "Mouse", "Bag", "Mic")) # Passing 4 inputs