import sys
import os

# Add current directory to path
sys.path.append('.')

def test_tools_in_adk_format():
    """Test if tools work in ADK format"""
    print("=== Testing Tools in ADK Format ===\n")
    
    # Test cve_lookup
    try:
        from app.tools.cve_lookup import cve_lookup
        result = cve_lookup("CVE-2021-44228")
        print("✓ cve_lookup tool works")
        print(f"  Result: {result}\n")
    except Exception as e:
        print(f"✗ cve_lookup failed: {e}\n")
    
    # Test threat intel scraper
    try:
        from app.tools.intel_scraper import scrape_threat_intel
        result = scrape_threat_intel("alienvault")
        print("✓ scrape_threat_intel tool works")
        print(f"  Result: {result}\n")
    except Exception as e:
        print(f"✗ scrape_threat_intel failed: {e}\n")
    
    # Test log parser
    try:
        from app.tools.log_parser import parse_security_logs
        result = parse_security_logs("sample log data")
        print("✓ parse_security_logs tool works")
        print(f"  Result: {result}\n")
    except Exception as e:
        print(f"✗ parse_security_logs failed: {e}\n")
    
    # Test system prompt
    try:
        from app.tools.system_prompt_tool import get_system_prompt
        result = get_system_prompt()
        print("✓ get_system_prompt tool works")
        print(f"  Result length: {len(result)} characters\n")
    except Exception as e:
        print(f"✗ get_system_prompt failed: {e}\n")

if __name__ == "__main__":
    test_tools_in_adk_format()
