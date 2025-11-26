from app.observability.tracing import tracer
import random
from datetime import datetime

def evaluate_threat_score(threat_data: str) -> str:
    trace_id = tracer.start_trace("Threat Scoring", "ThreatScorer")
    
    try:
        tracer.add_event("THREAT_SCORING_START", f"Evaluating threat: {threat_data[:100]}...")
        
        threat_lower = threat_data.lower()
        base_score = 50
        
        if 'critical' in threat_lower or 'cve-2021-44228' in threat_lower or 'ransomware' in threat_lower:
            base_score += 35
        elif 'exploit' in threat_lower or 'malware' in threat_lower:
            base_score += 25
        elif 'phishing' in threat_lower or 'brute force' in threat_lower:
            base_score += 20
            
        if 'failed' in threat_lower and 'login' in threat_lower:
            base_score += 15
            
        final_score = min(100, base_score + random.randint(-5, 10))
        
        if final_score >= 80:
            risk_level = "🔴 CRITICAL"
            recommendation = "Immediate action required. Isolate affected systems and begin incident response."
        elif final_score >= 60:
            risk_level = "🟠 HIGH" 
            recommendation = "Urgent investigation needed. Implement containment measures."
        elif final_score >= 40:
            risk_level = "🟡 MEDIUM"
            recommendation = "Monitor closely and plan remediation activities."
        else:
            risk_level = "🟢 LOW"
            recommendation = "Routine monitoring recommended."
        
        result = f"""# THREAT RISK ASSESSMENT
## Score: {final_score}/100
## Risk Level: {risk_level}

### Assessment Details
- **Threat Data Analyzed**: {len(threat_data)} characters
- **Assessment Time**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Key Indicators**: {', '.join([word for word in ['critical', 'exploit', 'malware', 'ransomware', 'phishing'] if word in threat_lower]) or 'General security event'}

### Recommendations
{recommendation}

### Next Steps
1. Validate threat indicators
2. Correlate with existing intelligence
3. Update security controls if needed
4. Document findings for future reference"""

        tracer.add_event("THREAT_SCORING_COMPLETE", f"Score: {final_score}/100 - {risk_level}")
        tracer.end_trace("completed")
        return result
        
    except Exception as e:
        tracer.add_event("THREAT_SCORING_ERROR", f"Error: {str(e)}")
        tracer.end_trace("failed", str(e))
        return f"Error evaluating threat score: {str(e)}"
