# Tuple 'tp' have 3 elements
tp = (3,'hello', 3.1)
#   (0     1      2) ➡ Index forward

# index '0' is element '1'= 3
# index '1' is element '2'= hello
# index '2' is elemtnt '3'= 3.1

# tp[1] = 'hello'
print("t[1] = ", tp[1])

# tp[0:3] = (3, 'hello', 3.1)
print("tp[0:3] = ", tp[0:3])

# Generates error
# Tuples are immutable
tp[0] = 6  # trying to change element 0 from '3' to '6'