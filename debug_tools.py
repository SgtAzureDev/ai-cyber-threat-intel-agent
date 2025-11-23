import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

print("=== Debugging tools imports ===")

# Test importing the modules directly
try:
    import app.tools.cve_lookup as cve_module
    print("✓ cve_lookup module imported")
    print(f"  Functions in module: {[x for x in dir(cve_module) if not x.startswith('_')]}")
except Exception as e:
    print(f"✗ cve_lookup module import failed: {e}")

try:
    import app.tools.intel_scraper as intel_module
    print("✓ intel_scraper module imported")
    print(f"  Functions in module: {[x for x in dir(intel_module) if not x.startswith('_')]}")
except Exception as e:
    print(f"✗ intel_scraper module import failed: {e}")

try:
    import app.tools.log_parser as log_module
    print("✓ log_parser module imported")
    print(f"  Functions in module: {[x for x in dir(log_module) if not x.startswith('_')]}")
except Exception as e:
    print(f"✗ log_parser module import failed: {e}")

try:
    import app.tools.system_prompt_tool as prompt_module
    print("✓ system_prompt_tool module imported")
    print(f"  Functions in module: {[x for x in dir(prompt_module) if not x.startswith('_')]}")
except Exception as e:
    print(f"✗ system_prompt_tool module import failed: {e}")
