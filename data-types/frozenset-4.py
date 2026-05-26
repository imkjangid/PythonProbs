# Primary Mathematical Mathematic (Non-mutating)

set_a = frozenset([1, 2, 3])
set_b = frozenset([3, 4, 5])

# Operations always return a BRAND NEW frozenset object
print("\nUnion (A ∪ B):", set_a.union(set_b))                 # Output: frozenset({1, 2, 3, 4, 5})
print("Intersection (A ∩ B):", set_a.intersection(set_b))     # Output: frozenset({3})
print("Difference (A - B):", set_a.difference(set_b))         # Output: frozenset({1, 2})