a = [5, 10, 15, 20, 25, 30, 35, 40]  # Total elemnets is 8
#   [0   1   2   3   4   5   6   7]  ⬅ Index forward
#   [-8 -7  -6  -5  -4  -3  -2  -1]  ➡ Index backward

# index '0' is element '1' = 5,
# index '1' is element '2' = 10,
# index '2' is element '3' = 15,
# .
# .
# .
# index '7' is element '8' = 40,

a[1] # To access the elements in the list

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])  # [0:3] means elements from 0 uptil 2 index (not include last element)
                            # [0:3] means from index 0 to 3 - 1
                            # [0:3] means from index 0 to 2

# a[5:] = [30, 35, 40]  # [5:] means all the elements from 5 till end
print("a[5:] = ", a[5:])