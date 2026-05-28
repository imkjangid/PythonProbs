command_payload = ["LOGIN", "kjangid"]

match command_payload:
    # Matches an empty sequence
    case []:
        print("System Alert: Received empty command sequence.")
        
    # Matches a sequence with exactly one element
    case ["SYSTEM_REBOOT"]:
        print("Action: Triggering immediate system reboot sequence.")
        
    # Matches a sequence with exactly two elements and binds the second to 'user'
    case ["LOGIN", user]:
        print(f"Action: Initializing secure login protocol for user: {user}")
        
    # Matches any sequence starting with "LOG" and packs the remainder into a list using '*'
    case ["LOG", severity, *message_tokens]:
        print(f"[{severity}] Parsed Log Tokens: {message_tokens}")

    # Matches any other sequence
    case _:
        print("System Alert: Malformed command signature.")