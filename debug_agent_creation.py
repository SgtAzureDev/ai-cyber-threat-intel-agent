import sys
import os
sys.path.append('.')

print("=== Debugging Agent Creation ===")

# Import and check what happens during agent creation
try:
    import app.agent
    print("✓ app.agent imported successfully")
    
    # Check what root_agent contains
    root_agent = app.agent.root_agent
    print(f"root_agent tools count: {len(root_agent.tools)}")
    
    # List all tools
    for i, tool in enumerate(root_agent.tools):
        print(f"Tool {i+1}: {getattr(tool, 'name', 'Unknown')}")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
