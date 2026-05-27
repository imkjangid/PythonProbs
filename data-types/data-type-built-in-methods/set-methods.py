# ==========================================
# SET MATHEMATICS & COMPONENT TESTING
# ==========================================
set_alpha = {1, 2, 3, 4}
set_beta = {3, 4, 5, 6}

# Non-mutating methods returning a new set object
print("Union Result:", set_alpha.union(set_beta))                 # Output: {1, 2, 3, 4, 5, 6}
print("Intersection Result:", set_alpha.intersection(set_beta)) # Output: {3, 4}

# Mutating operations
set_alpha.add(99)
print("Set Alpha after adding element:", set_alpha)

# Discard vs Remove safety check
set_alpha.discard(100) # Safe: Does nothing if element is missing
print("Discard execution passed without crashing.")