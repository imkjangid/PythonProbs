# ==========================================
# 2. IN-PLACE LIST MANIPULATION
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