# Real-World Example: Default shipping destination is hardcoded to India
def create_shipping_label(customer_name, country="India"):
    print(f"Shipping to: {customer_name}, Country: {country}")

# 1. Missing the optional parameter (Triggers default fallback "India")
create_shipping_label("Kapil")  # Output: Shipping to: Kapil, Country: India

# 2. Providing the optional parameter (Overwrites default to "USA")
create_shipping_label("Yash", country="USA")  # Output: Shipping to: Yash, Country: USA