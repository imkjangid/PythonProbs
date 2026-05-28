<div title="Back to Home" style="float:left;padding:10px 0;">
    Navigation: 
    <label>⬅️ <a href="https://github.com/imkjangid/PythonProbs">Back to Home</a></label>
    <label title="Python Basics">📁 <a href="https://github.com/imkjangid/PythonProbs/tree/main/python-basics/">Python Basics</a><label>
    <label title="Data Types">📁 <a href="https://github.com/imkjangid/PythonProbs/tree/main/data-types/">Data Types</a><label>
    <label title="Showing Operators">📂 <span style="border-bottom: #06d solid 3px;">Operators</span></label>
    <label title="Control Flow">📂 <a href="https://github.com/imkjangid/PythonProbs/tree/main/control-flow/">Control Flow</a></label>
    <label title="Showing Functions">📂 <a href="https://github.com/imkjangid/PythonProbs/tree/main/functions/">Functions</a></label>
</div>
<br>
<br>

# **Operators**

Operators are special symbols in Python used to perform operations on values and variables (operands). Python categorizes operators based on their functionality: Arithmetic, Comparison, Logical, Assignment, Bitwise, and Special Identity/Membership operators.

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; text-align: left;">
    <thead>
        <tr>
            <th style="padding: 10px; font-size: 16px;">#</th>
            <th style="padding: 10px; font-size: 16px;">Operator Category</th>
            <th style="padding: 10px; font-size: 16px;">Symbols</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="font-weight: bold; padding: 8px; vertical-align: top;">1.</td>
            <td style="font-weight: bold; padding: 8px; vertical-align: top;">Arithmetic</td>
            <td style="padding: 8px; letter-spacing: 5px;">+ , - , * , / , // , % , **</td>
        </tr>
        <tr>
            <td style="font-weight: bold; padding: 8px; vertical-align: top;">2.</td>
            <td style="font-weight: bold; padding: 8px; vertical-align: top;">Comparison</td>
            <td style="padding: 8px; letter-spacing: 5px;">== , != , &gt; , &lt; , &gt;= , &lt;=</td>
        </tr>
        <tr>
            <td style="font-weight: bold; padding: 8px; vertical-align: top;">3.</td>
            <td style="font-weight: bold; padding: 8px; vertical-align: top;">Logical</td>
            <td style="padding: 8px; letter-spacing: 5px;">and , or , not</td>
        </tr>
        <tr>
            <td style="font-weight: bold; padding: 8px; vertical-align: top;">4.</td>
            <td style="font-weight: bold; padding: 8px; vertical-align: top;">Assignment</td>
            <td style="padding: 8px; letter-spacing: 5px;">= , += , -= , *= , /= , //= , %= , **=</td>
        </tr>
        <tr>
            <td style="font-weight: bold; padding: 8px; vertical-align: top;">5.</td>
            <td style="font-weight: bold; padding: 8px; vertical-align: top;">Identity</td>
            <td style="padding: 8px; letter-spacing: 5px;">is , is not</td>
        </tr>
        <tr>
            <td style="font-weight: bold; padding: 8px; vertical-align: top;">6.</td>
            <td style="font-weight: bold; padding: 8px; vertical-align: top;">Membership</td>
            <td style="padding: 8px; letter-spacing: 5px;">in , not in</td>
        </tr>
        <tr>
            <td style="font-weight: bold; padding: 8px; vertical-align: top;">7.</td>
            <td style="font-weight: bold; padding: 8px; vertical-align: top;">Bitwise</td>
            <td style="padding: 8px; letter-spacing: 5px;">&amp; , | , ^ , ~ , &lt;&lt; , &gt;&gt;</td>
        </tr>
    </tbody>
</table>

### 1. Arithmetic Operators
Behavioral Description: These operators perform standard mathematical calculations on numeric data types (`int`, `float`, `complex`). When a division operation (`/`) is performed, Python automatically casts the result to a float, even if the numbers divide evenly. Floor division (`//`) rounds the result down to the nearest whole integer towards minus infinity, while the modulo operator (`%`) calculates the true remainder of a division.

