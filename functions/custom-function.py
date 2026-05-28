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