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

<table border=1><thead><th>Data Type<th colspan=2>Class Name<th>Mutablility<th>Category<th>Hashable<th>Core Use Case<tbody align=center><tr><th rowspan=4>Numbers<td><tr><td>Integer<td>int<td>❌<td>Numeric<td>✅<td rowspan=2>Mathematical computations & counters.<tr><td>Flaot<td>flaot<td>❌<td>Numeric<td>✅<tr><td>Complex<td>complex<td>❌<td>Numeric<td>✅<td>2D coordinate geometry, physics simulation, electrical engineering math.<tr><th rowspan=2>Texts<tr><td>String<td>str<td>❌<td>Sequence<td>✅<td>Text representation & string manipulation.<tr><th rowspan=2>Booleans<tr><td>Boolean<td>bool<td>❌<td>Numeric (0, 1)<td>✅<td>Conditional branching, flags, and logic evaluation gateways.<tr><th rowspan=2>NoneType<tr><td>None<td>NoneType<td>❌<td>Singleton<td>✅<td>Placeholder for missing data, default function returns, and state resets.<tr><th rowspan=6>Collection<tr><td>List<td>list<td>✅<td>Sequence<td>❌<td>Ordered collections where items change frequently.<tr><td>Tuple<td>tuple<td>❌<td>Sequence<td>✅<td>Fixed, read-only ordered structures (Data integrity).<tr><td>Dictionary<td>dict<td>✅<td>Mapping<td>❌<td>Fast key-value lookups (<i>O</i>(1) complexity).<tr><td>Set<td>set<td>✅<td>Set Types<td>❌<td>Unordered unique elements, mathematical set math.<tr><td>Frozen Set<td>frozenset<td>❌<td>Set Types<td>❌<td>Immutable unique collection; usable as dict keys/nested sets.</table>

## Numbers
Python's `numbers` category includes integers (`int`), floating-point numbers (`float`), and complex numbers (`complex`). To identify the specific class a variable or value belongs to, use the `type()` function. For checking if an object is an instance of a particular class or its subclasses, use the `isinstance()` function.

See: [`numeric-1.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/numeric-1.py)
```python
a = 5
print(a, "is of type", type(a)) # Output: <class 'int'>
print(a, "is integer number?", isinstance(5,int)) # Output: True

a = 2.0
print(a, "is of type", type(a)) # Output: <class 'float'>
print(a, "is float number?", isinstance(2.0,float)) # Output: True

a = 2+3j  # '2' is real part and '3j' is imaginary part
print(a, "is of type", type(a)) # Output: <class 'complex'>
print(a, "is complex number?", isinstance(2+3j,complex)) # Output: True
```

- **Integers**: Can be of any length and are only limited by available memory.
- **Floating-Point Numbers**: Accurate up to approximately `15 decimal places`. They are separated from integers by a decimal point (e.g., `1` is an `integer`, while `1.0` is a `float`).
- **Complex Numbers**: Written in the form `x + yj`, where `x` is the real part and `yj` is the imaginary part.

See: [`numeric-2.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/numeric-2.py)
```python
a = 1234567890123456789
print (a) # Output: 1234567890123456789

b = 0.1234567890123456789  # total of only 17 numbers after decimal can be printed.
print (b) # Output: 0.12345678901234568

c = 1+2j
print (c) # Output: (1+2j)
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
print(mystring) # Output: Hello World 1
mystring = """Hello World 2"""
print(mystring) # Output: Hello World 2
mystring = 'Hello World 3'
print(mystring) # Output: Hello World 3
mystring = "Hello World 4"
print(mystring) # Output: Hello World 4
mystring = Hello World 5  # cannot write string without quotes ('', " ", """ """, ''' ''')
print(mystring) # Output: NameError: name 'Hello World 5' is not defined
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
print("mystring[4] = ", mystring[4]) # Output: 'o'

# mystring[6:10] = 'world' # index '6' to '10' means element from 6 to 10
print("mystring[6:10] = ", mystring[6:10]) # Output: 'world'
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
print("a[2] = ", a[2]) # Output: 15

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])  # Output: [5, 10, 15]

# a[5:] = [30, 35, 40]  # [5:] means all the elements from 5 till end
print("a[5:] = ", a[5:]) # Output: [30, 35, 40]
```

**NOTE**: Lists are `mutable`, which simply means you can change the items inside a list after you've made it.

### Tuple

A tuple is an ordered, immutable sequence of items. Like lists, tuples can contain heterogeneous data and are created by enclosing a comma-separated sequence of items within parentheses (`()`). The key distinction is that once a tuple is created, its contents cannot be modified. Due to their static nature, tuples are often faster and are used for "write-protecting" data.

