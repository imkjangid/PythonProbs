<div title="Back to Home" style="float:left;padding:10px 0;">
    Navigation: 
    <label>⬅️ <a href="https://github.com/imkjangid/PythonProbs">Back to Home</a></label>
    <label title="Showing Python Basics">📂 <a href="https://github.com/imkjangid/PythonProbs/tree/main/python-basics">Python Basics</a></label>
    <label title="Data Types">📁 <a href="https://github.com/imkjangid/PythonProbs/tree/main/data-types/">Data Types</a><label><label title="Operators">📂 <a href="https://github.com/imkjangid/PythonProbs/tree/main/operators/">Operators</a></label>
    <label title="Control Flow">📂 <a href="https://github.com/imkjangid/PythonProbs/tree/main/control-flow/">Control Flow</a></label>
    <label title="Functions">📂 <a href="https://github.com/imkjangid/PythonProbs/tree/main/functions/">Functions</a></label>
    <label title="Showing Closures & Decorators">📂 <span style="border-bottom: #06d solid 3px;">Closures & Decorators</span></label>
</div>
<br>
<br>

# Closuers & Decorators

## 1. What is a Closure? (The Backpack Analogy)
> Imagine a traveler who packs a water bottle into their backpack and leaves their house. Even though they are far away from home, they can still open their backpack and drink that water anytime.

> In Python, a Closure is a nested function (a function inside a function) that remembers and keeps access to the variables of its outer function, even after the outer function has completely finished executing. It carries those variables around like a backpack!

See: [`closure.py`](https://github.com/imkjangid/PythonProbs/blob/main/closure_decorator/closure.py)

```python
# Real-World Example: A customized message tag maker
def make_greeting_tag(prefix):
    # This is the outer function's variable
    
    def greet(name):
        # The inner function remembers 'prefix' from its "backpack"
        return f"{prefix} {name}!"
    
    return greet  # We return the inner function memory address WITHOUT calling it

# Creating customized closure functions
morning_greeter = make_greeting_tag("Good Morning")
festive_greeter = make_greeting_tag("Happy Diwali")

# Calling the inner functions later in the code
print(morning_greeter("Kapil"))   # Output: Good Morning Kapil!
print(festive_greeter("Yash"))    # Output: Happy Diwali Yash!
```

## 2. What is a Decorator? (The Smartphone Cover Analogy)

> Imagine you buy a brand new smartphone. It works perfectly fine on its own. Now, you put a stylish **protective cover** on it.
> - The phone's core internal hardware doesn't change.
> - But the cover adds new features (protection from falls, a cardholder slot, a better grip).

> In Python, a Decorator is a function that takes another function, **adds some extra features or behaviors to it, and returns it**, all without modifying the original function's source code. You use the `@` symbol shortcut to apply a decorator.

See: [`decorator.py`](https://github.com/imkjangid/PythonProbs/blob/main/closure_decorator/decorator.py)

```python
# Real-World Example: Adding a security lock check before running a task

# Step 1: Create the Decorator (The Wrapper/Cover)
def security_lock(original_function):
    
    def wrapper():
        print("[Security Check]: Scanning fingerprint... Access Granted!")
        original_function()  # Running the actual core function
        print("[Log]: Task completed securely.")
        
    return wrapper

# Step 2: Apply the Decorator to a basic function using the @ symbol
@security_lock
def open_bank_locker():
    print(" -> Core Action: Opening the safe vault box.")

# Step 3: Call the function
open_bank_locker()

# Output:
# [Security Check]: Scanning fingerprint... Access Granted!
#  -> Core Action: Opening the safe vault box.
# [Log]: Task completed securely.
```
## 3. Structural Mechanics Matrix

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; text-align: left; font-family: Arial, sans-serif; width: 100%;">
    <thead>
        <tr>
            <th style="padding: 10px; font-size: 15px; width: 20%;">Concept</th>
            <th style="padding: 10px; font-size: 15px; width: 30%;">Syntax Blueprint</th>
            <th style="padding: 10px; font-size: 15px; width: 50%;">Core Behavioral Logic</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="font-weight: bold; padding: 8px;">Closure</td>
            <td style="font-family: 'Courier New', Courier, monospace; padding: 8px; color: #d14;">def outer(x):<br>&nbsp;&nbsp;&nbsp;&nbsp;def inner(): return x<br>&nbsp;&nbsp;&nbsp;&nbsp;return inner</td>
            <td style="padding: 8px;">An inner function retains data variables from its enclosing outer scope even after the outer function execution context is destroyed. Used for lightweight data hiding.</td>
        </tr>
        <tr>
            <td style="font-weight: bold; padding: 8px;">Decorator</td>
            <td style="font-family: 'Courier New', Courier, monospace; padding: 8px; color: #d14;">@my_decorator<br>def my_func():</td>
            <td style="padding: 8px;">Wraps a target function inside another execution container layer. Dynamically extends behavior or injects preprocessing code without changing the original source code.</td>
        </tr>
    </tbody>
</table>

## 4. Advanced Concept: Memorization Using Closures

> We can use a closure to create a smart memory notebook (cache) that stores previous calculation inputs. This optimizes code performance and prevents repetitive processing bottlenecks.

See: [`memorization.py`](https://github.com/imkjangid/PythonProbs/blob/main/closure_decorator/memorization.py)

```python
# Real-World Example: A smart calculator that remembers previous operations

def smart_memo_calculator():
    past_calculations = {}  # The "backpack" storage notebook
    
    def double_number(x):
        if x in past_calculations:
            print(f"[Cache Hit]: Fetching saved answer for {x} instantly!")
            return past_calculations[x]
            
        print(f"[Calculating]: Running multiplication loops for {x}...")
        result = x * 2
        past_calculations[x] = result  # Saving the answer in the notebook
        return result
        
    return double_number

# Setup the closure instance
calc = smart_memo_calculator()

print(calc(5))   # First time: Runs the computation loop
print(calc(5))   # Second time: Grabs it instantly from the backpack memory!
```