<div title="Back to Home" style="float:left;padding:10px 0;">
    Navigation: 
    <label>⬅️ <a href="https://github.com/imkjangid/PythonProbs">Back to Home</a></label>
    <label title="Python Basics">📁 <a href="https://github.com/imkjangid/PythonProbs/tree/main/python-basics/">Python Basics</a><label>
    <label title="Showing Data Types">📂 <span style="border-bottom: #06d solid 3px;">Data Types</span></label>
</div>
<br>
<br>

# **Data Types**

In Python, every value is an object with a specific data type. These data types are defined by classes, and variables are instances of those classes.
Key aspects of Python data types:
* **Dynamic Typing**: Python automatically assigns the correct data type at runtime based on the value given to the variable.
* **Wide Variety**: Python includes a rich set of built-in types to handle different data, including numbers, text, and collections.

Some of the most important types are listed below.

<table border="1"><thead><th>Data Type</th><th colspan="2">Class Name</th><th>Mutablility</th></thead><tbody align="center"><tr><th rowspan="4">Numbers</th><td><tr><td>Integer</td><td>int</td><td>❌</td></tr><tr><td>Flaot</td><td>flaot</td><td>❌</td></tr><tr><td>Complex</td><td>complex</td><td>❌</td></tr></td></tr><tr><th rowspan="2">Texts</th><tr><td>String</td><td>str</td><td>❌</td></tr></tr><tr><th rowspan="2">Booleans</th><tr><td>Boolean</td><td>bool</td><td>❌</td></tr></tr><tr><th rowspan="2">NoneType</th><tr><td>None</td><td>NoneType</td><td>❌</td></tr></tr><tr><th rowspan="5">Collection</th><tr><td>List</td><td>list</td><td>✅</td></tr><tr><td>Tuple</td><td>tuple</td><td>❌</td></tr><tr><td>Dictionary</td><td>dict</td><td>✅</td></tr><tr><td>Set</td><td>set</td><td>✅</td></tr></tr></tbody></table>

## Numbers
Python's `numbers` category includes integers (`int`), floating-point numbers (`float`), and complex numbers (`complex`). To identify the specific class a variable or value belongs to, use the `type()` function. For checking if an object is an instance of a particular class or its subclasses, use the `isinstance()` function.

See: [`numeric-1.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/numeric-1.py)
```python
a = 5
print(a, "is of type", type(a))
print(a, "is integer number?", isinstance(5,int))

a = 2.0
print(a, "is of type", type(a))
print(a, "is float number?", isinstance(2.0,float))

a = 2+3j  # '2' is real part and '3j' is imaginary part
print(a, "is of type", type(a))
print(a, "is complex number?", isinstance(2+3j,complex))
```

- **Integers**: Can be of any length and are only limited by available memory.
- **Floating-Point Numbers**: Accurate up to approximately `15 decimal places`. They are separated from integers by a decimal point (e.g., `1` is an `integer`, while `1.0` is a `float`).
- **Complex Numbers**: Written in the form `x + yj`, where `x` is the real part and `yj` is the imaginary part.

See: [`numeric-2.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/numeric-2.py)
```python
a = 1234567890123456789
print (a)

b = 0.1234567890123456789  # total of only 17 numbers after decimal can be printed.
print (b)

c = 1+2j
print (c)
```

Notice that the value of the float variable `b` was truncated.

## Boolean

The boolean (`bool`) data type in Python represents logical values, which are limited to either True or False. As a cornerstone of conditional logic, booleans are the result of many comparison and logical operations, and are critical for controlling program flow.

See: [`boolean-type.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/boolean-type.py)
```python
a = True
b = False
print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False
```

#### Truthy and Falsy Values
In Python, every value has a "*truthiness*" that determines how it behaves in a boolean context, like an if statement.
- **Falsy Values**: The following values are treated as False. You can confirm this with the bool() function.
    - False, None
    - The number zero (`0`, `0.0`, `0j`)
    - Empty sequences (`""`, `[]`, `()`)
    - Empty collections (`{}`, `set()`, `range(0)`)
- **Truthy Values**: All other values are considered `True` in a boolean context.

### NoneType

The `NoneType` is the single data type for the special constant `None` in Python. `None` is an object that represents a null value or the absence of a value, often used as a sentinel to indicate that a variable has no assigned data or that an operation has not returned a result.

#### Key Characteristics of the `None` Object
- **Singleton**: There is only one `None` object in a Python program. When you assign `None` to different variables, they all point to this same object.
- **Case-sensitive**: Always write `None` with a capital "`N`." Using lowercase `none` will cause an error.
- **Distinct**: `None` is a unique value. It is not equivalent to `0`, an empty string (`""`), or `False`.

See: [`none-type.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/none-type.py)

