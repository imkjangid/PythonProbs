# Identity Behavior
list_a = [1, 2]
list_b = [1, 2]
list_c = list_a # Points to same memory reference

print("Value Equality (list_a == list_b):", list_a == list_b) # Output: True
print("Identity Reference (list_a is list_b):", list_a is list_b) # Output: False
print("Shared Identity Check (list_a is list_c):", list_a is list_c) # Output: True