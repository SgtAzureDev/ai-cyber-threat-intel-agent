# test_memory_fixed.py
import sys
import os
sys.path.append(os.path.dirname(__file__))

print("Testing memory imports...")

try:
    from app.memory.longterm_memory import store_threat_intel
    print("✅ store_threat_intel imported")
except ImportError as e:
    print(f"❌ store_threat_intel failed: {e}")

try:
    from app.memory.session_store import store_session
    print("✅ store_session imported")
except ImportError as e:
    print(f"❌ store_session failed: {e}")
