# Bitwise Behavior
# Binary mapping: 5 is 0101, 3 is 0011
val_a = 5 
val_b = 3

# Bitwise AND: 0101 & 0011 = 0001 (which is 1)
print("Bitwise AND (&) result:", val_a & val_b) # Output: 1

# Left Shift: 0101 << 1 becomes 1010 (which is 10)
print("Left Shift (<< 1) effectively multiplies by 2:", val_a << 1) # Output: 10