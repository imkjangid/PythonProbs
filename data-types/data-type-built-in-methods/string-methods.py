raw_log = "  ERROR: Connection timed out on node_01    "

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