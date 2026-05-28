# Syntax Pattern: lambda arguments: expression

# Regular or Standard Function
def square_num(x): return x ** 2

# Equivalent Lambda Function
quick_square = lambda x: x ** 2
print("Lambda Execution:", quick_square(5)) # Output: 25

# Real-World Use Case: Inline conditional string sanitation formatting
clean_input = lambda text: text.strip().lower()
print(clean_input("   ARCHITECTNK.COM   ")) # Output: architectnk.com