See: [`tuple-1.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/tuple-1.py)
```python
tp = (3,'hello', 3.1)
print(tp) # Output: (3, 'hello', 3.1)
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
print("tp[1] = ", tp[1]) # Output: hello

# tp[0:3] = (3, 'hello', 3.1)
print("tp[0:3] = ", tp[0:3]) # Output: (3, 'hello', 3.1)

# Generates error
# Tuples are immutable
tp[0] = 6  # Output: TypeError: 'tuple' object does not support item assignment
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
print(mylist)         # Output: [3, 'python', 2.1]

mytuple[1]= 'python'  # Tuple is immutable
print(mytuple)        # Output: TypeError: 'tuple' object does not support item assignment
```

### Sets

A set is an unordered and mutable collection of unique, hashable items. Sets are defined by enclosing a comma-separated sequence of values within curly braces (`{}`). Because they are unordered, items within a set cannot be accessed by index and duplicates items removed automatically

See: [`set-1.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/set-1.py)
```python
myset = {6,4,7,8,4}

# printing set variable
print("myset = ", myset) # Output: {4, 6, 7, 8}

# data type of variable myset
print(type(myset)) # Output: <class 'set'>
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

### Frozen Sets

A *`frozenset`* is a built-in data type in Python that represents an immutable version of a standard set defined by *`frozenset([ele1, ele2])`*. While elements in a regular set can be added or removed at runtime , a frozenset cannot be modified after it is created.

See: [`frozenset-1.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/frozenset-1.py)
1. Initialization & Type Checking
```python
# Creating a frozen set from a list
fs1 = frozenset([10, 20, 30, 40, 20]) # Duplicates (20) are automatically removed
print("Frozen Set 1:", fs1)           # Output: frozenset({40, 10, 20, 30})
print("Data Type:", type(fs1))        # Output: <class 'frozenset'>

# Creating a frozen set from a string
fs_str = frozenset("kapil")
print("Frozen Set from String:", fs_str) # Output: Unique unordered characters

# Creating an empty frozen set
empty_fs = frozenset()
print("Empty Frozen Set:", empty_fs)   # Output: frozenset()
```

2. Immutability Demonstration (Read-Only)
```python
sample_fs = frozenset([1, 2, 3])
# Frozen sets DO NOT have methods like .add(), .remove(), or .pop()
sample_fs.add(4) # Will raise AttributeError: 'frozenset' object has no attribute 'add'

sample_fs.clear() # Will raise AttributeError: 'frozenset' object has no attribute 'clear'
```
3. Membership Testing
```python
tech_stack = frozenset(["Python", "Django", "Flask"])

# Checking if an item exists inside the frozen set (O(1) Complexity)
print("\nIs Python present?:", "Python" in tech_stack)   # Output: True
print("Is Salesforce present?:", "Salesforce" in tech_stack) # Output: False
```

4. Primary Mathematical Mathematic (Non-mutating)
```python
set_a = frozenset([1, 2, 3])
set_b = frozenset([3, 4, 5])

# Operations always return a BRAND NEW frozenset object
print("\nUnion (A ∪ B):", set_a.union(set_b))                 # Output: frozenset({1, 2, 3, 4, 5})
print("Intersection (A ∩ B):", set_a.intersection(set_b))     # Output: frozenset({3})
print("Difference (A - B):", set_a.difference(set_b))         # Output: frozenset({1, 2})
```

### Dictionary

A dictionary is a mutable collection of key-value pairs, where each key maps to a corresponding value. Dictionaries are optimized for efficient data retrieval when the key is known, making them suitable for handling large datasets. In Python, dictionaries are defined by enclosing comma-separated *`key:value`* pairs within curly braces (`{}`), where both keys and values can be of any type.

See: [`dictionary-1.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/dictionary-1.py)
```python
mydict = {1: 'One', 2: 'Two', 3: 'Three'}  # 'One' is a value while 1 is the key of an element.
print(mydict, type(mydict))

print(mydict[3]) # Output: Three
```

Accessing Dictionary Values
- **Use the key**: To get a value from a dictionary, you must provide its associated key.
- **One-way lookup**: You cannot use a value to find its key. This makes the lookup process very fast.

See: [`dictionary-2.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/dictionary-2.py)
```python
mydict = {1:'value','key':2} # '1' is the key to access 'value' and 'key' is the key to access '2'
print(type(mydict))

print("mydict[1] = ", mydict[1]); # Output: value

print("mydict['key'] = ", mydict['key']);  # Output: 2
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