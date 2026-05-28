<div title="Back to Home" style="float:left;padding:10px 0;">
    Navigation: 
    <label>⬅️ <a href="https://github.com/imkjangid/PythonProbs">Back to Home</a></label>
    <label title="Python Basics">📁 <a href="https://github.com/imkjangid/PythonProbs/tree/main/python-basics/">Python Basics</a><label>
    <label title="Data Types">📁 <a href="https://github.com/imkjangid/PythonProbs/tree/main/data-types/">Data Types</a><label>
    <label title="Operators">📂 <a href="https://github.com/imkjangid/PythonProbs/tree/main/operators/">Operators</a></label>
    <label title="Control Flow">📂 <a href="https://github.com/imkjangid/PythonProbs/tree/main/control-flow/">Control Flow</a></label>
    <label title="Showing Functions">📂 <span style="border-bottom: #06d solid 3px;">Functions</span></label>
</div>
<br>
<br>

# Functions & Advanced Functional Programming

## 1. Examples & Primary Syntax
### A. Built-in Functions vs. Custom Functions
Python provides a vast library of pre-defined Built-in Functions (like `print()`, `len()`, `max()`, and `type()`) to perform immediate tasks. For custom workflows, you can define your own blocks of code using the `def` keyword. A function only executes when it is explicitly invoked via a Function Call.

