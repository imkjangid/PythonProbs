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