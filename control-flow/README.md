<div title="Back to Home" style="float:left;padding:10px 0;">
    Navigation: 
    <label>⬅️ <a href="https://github.com/imkjangid/PythonProbs">Back to Home</a></label>
    <label title="Python Basics">📁 <a href="https://github.com/imkjangid/PythonProbs/tree/main/python-basics/">Python Basics</a><label>
    <label title="Data Types">📁 <a href="https://github.com/imkjangid/PythonProbs/tree/main/data-types/">Data Types</a><label>
    <label title="Operators">📂 <a href="https://github.com/imkjangid/PythonProbs/tree/main/operators/">Operators</a></label>
    <label title="Showing Control Flow">📂 <span style="border-bottom: #06d solid 3px;">Control Flow</span></label>
</div>
<br>
<br>

# Control Flow

## 1. Basic Examples & Primary Syntax

### A. Conditional Gateways (if-elif-else)
In Python, programmatic decisions are executed using the `if`, `elif` (else if), and `else` keywords. Instead of curly braces `{}` to define scopes, Python relies strictly on Indentation (conventionally 4 spaces) to mark block boundaries.

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; text-align: left; font-family: Arial, sans-serif; width: 100%;"><thead><tr><th style="padding: 10px; font-size: 15px; width: 25%;">Structure Layer</th><th style="padding: 10px; font-size: 15px; width: 25%;">Syntax Architecture</th><th style="padding: 10px; font-size: 15px; width: 35%;">Logical Branch Evaluation</th><th style="padding: 10px; font-size: 15px; width: 15%;">Time Complexity</th></tr></thead><tbody><tr><td style="font-weight: bold; padding: 8px;">Simple if</td><td style="font-family: 'Courier New', Courier, monospace; padding: 8px; color: #d14;">if condition:</td><td style="padding: 8px;">If the condition evaluates to True, the block executes; otherwise, it is entirely skipped.</td><td style="padding: 8px; font-family: 'Courier New', Courier, monospace;">O(1)</td></tr><tr><td style="font-weight: bold; padding: 8px;">Binary if-else</td><td style="font-family: 'Courier New', Courier, monospace; padding: 8px; color: #d14;">if condition:<br>&nbsp;&nbsp;&nbsp;&nbsp;...<br>else:<br>&nbsp;&nbsp;&nbsp;&nbsp;...</td><td style="padding: 8px;">Guarantees that execution flows through exactly <strong>one mandatory branch</strong> based on boolean truthiness.</td><td style="padding: 8px; font-family: 'Courier New', Courier, monospace;">O(1)</td></tr><tr><td style="font-weight: bold; padding: 8px;">Chained if-elif</td><td style="font-family: 'Courier New', Courier, monospace; padding: 8px; color: #d14;">if c1:<br>&nbsp;&nbsp;&nbsp;&nbsp;...<br>elif c2:<br>&nbsp;&nbsp;&nbsp;&nbsp;...<br>else:<br>&nbsp;&nbsp;&nbsp;&nbsp;...</td><td style="padding: 8px;">Evaluates sequentially from top to bottom. The first matching True condition executes its block and <strong>short-circuits</strong> the remaining evaluations.</td><td style="padding: 8px; font-family: 'Courier New', Courier, monospace;">O(n)</td></tr></tbody></table>

#### i. Basic if

