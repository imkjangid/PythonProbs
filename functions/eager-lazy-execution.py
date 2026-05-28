import sys

# Data target matrix boundary size
data_range = range(100000)

# Eager Execution: Immediately builds a 100,000 item list inside RAM
eager_list = [x * 2 for x in data_range]

# Lazy Execution: Only saves a memory pipeline instruction pointer map
lazy_map_stream = map(lambda x: x * 2, data_range)

print(f"RAM footprint for Eager List Array: {sys.getsizeof(eager_list)} bytes.")
print(f"RAM footprint for Lazy Map Stream:  {sys.getsizeof(lazy_map_stream)} bytes.")
# Note: The lazy stream object consumes almost zero bytes regardless of the dataset size!