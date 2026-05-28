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