import sys
import os
sys.path.append('.')

def verify_tools():
    print("=== Verifying Tools in root_agent ===")
    
    try:
        from app.agent import root_agent
        
        print(f"Agent name: {root_agent.name}")
        print(f"Number of tools: {len(root_agent.tools)}")
        print("Available tools:")
        
        for i, tool in enumerate(root_agent.tools):
            tool_name = getattr(tool, 'name', 'Unknown')
            print(f"  {i+1}. {tool_name}")
            
        # Check if our specific tools are present
        tool_names = [getattr(tool, 'name', '') for tool in root_agent.tools]
        expected_tools = ['cve_lookup', 'scrape_threat_intel', 'parse_security_logs', 'get_system_prompt', '_threat_pipeline']
        
        print("\nChecking for expected tools:")
        for expected_tool in expected_tools:
            if expected_tool in tool_names:
                print(f"  ✓ {expected_tool} - FOUND")
            else:
                print(f"  ✗ {expected_tool} - MISSING")
                
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    verify_tools()
