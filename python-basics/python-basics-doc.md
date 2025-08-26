**Python Comments**

Comments are an essential part of writing code, as they help explain what a program is doing. They provide valuable context and documentation for the source code, making it easier for developers to understand the program's logic, even after some time has passed.

In Python, you can add comments by using the hash (`#`) symbol. The comment will extend from the `#` symbol to the end of the line. Python's interpreter will ignore these comments and they are solely for the benefit of human readers.

See: *<code>comments-docstring.py</code>*
```python
# This is a comment

##################################
### This is decorative comment ###
##################################
```

Taking the time to add informative comments can greatly improve the maintainability and readability of your Python code. This is especially important when working on complex programs or collaborating with other developers.

**Inline Comments**

Inline comments are comments that are placed directly on the same line as a statement. They begin with a single hash (#) sign, followed by a space, and then the comment.

For clarity, it's a good practice to separate the inline comment from the statement with at least two spaces.

```python
print("hello inline comment") # This is an inline comment
```

**Docstrings in Python**

A docstring is short for documentation string.

Python *Docstrings* (documentation strings) are the string literals that appear right after the definition of a function, method, class, or module.

Triple quotes (`"""` or `'''`) are used while writing docstrings.

```python
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
    for class MyClass2."""
    pass
```

Docstrings appear right after the definition of a function, class, or module. It separates docstrings from multiline comments using triple quotes.

Docstrings are associated with objects as their `__doc__` attribute.

So, we can access the docstring of the above function with the following lines of code:

```python
print(my_function.__doc__)
print(my_function2.__doc__)
print(MyClass.__doc__)
print(MyClass2.__doc__)
```