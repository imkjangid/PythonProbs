# Logical chaining
is_admin = True
has_valid_token = False

# Evaluates both paths unless short-circuiting triggers
print("Logical AND gateway:", is_admin and has_valid_token) # Output: False
print("Logical NOT inversion:", not has_valid_token)       # Output: True