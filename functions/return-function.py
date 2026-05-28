# Example: Calculating the total price of apples
def calculate_bill():
    price_per_kg = 120 # Rs/kg, price
    weight = 3 # kgweight
    total_price = price_per_kg * weight
    return total_price

# Calling the function with values
my_bill = calculate_bill() # returned value assigned to a variable
print("Total Bill Amount: Rs.", my_bill) # Output: Total Bill Amount: Rs. 360