See: [`arithmetic-operators.py`](https://github.com/imkjangid/PythonProbs/blob/main/operators/arithmetic-operators.py)

```python
# Arithmetic Behavior
x = 5
y = 6

print("Addition (+):", x + by)          # Output: 19
print("Standard Division (/) always returns float:", x / y)   # Output: 3.4
print("Floor Division (//) truncates down:", x // y) # Output: 3
print("Modulo (%) returns remainder:", x % y)         # Output: 2
print("Exponentiation (**):", x ** 3)   # Output: 3375 (15 raised to power 3)
```

### 2. Comparison Operators
Comparison operators evaluate the relational value between two operands and always return a strict boolean value (`True` or `False`). They are natively chained in Python from left to right (e.g., `a < b < c`). Relational comparisons are valid across numeric values and sequences (like strings, where they compare lexicographical ASCII/Unicode values), but will throw a `TypeError` if you attempt to compare unordered mismatched types like a string and an integer.

See: [`comparison-operators.py`](https://github.com/imkjangid/PythonProbs/blob/main/operators/comparison-operators.py)

```python
# Comparison Behavior
char_a = "apple"
char_b = "banana"

# Lexicographical comparison (ASCII evaluation)
print("Is 'apple' less than 'banana'?:", char_a < char_b)  # Output: True
print("Numeric Equality check (10 == 10.0):", 10 == 10.0) # Output: True
```

### 3. Logical Operators
Used to combine conditional expressions. They operate based on lazy **Short-Circuit Evaluation**. In an `and` expression, if the left operand evaluates to `False`, the entire expression instantly returns `False` without checking the right operand. In an `or` expression, if the left operand is `True`, it instantly returns `True` and bypasses the remaining evaluations.

See: [`logical-operators.py`](https://github.com/imkjangid/PythonProbs/blob/main/operators/logical-operators.py)

```python
# Logical chaining
is_admin = True
has_valid_token = False

# Evaluates both paths unless short-circuiting triggers
print("Logical AND gateway:", is_admin and has_valid_token) # Output: False
print("Logical NOT inversion:", not has_valid_token)       # Output: True
```

### 4. Assignment Operators
Assignment operators bind a value or an expression's evaluated result to a variable name variable token. Compound assignment operators (like `+=`, `-=`, `*=`) evaluate the right-hand expression first, perform the respective mathematical operation with the current value of the left-hand variable, and reassign the final outcome back to that variable in a single operational step.

See: [`assignment-operators.py`](https://github.com/imkjangid/PythonProbs/blob/main/operators/assignment-operators.py)

```python
# Assignment Behavior
counter = 10
step_factor = 5

# Evaluates: counter = counter + step_factor
counter += step_factor 
print("Updated Counter Value:", counter) # Output: 15
```

### 5. Identity Operators
Instead of checking value equality, identity operators (`is`, `is not`) check whether two distinct variable names point to the exact same memory address (`id()`) in RAM. They are highly performant ($O(1)$ complexity) because they compare memory pointer integers directly rather than recursively parsing object data contents.

See: [`identity-operators.py`](https://github.com/imkjangid/PythonProbs/blob/main/operators/identity-operators.py)

```python
# Identity Behavior
list_a = [1, 2]
list_b = [1, 2]
list_c = list_a # Points to same memory reference

print("Value Equality (list_a == list_b):", list_a == list_b) # Output: True
print("Identity Reference (list_a is list_b):", list_a is list_b) # Output: False
print("Shared Identity Check (list_a is list_c):", list_a is list_c) # Output: True
```

### 6. Membership Operators

Behavioral Description: Membership operators (in, not in) test whether a targeted element exists inside a specified collection or sequence (like a string, list, tuple, set, or dictionary). The internal lookup behavior changes radically depending on the data type: searching a item inside a list scales linearly ($O(n)$ time complexity), whereas searching a key inside a dict or an element inside a set executes instantly via the hashing engine at constant time ($O(1)$ complexity).

See: [`membership-operators.py`](https://github.com/imkjangid/PythonProbs/blob/main/operators/membership-operators.py)

```python
# Membership Behavior
authorized_api_keys = {"KEY_ALPHA", "KEY_BETA", "KEY_GAMMA"} # Set lookup is O(1)
incoming_request_key = "KEY_BETA"

print("Is key authorized inside matrix?:", incoming_request_key in authorized_api_keys) # Output: True
```

### 7. Bitwise Operators
These operators treat integers as strings of binary bits (zeros and ones) and perform low-level operations directly on their binary representations. They work on the two's complement format for negative integers. When bitwise operators (&, |) are applied to set types instead of numbers, Python overrides their behavior to execute mathematical set operations like intersections and unions.

See: [`bitwise-operators.py`](https://github.com/imkjangid/PythonProbs/blob/main/operators/bitwise-operators.py)

```python
# Bitwise Behavior
# Binary mapping: 5 is 0101, 3 is 0011
val_a = 5 
val_b = 3

# Bitwise AND: 0101 & 0011 = 0001 (which is 1)
print("Bitwise AND (&) result:", val_a & val_b) # Output: 1

# Left Shift: 0101 << 1 becomes 1010 (which is 10)
print("Left Shift (<< 1) effectively multiplies by 2:", val_a << 1) # Output: 10
```



### Python Operator Precedence & Associativity Matrix

When multiple operators appear in a single expression, Python resolves them according to **Operator Precedence** (priority rules). If operators have the same precedence layer, Python resolves them sequentially using **Associativity** (direction of evaluation: Left-to-Right or Right-to-Left).

| Precedence Layer (High to Low) | Operator Symbol | Description | Associativity |
| :--- | :--- | :--- | :--- |
| **1 (Highest Priority)** | `()` | Parentheses (Grouping expressions explicitly) | Left-to-Right |
| **2** | `**` | Exponentiation (Power matrix calculations) | **Right-to-Left** |
| **3** | `+x`, `-x`, `~x` | Unary positive, Unary negative, Bitwise NOT | Right-to-Left |
| **4** | `*`, `/`, `//`, `%` | Multiplication, Division, Floor Division, Modulo | Left-to-Right |
| **5** | `+`, `-` | Addition, Subtraction | Left-to-Right |
| **6** | `<<`, `>>` | Bitwise Shift left / Shift right operations | Left-to-Right |
| **7** | `&` | Bitwise AND | Left-to-Right |
| **8** | `^` | Bitwise XOR | Left-to-Right |
| **9** | `\|` | Bitwise OR | Left-to-Right |
| **10** | `==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in` | Comparisons, Identity, and Membership tests | Left-to-Right (Chained) |
| **11 (Lowest Priority)** | `not`, `and`, `or` | Logical NOT, Logical AND, Logical OR | Left-to-Right |

