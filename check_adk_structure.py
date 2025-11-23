import sys
import os
sys.path.append('.')

def check_adk_compatibility():
    """Check if tools are ADK compatible"""
    print("=== Checking ADK Compatibility ===\n")
    
    # Check if we can import as ADK tools
    try:
        # Try to import the tools module
        import app.tools as tools_module
        print("✓ Tools module imports successfully")
        
        # Check what's available
        available_tools = [attr for attr in dir(tools_module) if not attr.startswith('_')]
        print(f"  Available tools: {available_tools}")
        
        # Test each tool
        for tool_name in available_tools:
            try:
                tool_func = getattr(tools_module, tool_name)
                if callable(tool_func):
                    print(f"  ✓ {tool_name} is callable")
                    # Test with sample input
                    if tool_name == 'get_system_prompt':
                        result = tool_func()
                    else:
                        result = tool_func("test_input")
                    print(f"    Returns: {type(result).__name__}")
                else:
                    print(f"  ✗ {tool_name} is not callable")
            except Exception as e:
                print(f"  ✗ {tool_name} test failed: {e}")
                
    except Exception as e:
        print(f"✗ Tools module import failed: {e}")

if __name__ == "__main__":
    check_adk_compatibility()
