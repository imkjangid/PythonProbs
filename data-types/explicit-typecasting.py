# Explicit typecasting

# float to int
my_float = 9.81
my_int = int(my_float)  # Truncates the decimal part
print(my_int) # Output: 9

# str to int
my_str_num = "42"
my_int_from_str = int(my_str_num)
print(my_int_from_str + 1) # Output: 43

# int to str
my_int_val = 123
my_str_val = str(my_int_val)
print("The number is " + my_str_val) # Output: The number is 123