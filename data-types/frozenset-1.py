# 1. INITIALIZATION & TYPE CHECKING

# Creating a frozen set from a list
fs1 = frozenset([10, 20, 30, 40, 20]) # Duplicates (20) are automatically removed
print("Frozen Set 1:", fs1)           # Output: frozenset({40, 10, 20, 30})
print("Data Type:", type(fs1))        # Output: <class 'frozenset'>

# Creating a frozen set from a string
fs_str = frozenset("kapil")
print("Frozen Set from String:", fs_str) # Output: Unique unordered characters

# Creating an empty frozen set
empty_fs = frozenset()
print("Empty Frozen Set:", empty_fs)   # Output: frozenset()