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