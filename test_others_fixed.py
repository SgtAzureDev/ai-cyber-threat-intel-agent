# test_others_fixed.py
import sys
import os
sys.path.append(os.path.dirname(__file__))

print("Testing other imports...")

try:
    from app.observability.logs import setup_logging
    print("✅ setup_logging imported")
except ImportError as e:
    print(f"❌ setup_logging failed: {e}")

try:
    from app.evaluation.threat_scoring import evaluate_threat_score
    print("✅ evaluate_threat_score imported")
except ImportError as e:
    print(f"❌ evaluate_threat_score failed: {e}")

try:
    from app.middleware.system_prompt import get_enhanced_system_prompt
    print("✅ get_enhanced_system_prompt imported")
except ImportError as e:
    print(f"❌ get_enhanced_system_prompt failed: {e}")

try:
    from app.agents.reporter import generate_clean_report
    print("✅ generate_clean_report imported")
except ImportError as e:
    print(f"❌ generate_clean_report failed: {e}")
