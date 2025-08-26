'''This is docstring for module docstring.py'''

"""This is another docstring with double quotes for module docstring.py"""

'''This is multi-line docstring
with single quotes for module docstring.py'''

"""This is multi-line docstring
with double quotes for module docstring.py"""

def my_function():
    """This is a docstring for function my_function."""
    pass

def my_function2():
    """This is a multi-line docstring
    for function my_function2."""
    pass

class MyClass:
    """This is a docstring for class MyClass."""
    pass

class MyClass2:
    """This is a multi-line docstring
    for class MyClass."""
    pass

print(my_function.__doc__)
print(my_function2.__doc__)
print(MyClass.__doc__)
print(MyClass2.__doc__)