#### i. Built-in Functions
See: [`built-in-functions.py`](https://github.com/imkjangid/PythonProbs/blob/main/functions/built-in-function.py)

```python
# ==========================================
# BUILT-IN FUNCTIONS OVERVIEW
# ==========================================
system_ports = [80, 8080, 443]

print("Total Active Ports (len):", len(system_ports)) # Output: 3
print("Highest Port Number (max):", max(system_ports)) # Output: 8080

print("Type of data (type):", type(system_ports)) # Output: <class 'list'>
print("Sorting (sorted):", sorted(system_ports)) # Output: [80, 8080, 443]

name = input("enter your name: ")
print("Welcome ", name) # Output: Welcome Kapil
```

#### ii. Custom Functions: Defining and Calling a Function
To create a custom function, we use the def keyword, followed by the function name and parentheses `()`. A function only runs when you explicitly call it.

See: [`custom-function.py`](https://github.com/imkjangid/PythonProbs/blob/main/functions/custom-function.py)


```python
# ==========================================
# DEFINING & CALLING A CUSTOM FUNCTION
# ==========================================
# Real-World Example: Generating a standardized local API greeting
def generate_welcome_message():
    """
    Docstring: This function takes user credentials and builds a 
    standardized landing page header.
    """
    username = "Kapil"
    venture_name = "Codweb Lab"

    formatted_header = f"Welcome back, {username}! | Connected to: {venture_name} Engine"
    print(formatted_header) # Sends the processed string back to the caller

# Function Calling Pipeline
generate_welcome_message() # Output: Welcome back, Kapil! | Connected to: Codweb Lab Engine
```

#### iii. Returning Functions with `return` Keyword

See: [`return-function.py`](https://github.com/imkjangid/PythonProbs/blob/main/functions/return-function.py)


```python
# Example: Calculating the total price of apples
def calculate_bill():
    price_per_kg = 120 # Rs/kg, price
    weight = 3 # kgweight
    total_price = price_per_kg * weight
    return total_price

# Calling the function with values
my_bill = calculate_bill() # returned value assigned to a variable
print("Total Bill Amount: Rs.", my_bill) # Output: Total Bill Amount: Rs. 360
```

### B. Modular Programming & Code Reusability
Functions are the foundation of Modular Programming. Instead of writing repetitive lines of code across your scripts, you wrap your logic inside isolated functional modules. This ensures code reusability if a business logic rule changes, you only update it inside that single function rather than altering dozens of files.

## 2. Scope Resolution: The LEGB Rule
When you access a variable inside a function, Python resolves its reference using a strict lookup order hierarchy called the LEGB Rule: Local $\rightarrow$ Enclosing $\rightarrow$ Global $\rightarrow$ Built-in.
- **Local (L)**: Variables defined entirely inside the current active function block.
- **Enclosing (E)**: Variables inside an outer nested function (relevant during structural closures).
- **Global (G)**: Variables declared at the topmost level of the script module.
- **Built-in (B)**: Standard pre-loaded keywords (like `open`, `range`, `ValueError`).

See: [`scope-resolution-1.py`](https://github.com/imkjangid/PythonProbs/blob/main/functions/scope-resolution-1.py)

```python
# Real-World Example: Classroom vs. School Bag

school_name = "Greenwood High" # GLOBAL: Everyone in the school knows it.

def classroom_one():
    student_bag = "Geometry Box" # LOCAL: Only visible inside this classroom.
    
    print("School Name (Global):", school_name)
    print("Inside Classroom (Local):", student_bag)

print("School Name (Global):", school_name) # Output: Greenwood High
classroom_one()
print("student bag (Local):", student_bag) # Output: NameError: name 'student_bag' is not defined
```

See: [`scope-resolution-2.py`](https://github.com/imkjangid/PythonProbs/blob/main/functions/scope-resolution-2.py)

```python
# Real-World Example: Server Configuration Control Scopes
server_env = "PRODUCTION" # Global Scope (G)

def network_gateway_outer():
    gateway_ip = "192.168.1.1" # Enclosing Scope (E) relative to inner function
    
    def internal_node_inner():
        node_id = "NODE_DELTA_09" # Local Scope (L)
        
        # Accessing all three scopes simultaneously
        print(f"--- Scope Check: {node_id} active on {gateway_ip} in {server_env} ---")
        
    internal_node_inner() # Function calling pipeline

network_gateway_outer() # Function calling pipeline
```

### Modifying Scopes: `global` vs. `nonlocal`
By default, functions can read outer variables but cannot modify them. Attempting to reassign an outer variable creates a new local variable instead. To explicitly modify global or enclosing variables, you must declare them using the `global` or `nonlocal` keywords.

See: [`modifying-scopes.py`](https://github.com/imkjangid/PythonProbs/blob/main/functions/modifying-scopes.py)

```python
score = 0 # Global

def play_game():
    player_status = "Level 1" # Enclosing
    
    def complete_level():
        global score
        nonlocal player_status
        
        score = 100 # Modifies the Global score
        player_status = "Level 2" # Modifies the Enclosing status
        
    complete_level()
    print("Updated Status:", player_status) # Output: Level 2

play_game()
print("Updated Global Score:", score) # Output: 100
```

## 3. Standard Arguments & Parameters
### A. Parameters vs. Arguments (The Core Difference)
- **Parameters**: Parameters: These are the variable names written inside the parentheses `()` during a function's definition (def). They act as empty placeholders.

- **Arguments**: These are the actual values or data coordinates you pass into the function when you invoke or call it.

See: [`standard-arguments.py`](https://github.com/imkjangid/PythonProbs/blob/main/functions/standard-arguments.py)

```python
def greet_user(username):  # 'username' is a PARAMETER
    print(f"Hello, {username}!")

greet_user("Kapil")        # "Kapil" is an ARGUMENT
```

### B. The 3 Pillars of Standard Arguments
Before handling dynamic lengths, you must master how standard data variables are mapped from a function call to a definition. Let's look at a simple smartphone ordering analogy:
#### i. Positional Arguments (Order Matters)
This is the most basic setup. Arguments are mapped to parameters based strictly on the sequence or position in which they are written.

See: [`positional-arguments.py`](https://github.com/imkjangid/PythonProbs/blob/main/functions/positional-arguments.py)


```python
# Real-World Example: Booking a smartphone order
def order_phone(brand, model):
    print(f"Order Confirmed: {brand} {model}")

# Perfect Order
order_phone("Apple", "iPhone 15")  # Output: Order Confirmed: Apple iPhone 15

# Wrong Order Trap! (Agar sequence badla, toh meaning badal jayega)
order_phone("iPhone 15", "Apple")  # Output: Order Confirmed: iPhone 15 Apple
```

#### ii. Keyword Arguments (Name Matters, Order Doesn't)
If you do not want to worry about maintaining a strict structural sequence, you can explicitly state the parameter names during the function call using a `key=value` format.

See: [`keyword-arguments.py`](https://github.com/imkjangid/PythonProbs/blob/main/functions/keyword-arguments.py)


```python
def order_phone(brand, model):
    print(f"Order Confirmed: {brand} {model}")

# Calling using key=value syntax (Order doesn't matter here)
order_phone(model="Galaxy S24", brand="Samsung") 
# Output: Order Confirmed: Samsung Galaxy S24
```

#### iii. Default Arguments (The Backup Plan)
Sometimes you want a parameter to have a fallback option so that the code does not crash if a user misses an input. You assign these baseline values using the = operator within the function definition.

See: [`default-arguments.py`](https://github.com/imkjangid/PythonProbs/blob/main/functions/default-arguments.py)


```python
# Real-World Example: Default shipping destination is hardcoded to India
def create_shipping_label(customer_name, country="India"):
    print(f"Shipping to: {customer_name}, Country: {country}")

# 1. Missing the optional parameter (Triggers default fallback "India")
create_shipping_label("Kapil")  # Output: Shipping to: Kapil, Country: India

# 2. Providing the optional parameter (Overwrites default to "USA")
create_shipping_label("Yash", country="USA")  # Output: Shipping to: Yash, Country: USA
```

#### iv: Transitioning to Arbitrary Arguments (*args & kwargs)
What are Arbitrary Arguments? (Real-World Analogy)
Imagine you are hosting a party and inviting friends.
- **Normal Arguments**: You know exactly how many friends are coming (e.g., exactly 3 friends). You create 3 seat allocations.
- **Arbitrary Arguments**: You don't know how many friends might show up. It could be 2, 5, or 10! Instead of creating fixed seats, you put a big empty couch or a dynamic dining table where anyone who comes can sit.

In Python, when you don't know in advance how many inputs a user will pass to your function, you use Arbitrary Arguments:

> **args (Non-keyword arguments)**: `*args` collects extra inputs as a Tuple.
> **kwargs (Keyword arguments)**: `**kwargs` collects extra inputs with names (labels) as a Dictionary.

#### `*args` (The Unnamed Packing Engine)
The asterisk `*` is the magic symbol. It tells Python to pack all the remaining loose inputs into a single ordered Tuple container.

See: [`args-function.py`](https://github.com/imkjangid/PythonProbs/blob/main/functions/args-function.py)

```python
# ==========================================
# WORKING WITH *ARGS (TUPLE PACKING)
# ==========================================
# Real-World Example: Adding items to a shopping cart
def calculate_total_items(*items):
    print("Under the hood, items are stored as:", type(items)) # Output: <class 'tuple'>
    print("Items list:", items)
    
    total = len(items)
    return f"Total items in your shopping cart: {total}"

# Calling the same function with different number of inputs
print(calculate_total_items("Book", "Pen"))          # Passing 2 inputs
print(calculate_total_items("Laptop", "Mouse", "Bag", "Mic")) # Passing 4 inputs
```

#### `**kwargs` (The Named/Labeled Packing Engine)
The double asterisk `**` tells Python to grab all the named inputs (`key=value` pairs) and pack them nicely into a searchable Dictionary container.

See: [`kwargs-function.py`](https://github.com/imkjangid/PythonProbs/blob/main/functions/kwargs-function.py)

```python
# ==========================================
# WORKING WITH **KWARGS (DICTIONARY PACKING)
# ==========================================
# Real-World Example: Creating a student profile card
def print_student_profile(name, **details):
    print(f"\n--- Student: {name} ---")
    print("Under the hood, details are stored as:", type(details)) # Output: <class 'dict'>
    
    # Looping through the collected dictionary items
    for key, value in details.items():
        print(f" -> {key.capitalize()}: {value}")

# Calling the function with varying named details
print_student_profile("XYZ", age=36, city="Ahmedabad", course="Python")
print_student_profile("ABC", city="Jaipur", role="Developer")
```

#### The Ultimate Argument Ordering Matrix
When you are mixing normal parameters, `*args`, and `**kwargs` together inside a single function definition, Python enforces a strict vertical order layout. Breaking this sequence will trigger a compilation error.

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; text-align: left; font-family: Arial, sans-serif; width: 100%;">
    <thead>
        <tr>
            <th style="padding: 10px; font-size: 15px; width: 15%;">Position Order</th>
            <th style="padding: 10px; font-size: 15px; width: 25%;">Argument Type</th>
            <th style="padding: 10px; font-size: 15px; width: 20%;">Syntax Blueprint</th>
            <th style="padding: 10px; font-size: 15px; width: 40%;">Internal Data Collection Container</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="font-weight: bold; padding: 8px;">1st (Highest)</td>
            <td style="padding: 8px;">Standard Positional / Required</td>
            <td style="font-family: 'Courier New', Courier, monospace; padding: 8px; color: #d14;">arg1, arg2</td>
            <td style="padding: 8px;">Bound directly to independent scalar local variables.</td>
        </tr>
        <tr>
            <td style="font-weight: bold; padding: 8px;">2nd</td>
            <td style="padding: 8px;">Arbitrary Positional (Optional)</td>
            <td style="font-family: 'Courier New', Courier, monospace; padding: 8px; color: #d14;">*args</td>
            <td style="padding: 8px; color: #2980b9; font-weight: bold;">Packed into an Immutable Tuple.</td>
        </tr>
        <tr>
            <td style="font-weight: bold; padding: 8px;">3rd</td>
            <td style="padding: 8px;">Keyword-Only / Defaults</td>
            <td style="font-family: 'Courier New', Courier, monospace; padding: 8px; color: #d14;">status="Active"</td>
            <td style="padding: 8px;">Bound to defaults unless explicitly named during call.</td>
        </tr>
        <tr>
            <td style="font-weight: bold; padding: 8px;">4th (Lowest)</td>
            <td style="padding: 8px;">Arbitrary Keyword (Optional)</td>
            <td style="font-family: 'Courier New', Courier, monospace; padding: 8px; color: #d14;">**kwargs</td>
            <td style="padding: 8px; color: #e74c3c; font-weight: bold;">Packed into a Mutable Dictionary.</td>
        </tr>
    </tbody>
</table>

See: [`unified-order.py`](https://github.com/imkjangid/PythonProbs/blob/main/functions/unified-order.py)

```python
# Complete Unified Order Example
def master_factory(required_id, *args, status="Pending", **kwargs):
    print("Required ID:", required_id)
    print("Extra Args Tuple:", args)
    print("Status Flag:", status)
    print("Extra Kwargs Dict:", kwargs)

master_factory(101, "Extra1", "Extra2", status="Active", location="India", score=95)
```

## 3. Recursion & Memoization

- **Recursion**: A behavioral programming pattern where a function calls itself to break down complex mathematical calculations into smaller sub-problems. Every recursive function must contain a Base Case to prevent infinite execution stacks.
- **Memoization**: An optimization technique used to accelerate slow recursive processes by caching the results of expensive function calls inside an internal look-up storage table. If the same inputs occur again, Python fetches the answer directly from the cache ($O(1)$ lookup) instead of recalculating it.

See: [`recursion-memoization.py`](https://github.com/imkjangid/PythonProbs/blob/main/functions/recursion-memoization.py)


```python
# Example: Counting down to zero (Recursion)
def count_down(number):
    # Base Case (The Stop Sign)
    if number == 0:
        print("Blast off!")
        return
        
    print(number)
    count_down(number - 1) # Function calls itself with a smaller number

count_down(3)
# Output:
# 3
# 2
# 1
# Blast off!
```

## 4. Advanced Functional Pipeline Tools
### A. Lambda Functions (Anonymous Expressions)
A Lambda Function is a compact, single-line anonymous function defined without a name using the `lambda` keyword. It can take any number of arguments but can only execute a single expression.

See: [`lambda-function.py`](https://github.com/imkjangid/PythonProbs/blob/main/functions/lambda-function.py)


```python
# Syntax Pattern: lambda arguments: expression

# Regular or Standard Function
def square_num(x): return x ** 2

# Equivalent Lambda Function
quick_square = lambda x: x ** 2
print("Lambda Execution:", quick_square(5)) # Output: 25

# Real-World Use Case: Inline conditional string sanitation formatting
clean_input = lambda text: text.strip().lower()
print(clean_input("   ARCHITECTNK.COM   ")) # Output: architectnk.com
```

### B. Functional Pipeline: `map()`, `filter()`, and `reduce()`
- **`map(function, iterable)`**: Applies a targeted transformation function to every individual item inside an iterable and returns a clean map generator object.
- **`filter(function, iterable)`**: Tests every item in an iterable against a boolean condition. It extracts only the items that evaluate to `True`.
- **`reduce(function, iterable)`**: Part of the `functools` module. It applies a rolling calculation across the elements of a sequence sequentially from left to right, reducing the entire array down to a single cumulative scalar value.

See: [`functional-pipeline.py`](https://github.com/imkjangid/PythonProbs/blob/main/functions/functional-pipeline.py)


```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# 1. FILTER: Keep only numbers greater than 3
filtered_numbers = list(filter(lambda x: x > 3, numbers))
print("Filtered (x > 3):", filtered_numbers) # Output: [4, 5, 6]

# 2. MAP: Multiply each remaining number by 10
mapped_numbers = list(map(lambda x: x * 10, filtered_numbers))
print("Mapped (Multiply by 10):", mapped_numbers) # Output: [40, 50, 60]

# 3. REDUCE: Add them all together into one final total
final_sum = reduce(lambda total, current: total + current, mapped_numbers)
print("Reduced (Sum of all):", final_sum) # Output: 150 (40 + 50 + 60) # Output: 150
```

## 5. Memory Execution: Eager vs. Lazy Execution
Understanding how functional pipelines generate objects in memory is a critical requirement for scaling systems efficiently.
- **Eager Execution**: Standard collections (like List Comprehensions or basic arrays) calculate all data elements immediately and load the entire payload directly into RAM. This can lead to heavy memory consumption if you are working with millions of entries.
- **Lazy Execution**: Functional streams (like `map()` and `filter()`) use lazy evaluation. They do not calculate anything upon creation; instead, they return a lightweight generator placeholder pointer. Data elements are computed and yielded one-at-a-time only when you explicitly iterate over them or cast them to a list.

See: [`eager-lazy-execution.py`](https://github.com/imkjangid/PythonProbs/blob/main/functions/eager-lazy-execution.py)


```python
import sys

# Data target matrix boundary size
data_range = range(100000)

# Eager Execution: Immediately builds a 100,000 item list inside RAM
eager_list = [x * 2 for x in data_range]

# Lazy Execution: Only saves a memory pipeline instruction pointer map
lazy_map_stream = map(lambda x: x * 2, data_range)

print(f"RAM footprint for Eager List Array: {sys.getsizeof(eager_list)} bytes.")
print(f"RAM footprint for Lazy Map Stream:  {sys.getsizeof(lazy_map_stream)} bytes.")
# Note: The lazy stream object consumes almost zero bytes regardless of the dataset size!
```