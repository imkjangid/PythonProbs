# Real-World Example: Booking a smartphone order
def order_phone(brand, model):
    print(f"Order Confirmed: {brand} {model}")

# Perfect Order
order_phone("Apple", "iPhone 15")  # Output: Order Confirmed: Apple iPhone 15

# Wrong Order Trap! (Agar sequence badla, toh meaning badal jayega)
order_phone("iPhone 15", "Apple")  # Output: Order Confirmed: iPhone 15 Apple