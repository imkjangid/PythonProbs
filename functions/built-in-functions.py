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