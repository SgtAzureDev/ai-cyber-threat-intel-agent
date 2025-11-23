import sys
import os
sys.path.append('.')

def check_agent_tools():
    """Check what tools are available in the agent"""
    try:
        from app.agent import agent
        print("=== Agent Tools Debug ===")
        print(f"Agent name: {agent.name}")
        print(f"Agent instructions: {agent.instructions[:100]}...")
        
        # Check available tools
        if hasattr(agent, 'tools'):
            print(f"Number of tools: {len(agent.tools)}")
            for i, tool in enumerate(agent.tools):
                print(f"Tool {i+1}: {getattr(tool, 'name', 'Unknown')}")
        else:
            print("No tools found in agent")
            
    except Exception as e:
        print(f"Error loading agent: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    check_agent_tools()