```python
none_object = None
print(none_object) # Output: None
print(type(none_object))  # Output: <class 'NoneType'>
```

## Text (String)

In Python, a string is an immutable sequence of Unicode characters. String literals can be expressed using single quotes, double quotes, or triple quotes.
- **Single and Double Quotes**: Both are functionally equivalent for creating single-line strings.
- **Triple Quotes (`'''` or `"""`)**: Used to define multi-line strings, which can span multiple lines and include newlines and other special characters.

See: [`string-1.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/string-1.py)
```python
mystring = '''Hello World 1'''
print(mystring)
mystring = """Hello World 2"""
print(mystring)
mystring = 'Hello World 3'
print(mystring)
mystring = "Hello World 4"
print(mystring)
mystring = Hello World 5  # cannot write string without quotes ('', " ", """ """, ''' ''')
print(mystring)
```

See: [`string-2.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/string-2.py)
```python
mystring = "This is a string"  # mystring is my variable
print(mystring)
multiline_string = '''A multiline
string'''
print(multiline_string)
```

The slicing operator (`[]`) can be used to extract items from strings, just as with lists and tuples. However, strings are immutable, meaning their elements cannot be changed after creation.

See: [`string-slice.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/string-slice.py)
```python
mystring = 'Hello world' # total 12 elements. Index start from '0' to '10'

# mystring[4] = 'o'
print("mystring[4] = ", mystring[4])

# mystring[6:10] = 'world' # index '6' to '10' means element from 6 to 10
print("mystring[6:10] = ", mystring[6:10])
```

**NOTE**: Strings cannot be modified after they are created as string is `immutable`.

## Collection
A Python collection is a container data type that stores a group of objects. The language provides several built-in collection types—including lists, tuples, sets, and dictionaries—that are distinguished by their behavior regarding order, mutability, and element access.

### Python List

Lists in Python are `mutable`, ordered collections of items. As a highly flexible data structure, a single list can contain elements of varying data types. Lists are created by enclosing comma-separated values within square brackets (`[]`).

See: [`list-1.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/list-1.py)
```python
a = [2, 2.1, 'python']
print(a)
```

You can extract a single item or a range of items from a list using the slicing operator (`[]`). Since Python uses zero-based indexing, the first item is at index `0`.

See: [`list-index-slice.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/list-index-slice.py)
```python
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
```

**NOTE**: Lists are `mutable`, which simply means you can change the items inside a list after you've made it.

### Tuple

A tuple is an ordered, immutable sequence of items. Like lists, tuples can contain heterogeneous data and are created by enclosing a comma-separated sequence of items within parentheses (`()`). The key distinction is that once a tuple is created, its contents cannot be modified. Due to their static nature, tuples are often faster and are used for "write-protecting" data.

See: [`tuple-1.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/tuple-1.py)
```python
tp = (3,'hello', 3.1)
print(tp)
```

#### *Tuples vs. Lists*
- Tuples are like lists, but with one key difference: they are `immutable`, meaning you cannot change their contents after they are created.
- This immutability makes tuples useful for data that should not be altered. It also makes them faster than lists for certain operations.


While the slicing operator (`[]`) can be used to extract items from a tuple, it is not possible to alter their values, as tuples are immutable. See example below:

See: [`tuple-index.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/tuple-index.py)
```python
# Tuple 'tp' have 3 elements
tp = (3,'hello', 3.1)
#   (0     1      2) ➡ Index forward

# index '0' is element '1'= 3
# index '1' is element '2'= hello
# index '2' is elemtnt '3'= 3.1

# tp[1] = 'hello'
print("tp[1] = ", tp[1])

# tp[0:3] = (3, 'hello', 3.1)
print("tp[0:3] = ", tp[0:3])

# Generates error
# Tuples are immutable
tp[0] = 6  # trying to change element 0 from '3' to '6'
```

As the result of above code

<pre>
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-0-c92d923bad3> in <module>
     15 # Generates error
     16 # Tuples are immutable
---> 17 tp[0] = 6  # trying to change element 0 from '3' to '6'

TypeError: 'tuple' object does not support item assignment
</pre>

Try the following code:

See: [`tuple-vs-list.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/tuple-vs-list.py)
```python
mylist =  [3, 'hello', 2.1]  # list
mytuple = (3, 'hello', 2.1)  # tuple

mylist[1] = 'python'  # List is mutable
print(mylist)         # No error here

mytuple[1]= 'python'  # Tuple is immutable
print(mytuple)        # error will be raised as show in previous example
```

