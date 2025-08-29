mylist =  [3, 'hello', 2.1]  # list
mytuple = (3, 'hello', 2.1)  # tuple

mylist[1] = 'python'  # List is mutable
print(mylist)         # No error here

mytuple[1]= 'python'  # Tuple is immutable
print(mytuple)        # error will be raised as show in previous example