See: [`basic-if-else.py`](https://github.com/imkjangid/PythonProbs/blob/main/control-flow/conditions/basic-if-else.py)

```python
# ==========================================
# BASIC IF-ELSE INITIALIZATION
# ==========================================
age = 20

if age >= 18:
    print("Status: Eligible to Vote")  # Executed if condition is True
else:
    print("Status: Not Eligible to Vote")  # Executed if condition is False
```

#### ii. Multi-Condition Chain

See: [`multi-condition-chain.py`](https://github.com/imkjangid/PythonProbs/blob/main/control-flow/conditions/multi-condition-chain.py)

```python
# ==========================================
# MULTI-CONDITION CHAINING (if-elif-else)
# ==========================================
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"  # This block fires, and the rest of the chain is skipped
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Resulting Grade Matrix: {grade}")
```

#### iii. Nested Conditional Gateways

See: [`nested-conditional-gateways.py`](https://github.com/imkjangid/PythonProbs/blob/main/control-flow/conditions/nested-conditional-gateways.py)

```python
# ==========================================
# NESTED CONDITIONAL GATEWAYS
# ==========================================
has_account = True
is_logged_in = False

if has_account:
    if is_logged_in:
        print("Redirecting to Dashboard...")
    else:
        print("Alert: Please login first.")
else:
    print("Redirecting to Registration Page...")
```

## B. Structural Pattern Matching (match-case)
### i. Basic Value Matching (Literal Patterns)
The simplest form of `match-case` mimics a traditional switch-case statement by comparing a variable against exact literal values (`int`, `float`, `str`, `bool`, or `None`). The `_` (underscore) symbol acts as the Wildcard (Default Catch-all) case, executing if no other patterns match.

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; text-align: left; font-family: Arial, sans-serif; width: 100%;"><thead><tr><th style="padding: 10px; font-size: 15px; width: 25%;">Pattern Design Category</th><th style="padding: 10px; font-size: 15px; width: 25%;">Syntax Mapping Blueprint</th><th style="padding: 10px; font-size: 15px; width: 35%;">Matching Behavior &amp; Runtime Logic</th><th style="padding: 10px; font-size: 15px; width: 15%;">Time Complexity</th></tr></thead><tbody><tr><td style="font-weight: bold; padding: 8px;">Literal Pattern</td><td style="font-family: 'Courier New', Courier, monospace; padding: 8px; color: #d14;">case 200:</td><td style="padding: 8px;">Checks for exact structural or value equality (== comparison contract).</td><td style="padding: 8px; font-family: 'Courier New', Courier, monospace;">O(1)</td></tr><tr><td style="font-weight: bold; padding: 8px;">Or Pattern</td><td style="font-family: 'Courier New', Courier, monospace; padding: 8px; color: #d14;">case 401 | 403:</td><td style="padding: 8px;">Packs multiple conditions together; short-circuits the case match if <em>any</em> sub-pattern passes.</td><td style="padding: 8px; font-family: 'Courier New', Courier, monospace;">O(1)</td></tr><tr><td style="font-weight: bold; padding: 8px;">Sequence Unpacking</td><td style="font-family: 'Courier New', Courier, monospace; padding: 8px; color: #d14;">case [command, *args]:</td><td style="padding: 8px;">Checks if the input is an iterable of compatible length, maps the head item to command, and slices the remainder into args.</td><td style="padding: 8px; font-family: 'Courier New', Courier, monospace;">O(n)</td></tr><tr><td style="font-weight: bold; padding: 8px;">Mapping Pattern</td><td style="font-family: 'Courier New', Courier, monospace; padding: 8px; color: #d14;">case {"role": "admin"}:</td><td style="padding: 8px;">Verifies key existence inside a dictionary mapping layout and checks the key's exact sub-value.</td><td style="padding: 8px; font-family: 'Courier New', Courier, monospace;">O(1)</td></tr><tr><td style="font-weight: bold; padding: 8px;">Conditional Guard</td><td style="font-family: 'Courier New', Courier, monospace; padding: 8px; color: #d14;">case x if x > 100:</td><td style="padding: 8px;">Binds the matched item to local variable x, then processes the relational guard expression before executing the inner block.</td><td style="padding: 8px; font-family: 'Courier New', Courier, monospace;">Dynamic</td></tr></tbody></table>

See: [`basic-value-matching.py`](https://github.com/imkjangid/PythonProbs/blob/main/control-flow/match-case/basic-value-matching.py)

```python
status_code = 400

match status_code:
    case 200:
        return "Success: OK"
    case 400:
        return "Client Error: Bad Request"
    case 404:
        return "Client Error: Not Found"
    case 500 | 503:
        # The '|' symbol represents an 'OR' pattern
        return "Server Error State"
    case _:
        return "Unknown Status Code Fallback"

print(evaluate_http_status(200))  # Output: Success: OK
print(evaluate_http_status(503))  # Output: Server Error State
print(evaluate_http_status(999))  # Output: Unknown Status Code Fallback
```

### ii. Sequence Pattern Matching (Destructuring Lists/Tuples)
match-case can look inside sequences to verify their length and unpack their internal values dynamically into local variables.

See: [`sequence-pattern-matching.py`](https://github.com/imkjangid/PythonProbs/blob/main/control-flow/match-case/sequence-pattern-matching.py)

```python
command_payload = ["LOGIN", "kjangid"]

match command_payload:
    # Matches an empty sequence
    case []:
        print("System Alert: Received empty command sequence.")
        
    # Matches a sequence with exactly one element
    case ["SYSTEM_REBOOT"]:
        print("Action: Triggering immediate system reboot sequence.")
        
    # Matches a sequence with exactly two elements and binds the second to 'user'
    case ["LOGIN", user]:
        print(f"Action: Initializing secure login protocol for user: {user}")
        
    # Matches any sequence starting with "LOG" and packs the remainder into a list using '*'
    case ["LOG", severity, *message_tokens]:
        print(f"[{severity}] Parsed Log Tokens: {message_tokens}")
        
    case _:
        print("System Alert: Malformed command signature.")
```

## C. Looping Constructs (for & while)
Loops are used to iterate over a sequence (like a list, tuple, string, or dictionary) or repeat a block of code while a condition remains true.

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; text-align: left; font-family: Arial, sans-serif; width: 100%;"><thead><tr><th style="padding: 10px; font-size: 15px; width: 25%;">Loop Type</th><th style="padding: 10px; font-size: 15px; width: 25%;">Controller Mechanic</th><th style="padding: 10px; font-size: 15px; width: 35%;">Associative else Behavior</th><th style="padding: 10px; font-size: 15px; width: 15%;">Time Complexity</th></tr></thead><tbody><tr><td style="font-weight: bold; padding: 8px;">for loop</td><td style="padding: 8px;"><strong>Definite Iteration:</strong> Traverses over a fixed sequence or an iterable generator using a pointer.</td><td style="padding: 8px;">Executes only when the iterable sequence <strong>exhausts completely</strong> without hitting an explicit break.</td><td style="padding: 8px; font-family: 'Courier New', Courier, monospace;">O(n)</td></tr><tr><td style="font-weight: bold; padding: 8px;">while loop</td><td style="padding: 8px;"><strong>Indefinite Iteration:</strong> Continues loop cycles as long as an underlying boolean evaluation flag remains True.</td><td style="padding: 8px;">Executes only when the monitoring condition evaluates to False naturally without a break intercept.</td><td style="padding: 8px; font-family: 'Courier New', Courier, monospace;">O(n)</td></tr></tbody></table>

### i. for-loop

See: [`for-loop.py`](https://github.com/imkjangid/PythonProbs/blob/main/control-flow/loops/for-loop.py)

```python
# Definite Iteration via 'for' loop using range()
print("Executing Definite Iteration:")
for i in range(1, 4):
    print(f" -> Loop Step Counter: {i}")
```

### ii. while-loop

See: [`while-loop.py`](https://github.com/imkjangid/PythonProbs/blob/main/control-flow/loops/while-loop.py)

```python
# Indefinite Iteration via 'while' loop
print("\nExecuting Indefinite Iteration:")
countdown = 3
while countdown > 0:
    print(f" -> T-Minus: {countdown}")
    countdown -= 1 # Crucial state modification to prevent infinite loops
```

