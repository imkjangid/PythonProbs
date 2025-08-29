<label title="Back to PythonProb">⬅️ <a href="https://github.com/imkjangid/PythonProbs">Back</a></label>

# **Data Types**

In Python, every value is an object with a specific data type. These data types are defined by classes, and variables are instances of those classes.
Key aspects of Python data types:
* **Dynamic Typing**: Python automatically assigns the correct data type at runtime based on the value given to the variable.
* **Wide Variety**: Python includes a rich set of built-in types to handle different data, including numbers, text, and collections.

Some of the most important types are listed below.

<table border="1"><thead><th>Data Type</th><th colspan="2">Class Name</th><th>Mutablility</th></thead><tbody align="center"><tr><th rowspan="4">Numbers</th><td><tr><td>Integer</td><td>int</td><td>❌</td></tr><tr><td>Flaot</td><td>flaot</td><td>❌</td></tr><tr><td>Complex</td><td>complex</td><td>❌</td></tr></td></tr><tr><th rowspan="2">Texts</th><tr><td>String</td><td>str</td><td>❌</td></tr></tr><tr><th rowspan="2">Booleans</th><tr><td>Boolean</td><td>bool</td><td>❌</td></tr></tr><tr><th rowspan="2">NoneType</th><tr><td>None</td><td>NoneType</td><td>❌</td></tr></tr><tr><th rowspan="5">Collection</th><tr><td>List</td><td>list</td><td>✅</td></tr><tr><td>Tuple</td><td>tuple</td><td>❌</td></tr><tr><td>Dictionary</td><td>dict</td><td>✅</td></tr><tr><td>Set</td><td>set</td><td>✅</td></tr></tr></tbody></table>

## Numbers
Python's `numbers` category includes integers (`int`), floating-point numbers (`float`), and complex numbers (`complex`). To identify the specific class a variable or value belongs to, use the `type()` function. For checking if an object is an instance of a particular class or its subclasses, use the `isinstance()` function.

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

```python
a = 1234567890123456789
print (a)

b = 0.1234567890123456789  # total of only 17 numbers after decimal can be printed.
print (b)

c = 1+2j
print (c)
```

Notice that the value of the float variable `b` was truncated.

## Text (String)

In Python, a string is an immutable sequence of Unicode characters. String literals can be expressed using single quotes, double quotes, or triple quotes.
- **Single and Double Quotes**: Both are functionally equivalent for creating single-line strings.
- **Triple Quotes (`'''` or `"""`)**: Used to define multi-line strings, which can span multiple lines and include newlines and other special characters.

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

```python
mystring = "This is a string"  # mystring is my variable
print(mystring)
multiline_string = '''A multiline
string'''
print(multiline_string)
```

The slicing operator (`[]`) can be used to extract items from strings, just as with lists and tuples. However, strings are immutable, meaning their elements cannot be changed after creation.

```python
mystring = 'Hello world' # total 12 elements. Index start from '0' to '10'

# mystring[4] = 'o'
print("mystring[4] = ", mystring[4])

# mystring[6:10] = 'world' # index '6' to '10' means element from 6 to 10
print("mystring[6:10] = ", mystring[6:10])
```

**NOTE**: Strings cannot be modified after they are created as string is `immutable`.

## Python List

Lists in Python are `mutable`, ordered collections of items. As a highly flexible data structure, a single list can contain elements of varying data types. Lists are created by enclosing comma-separated values within square brackets (`[]`).

```python
a = [2, 2.1, 'python']
print(a)
```

You can extract a single item or a range of items from a list using the slicing operator (`[]`). Since Python uses zero-based indexing, the first item is at index `0`.

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

## Tuple

A tuple is an ordered, immutable sequence of items. Like lists, tuples can contain heterogeneous data and are created by enclosing a comma-separated sequence of items within parentheses (`()`). The key distinction is that once a tuple is created, its contents cannot be modified. Due to their static nature, tuples are often faster and are used for "write-protecting" data.

```python
tp = (3,'hello', 3.1)
```

### *Tuples vs. Lists*
- Tuples are like lists, but with one key difference: they are `immutable`, meaning you cannot change their contents after they are created.
- This immutability makes tuples useful for data that should not be altered. It also makes them faster than lists for certain operations.


While the slicing operator (`[]`) can be used to extract items from a tuple, it is not possible to alter their values, as tuples are immutable. See example below:

```python
# Tuple 'tp' have 3 elements
tp = (3,'hello', 3.1)
#   (0     1      2) ➡ Index forward

# index '0' is element '1'= 3
# index '1' is element '2'= hello
# index '2' is elemtnt '3'= 3.1

# tp[1] = 'hello'
print("t[1] = ", t[1])

# tp[0:3] = (3, 'hello', 3.1)
print("tp[0:3] = ", t[0:3])

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

```python
mylist =  [3, 'hello', 2.1]  # list
mytuple = (3, 'hello', 2.1)  # tuple

mylist[1] = 'python'  # List is mutable
print(mylist)         # No error here

mytuple[1]= 'python'  # Tuple is immutable
print(mytuple)        # error will be raised as show in previous example
```