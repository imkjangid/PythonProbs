# ==========================================
# IMMUTABLE FROZEN SET COMPONENT METHODS
# ==========================================
fs_network_a = frozenset([80, 443, 8080])
fs_network_b = frozenset([443, 22, 21])

# A. Checking overlapping boundaries using Boolean Methods
# .isdisjoint() returns True if there is zero intersection
print("Are networks entirely disjoint?:", fs_network_a.isdisjoint(fs_network_b)) # Output: False (443 is common)

# Checking subset/superset constraints
fs_sub = frozenset([80, 443])
print("Is fs_sub a subset of network_a?:", fs_sub.issubset(fs_network_a)) # Output: True

# B. Copying references securely
# Using .copy() on a frozenset behaves differently than mutable collections
fs_copy = fs_network_a.copy()
print("Are original and copy the exact same object reference?:", fs_network_a is fs_copy) # Output: True!