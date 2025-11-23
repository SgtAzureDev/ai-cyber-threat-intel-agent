# test_tools_fixed.py
import sys
import os
sys.path.append(os.path.dirname(__file__))

print("Testing tools imports...")

try:
    from app.tools.cve_lookup import cve_lookup
    print("✅ cve_lookup imported")
except ImportError as e:
    print(f"❌ cve_lookup failed: {e}")

try:
    from app.tools.intel_scraper import scrape_threat_intel
    print("✅ scrape_threat_intel imported")
except ImportError as e:
    print(f"❌ scrape_threat_intel failed: {e}")

try:
    from app.tools.log_parser import parse_security_logs
    print("✅ parse_security_logs imported")
except ImportError as e:
    print(f"❌ parse_security_logs failed: {e}")

try:
    from app.tools.system_prompt_tool import get_system_prompt
    print("✅ get_system_prompt imported")
except ImportError as e:
    print(f"❌ get_system_prompt failed: {e}")
