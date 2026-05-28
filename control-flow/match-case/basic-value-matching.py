status_code = 400

match status_code:
    case 200:
        print("Success: OK")
    case 400:
        print("Client Error: Bad Request")
    case 404:
        print("Client Error: Not Found")
    case 500 | 503:
        # The '|' symbol represents an 'OR' pattern
        print("Server Error State")
    case _:
        print("Unknown Status Code Fallback")