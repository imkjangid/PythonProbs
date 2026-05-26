# Immutability Demonstration (Read-Only)

sample_fs = frozenset([1, 2, 3])
# Frozen sets DO NOT have methods like .add(), .remove(), or .pop()
sample_fs.add(4) # Will raise AttributeError: 'frozenset' object has no attribute 'add'

sample_fs.clear() # Will raise AttributeError: 'frozenset' object has no attribute 'clear'