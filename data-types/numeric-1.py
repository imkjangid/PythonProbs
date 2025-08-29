a = 5
print(a, "is of type", type(a))
print(a, "is integer number?", isinstance(5,int))

a = 2.0
print(a, "is of type", type(a))
print(a, "is float number?", isinstance(2.0,float))

a = 2+3j  # '2' is real part and '3j' is imaginary part
print(a, "is of type", type(a))
print(a, "is complex number?", isinstance(2+3j,complex))