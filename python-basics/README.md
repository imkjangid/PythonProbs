<label title="Back to PythonProb">⬅️ <a href="https://github.com/imkjangid/PythonProbs">Back</a></label>

## **Python Comments**

Comments are an essential part of writing code, as they help explain what a program is doing. They provide valuable context and documentation for the source code, making it easier for developers to understand the program's logic, even after some time has passed.

In Python, you can add comments by using the hash (`#`) symbol. The comment will extend from the `#` symbol to the end of the line. Python's interpreter will ignore these comments and they are solely for the benefit of human readers.

See: [*<code>comments.py</code>*](https://github.com/imkjangid/PythonProbs/blob/main/python-basics/comments.py)

```python
# This is a comment

##################################
### This is decorative comment ###
##################################
```

Taking the time to add informative comments can greatly improve the maintainability and readability of your Python code. This is especially important when working on complex programs or collaborating with other developers.

## **Inline Comments**

Inline comments are comments that are placed directly on the same line as a statement. They begin with a single hash (#) sign, followed by a space, and then the comment.

For clarity, it's a good practice to separate the inline comment from the statement with at least two spaces.

```python
print("hello inline comment") # This is an inline comment
```

## Variables

A variable is a named container in computer memory used to store and hold data that can be changed during a program's execution. For readability, it's best practice to use mnemonic (easily remembered) names.

For example:
```python
name = "python"
```

The variable `name` is assigned the value `10`.

The value of variable can be replaced as per our requirement.

```python
name = "python"
name = "python programming"
```
The value of `name` was changed from `python` to `python programming`.

**NOTE:** Python variables are references to objects, not containers for values. An assignment operation simply points the variable's reference to the correct object in memory.

In Python, you don't need to declare a variable's type explicitly. Python is a dynamically typed language, which means it automatically determines the variable's type based on the value assigned to it.

### Variable Naming Rules
- **Start with a letter or underscore**: Names must begin with a letter (`A-z`) or an underscore (`_`).
- **Don't start with a number**: A variable name cannot start with a digit (`0-9`).
- **Use valid characters**: A variable name can only contain alphanumeric characters and underscores (`A-z`, `0-9`, and `_`).
- **Case-sensitive**: Names are case-sensitive. For example, `programming_name`, `Programming_name`, and `PROGRAMMING_NAME` are all treated as different variables.
- **Follow conventions**: It is recommended to use lowercase letters and underscores (snake_case) for variable names for better readability.

### Example of some valid variable names
```python
firstname = "your_first_name"
lastname = "your_last_name"
age = 30
country = "india"
city = "Ajmer"
first_name = "your_first_name"
last_name = "your_last_name"
capital_city = "Ajmer"
_if = "some value"       # if we want to use reserved word as a variable
year_2021
year2021
current_year_2021
birth_year = 2020
num1 = 10
num2 = 20
```

### Example of invalid names
```python
first-name = "xyz"

File "<python-input-0>", line 1
    first-name = "xyz"
    ^^^^^^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
```

```python
first@name = "xyz"

File "<python-input-1>", line 1
    first@name = "xyz"
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
```

```python
first$name = "xyz"

File "<python-input-2>", line 1
    first$name = "xyz"
         ^
SyntaxError: invalid syntax
```

```python
num-1 = 10

File "<python-input-3>", line 1
    num-1 = 10
    ^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
```

```python
1num = 10

File "<python-input-4>", line 1
    1num = 10
    ^
SyntaxError: invalid decimal literal
```

### Assigning values to Variables in Python
In Python, you assign values to variables using the equals sign (`=`). Unlike many other languages, you don't need to declare a variable's type, because Python is dynamically typed and infers the type from the assigned value. A variable is essentially a name that references an object in memory, not a container holding a value directly. 

See: [*<code>variables.py</code>*](https://github.com/imkjangid/PythonProbs/tree/main/python-basics/variables.py)
```python
# variable declaration
x = 5
y = "Hello"
z = 3.14

print(x)      # Output: 5
print(y)      # Output: Hello
print(z)      # Output: 3.14

# x, y, z also known as keywords in the case of variable declaration only
# but they are not reserved keywords in Python.

programming_name = "python"
print(programming_name)  # Output: python

age = 30
name = "XYZ"
price = 19.99
is_student = True

print(age)      # Output: 30
print(name)      # Output: XYZ
print(price)     # Output: 19.99
print(is_student)  # Output: True
```

### Multiple assignment

Python offers several efficient ways to assign multiple values at once. 

You can assign different values to different variables on a single line. The number of variables on the left must match the number of values on the right. 

```python
a, b, c = "Apple", "Banana", "Cherry"
```

### Assigning the same value to multiple variables

You can assign the same value to multiple variables in a chained assignment. 

```python
a, b, c = "Apple"
```

**NOTE**: This can have unintended side effects with mutable objects like lists. If you modify one of the variables, the others will also change because they all point to the same object in memory.

## Constants in Python

In programming, a constant is an identifier for a value that is immutable, meaning its value cannot be modified during program execution. Using constants improves code readability, prevents accidental data modification, and makes the program more maintainable.

Use all uppercase letters with underscores to separate words for constant variable names. This serves as a strong signal to other developers that the value should not be reassigned.

See: [*`constant-var.py`*](https://github.com/imkjangid/PythonProbs/tree/main/python-basics/constant-var.py)
```python
PI = 3.14159
MAX_CONNECTIONS = 1000
BACKGROUND_COLOR = "#FFFFFF"

# You can still reassign this, but you shouldn't by convention
PI = 3.14  # This will not cause an error
```

## Keywords and Identifiers

Keywords are the reserved words in Python so we cannot use a keyword as a **variable** name, **function** name or any other identifier. They are used to define the syntax and structure of the Python language.

In Python, keywords are **case sensitive**.

There are **36+** keywords in Python 3.9. This number can vary slightly over the course of time.

All the keywords except **`True`**, **`False`** and **`None`** are in lowercase and they must be written as they are. The **list of all the keywords** is given below.

**Keywords in Python**

|     |     |     |     |     |
|:----|:----|:----|:----|:----|
| **in** | **is** | **or** | **and** | **not** |
| **for** | **while** | **break** | **continue** | **pass** |
| **if** | **elif** | **else** | **async** | **await** |
| **def** | **local** | **global** | **return** | **yield** |
| **try** | **except** | **finally** | **raise** | **assert** |
| **from** | **import** | **as** | **class** | **with** |
| **del** | **local** | **nonlocal** | **global** | **lambda** |
| **True** | **False** | **None** |  | |


Code shown below, a variable created with using a `if` which is reserved word results in an **error**:

```python
if = "hello"
  File "<python-input-0>", line 1
    if = "hello"
       ^
SyntaxError: invalid syntax
```

## **Docstrings in Python**

A docstring is short for documentation string.

Python *Docstrings* (documentation strings) are the string literals that appear right after the definition of a function, method, class, or module.

Triple quotes (`"""` or `'''`) are used while writing docstrings.

See: [*<code>docstring.py</code>*](https://github.com/imkjangid/PythonProbs/blob/main/python-basics/docstring.py)
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