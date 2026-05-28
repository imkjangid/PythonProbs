score = 0 # Global

def play_game():
    player_status = "Level 1" # Enclosing
    
    def complete_level():
        global score
        nonlocal player_status
        
        score = 100 # Modifies the Global score
        player_status = "Level 2" # Modifies the Enclosing status
        
    complete_level()
    print("Updated Status:", player_status) # Output: Level 2

play_game()
print("Updated Global Score:", score) # Output: 100