### Sets

A set is an unordered and mutable collection of unique, hashable items. Sets are defined by enclosing a comma-separated sequence of values within curly braces (`{}`). Because they are unordered, items within a set cannot be accessed by index.

See: [`set-1.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/set-1.py)
```python
myset = {6,4,7,8,4}

# printing set variable
print("myset = ", myset)

# data type of variable myset
print(type(myset))
```

Due to their unordered nature, sets do *not support `indexing`*, and therefore, the slicing operator (`[]`) is not applicable.

See: [`set-2.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/set-2.py)
```python
myset = {1,2,3}  # Elements in a set cannot be accessed by index because a set is an unordered collection.
myset[1]  # it will raise an error
```

<pre>
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-234b76ef2a87> in <module>
      1 a = {1,2,3}  # Elements in a set cannot be accessed by index because a set is an unordered collection.
----> 2 a[1]  # it will raise an error

TypeError: 'set' object is not subscriptable
</pre>

Sets allow you to perform common mathematical operations like `union` and `intersection`. A key characteristic of sets is that they only contain unique elements, which automatically eliminates duplicates.

See: [`set-3.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/set-3.py)
```python
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Using the union() method
union_set_method = set_a.union(set_b)
print(f"Union (method): {union_set_method}")

# Using the intersection() method
intersection_set_method = set_a.intersection(set_b)
print(f"Intersection (method): {intersection_set_method}")
```

### Dictionary

A dictionary is a mutable collection of key-value pairs, where each key maps to a corresponding value. Dictionaries are optimized for efficient data retrieval when the key is known, making them suitable for handling large datasets. In Python, dictionaries are defined by enclosing comma-separated *`key:value`* pairs within curly braces (`{}`), where both keys and values can be of any type.

See: [`dictionary-1.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/dictionary-1.py)
```python
mydict = {1: 'One', 2: 'Two', 3: 'Three'}  # 'One' is a value while 1 is the key of an element.
print(mydict, type(mydict))

print(mydict[3])
```

Accessing Dictionary Values
- **Use the key**: To get a value from a dictionary, you must provide its associated key.
- **One-way lookup**: You cannot use a value to find its key. This makes the lookup process very fast.

See: [`dictionary-2.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/dictionary-2.py)
```python
mydict = {1:'value','key':2} # '1' is the key to access 'value' and 'key' is the key to access '2'
print(type(mydict))

print("mydict[1] = ", mydict[1]); # try to find the element from key.

print("mydict['key'] = ", mydict['key']);  # try to find the key from the element.
```

### Data Typecasting

Type casting, or type conversion, is the process of changing the data type of a value. Python supports two types of conversion:

#### Implicit Conversion
- **Automatic**: Handled automatically by the interpreter.
- **Purpose**: Prevents data loss during operations between compatible data types.
- **Mechanism**: Python converts a lower-hierarchy data type to a higher-hierarchy one (e.g., `int` to `float`).

See: [`implicit-typecasting.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/implicit-typecasting.py)
```python
# Implicit typecasting

num_int = 10
num_float = 5.5

# Implicit conversion occurs here; num_int is converted to a float
result = num_int + num_float

print(result)
print(type(result))  # Output: <class 'float'>
```

#### Explicit Conversion (Manual Casting)
- **Manual process**: Performed by the programmer using built-in functions.
- **Control**: Offers precise control over the conversion.
- **Risk**: Can result in data loss (e.g., converting a float to an int truncates the decimal).
- **Classes**: int(), float(), str(), list(), tuple(), set().

See: [`explicit-typecasting.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/explicit-typecasting.py)
```python
# Explicit typecasting

# float to int
my_float = 9.81
my_int = int(my_float)  # Truncates the decimal part
print(my_int) # Output: 9

# str to int
my_str_num = "42"
my_int_from_str = int(my_str_num)
print(my_int_from_str + 1) # Output: 43

# int to str
my_int_val = 123
my_str_val = str(my_int_val)
print("The number is " + my_str_val) # Output: The number is 123
```