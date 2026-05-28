<div title="Back to Home" style="float:left;padding:10px 0;">
    Navigation: 
    <label>⬅️ <a href="https://github.com/imkjangid/PythonProbs">Back to Home</a></label>
    <label title="Python Basics">📁 <a href="https://github.com/imkjangid/PythonProbs/tree/main/python-basics/">Python Basics</a><label>
    <label title="Data Types">📂 <a href="https://github.com/imkjangid/PythonProbs/tree/main/data-types/built-in-methods">Data Types</a>/<label title="Showing Data Types Methods"><span style="border-bottom: #06d solid 3px;">Built-in Methods</span><label></label>
    <label title="Operators">📂 <a href="https://github.com/imkjangid/PythonProbs/tree/main/operators/">Operators</a></label>
    <label title="Control Flow">📂 <a href="https://github.com/imkjangid/PythonProbs/tree/main/control-flow/">Control Flow</a></label></div>
</div>
<br>
<br>

# Data Types Essential Built-in Methods

## 1. String Methods
Strings has methods which are use to change and manipulate text data in different scenerio. Methods like split, upper, lower, replace make a string content to uppercase, lowercase and replace char/word in a string.

See: [`string-methods.py`](http://github.com/imkjangid/PythonProbs/blob/main/data-types/data-type-built-in-methods/string-methods.py)
```python
# ==========================================
# CORE STRING OPERATIONS
# ==========================================
raw_log = "  ERROR: Connection timed out on node_01   "

# Cleaning whitespace padding
clean_log = raw_log.strip()
print(f"Stripped Log: '{clean_log}'") # Output: 'ERROR: Connection timed out on node_01'

# Case manipulation & state checking
print("Uppercase conversion:", clean_log.upper())
print("Does it start with 'ERROR'?:", clean_log.startswith("ERROR")) # Output: True

# Splitting and Replacing
log_parts = clean_log.split(": ")
print("Split into tokens:", log_parts) # Output: ['ERROR', 'Connection timed out on node_01']

sanitized_log = clean_log.replace("node_01", "production_server")
print("Sanitized String:", sanitized_log)
```

## 2. List (list) Methods
Lists are mutable, so methods like `.append()`, `.extend()`, and `.sort()` modify the data structure in-place and return None.

See: [`list-methods.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/data-type-built-in-methods/list-methods.py)
```python
# ==========================================
# IN-PLACE LIST MANIPULATION
# ==========================================
active_ports = [80, 443]

# Appending a single element vs Extending an iterable
active_ports.append(8080)
print("After Append:", active_ports)  # Output: [80, 443, 8080]

active_ports.extend([22, 21])
print("After Extend:", active_ports)  # Output: [80, 443, 8080, 22, 21]

# Removing elements: by index (pop) vs by value (remove)
removed_port = active_ports.pop(2)    # Removes index 2 (8080)
print(f"Popped Port: {removed_port}, Current Ports: {active_ports}")

active_ports.remove(21)               # Removes the value 21 directly
print("After Removing value 21:", active_ports)
```

## 3. Dictionary (dict) Methods
Dictionaries manage key-value pairs. Safe data extraction and clearing runtime references are key workflows here.

See: [`dict-methods.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/data-type-built-in-methods/dict-methods.py)
```python
# ==========================================
# ADVANCED KEY-VALUE EXTRACTION
# ==========================================
user_session = {"user_id": 101, "role": "admin", "status": "Active"}

# Safe retrieval using .get() to prevent explicit KeyError crashes
# Syntax: .get(key, default_value)
print("Role Resolved:", user_session.get("role", "Guest"))
print("Token Check (Fallback):", user_session.get("auth_token", "NOT_FOUND"))

# Fetching isolated dynamic view loops
print("Dictionary Keys View:", list(user_session.keys()))
print("Dictionary Values View:", list(user_session.values()))

# Merging dictionaries using .update()
user_session.update({"status": "Suspended", "flagged": True})
print("Updated Dictionary Payload:", user_session)
```

## 4. Set (set) Methods
Sets focus on unique memberships and core mathematical operations like `union()`, `intersection()`, `difference()`, `symmetric_difference()` and so on.

See: [`set-methods.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/data-type-built-in-methods/set-methods.py)

```python
# ==========================================
# SET MATHEMATICS & COMPONENT TESTING
# ==========================================
set_alpha = {1, 2, 3, 4}
set_beta = {3, 4, 5, 6}

# Non-mutating methods returning a new set object
print("Union Result:", set_alpha.union(set_beta))                 # Output: {1, 2, 3, 4, 5, 6}
print("Intersection Result:", set_alpha.intersection(set_beta)) # Output: {3, 4}

# Mutating operations
set_alpha.add(99)
print("Set Alpha after adding element:", set_alpha)

# Discard vs Remove safety check
set_alpha.discard(100) # Safe: Does nothing if element is missing
print("Discard execution passed without crashing.")
```

## 5. Frozen Set (frozenset) Methods
Since frozen sets are completely immutable, state-changing methods like `.add()`, `.remove()`, `.pop()` and others are restricted in them. They support only those methods that return a completely new object without altering the data values.

See: [`frozenset-methods.py`](https://github.com/imkjangid/PythonProbs/blob/main/data-types/data-type-built-in-methods/frozenset-methods.py)

```python
# ==========================================
# IMMUTABLE FROZEN SET COMPONENT METHODS
# ==========================================
fs_network_a = frozenset([80, 443, 8080])
fs_network_b = frozenset([443, 22, 21])

# A. Checking overlapping boundaries using Boolean Methods
# .isdisjoint() returns True if there is zero intersection
print("Are networks entirely disjoint?:", fs_network_a.isdisjoint(fs_network_b)) # Output: False (443 is common)

# Checking subset/superset constraints
fs_sub = frozenset([80, 443])
print("Is fs_sub a subset of network_a?:", fs_sub.issubset(fs_network_a)) # Output: True

# B. Copying references securely
# Using .copy() on a frozenset behaves differently than mutable collections
fs_copy = fs_network_a.copy()
print("Are original and copy the exact same object reference?:", fs_network_a is fs_copy) # Output: True!
```