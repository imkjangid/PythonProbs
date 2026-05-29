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