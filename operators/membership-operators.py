# Membership Behavior
authorized_api_keys = {"KEY_ALPHA", "KEY_BETA", "KEY_GAMMA"} # Set lookup is O(1)
incoming_request_key = "KEY_BETA"

print("Is key authorized inside matrix?:", incoming_request_key in authorized_api_keys) # Output: True