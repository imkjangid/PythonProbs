# Real-World Example: Server Configuration Control Scopes
server_env = "PRODUCTION" # Global Scope (G)

def network_gateway_outer():
    gateway_ip = "192.168.1.1" # Enclosing Scope (E) relative to inner function
    
    def internal_node_inner():
        node_id = "NODE_DELTA_09" # Local Scope (L)
        
        # Accessing all three scopes simultaneously
        print(f"--- Scope Check: {node_id} active on {gateway_ip} in {server_env} ---")
        
    internal_node_inner() # Function calling pipeline

network_gateway_outer() # Function calling pipeline