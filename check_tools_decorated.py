import sys
import os
sys.path.append('.')

def check_tools():
    print("=== Checking Tool Decorations ===")
    
    tools_to_check = [
        'app.tools.cve_lookup',
        'app.tools.intel_scraper',
        'app.tools.log_parser',
        'app.tools.system_prompt_tool'
    ]
    
    for tool_module in tools_to_check:
        try:
            module = __import__(tool_module, fromlist=['*'])
            functions = [attr for attr in dir(module) if not attr.startswith('_')]
            print(f"{tool_module}: {functions}")
            
            for func_name in functions:
                func = getattr(module, func_name)
                if hasattr(func, '_is_tool'):
                    print(f"  ✓ {func_name} is decorated with @tool")
                else:
                    print(f"  ✗ {func_name} is NOT decorated with @tool")
                    
        except Exception as e:
            print(f"Error checking {tool_module}: {e}")

if __name__ == "__main__":
    check_tools()
