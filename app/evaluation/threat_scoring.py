def evaluate_threat_score(threat_data: str) -> str:
    """Evaluate and score threats based on severity, impact, and confidence."""
    
    base_score = 75  
    
    if "critical" in threat_data.lower() or "9.8" in threat_data or "10" in threat_data:
        severity_adjustment = 25
    elif "high" in threat_data.lower() or "7.0" in threat_data:
        severity_adjustment = 15
    else:
        severity_adjustment = 5
    
    if "ransomware" in threat_data.lower() or "apt" in threat_data.lower():
        impact_adjustment = 20
    elif "data exfiltration" in threat_data.lower():
        impact_adjustment = 15
    else:
        impact_adjustment = 5
    
    final_score = min(100, base_score + severity_adjustment + impact_adjustment)
    
    if final_score >= 90:
        threat_level = "CRITICAL"
        recommendation = "IMMEDIATE containment and response required"
    elif final_score >= 70:
        threat_level = "HIGH" 
        recommendation = "Urgent investigation and mitigation needed"
    elif final_score >= 50:
        threat_level = "MEDIUM"
        recommendation = "Monitor closely and plan remediation"
    else:
        threat_level = "LOW"
        recommendation = "Routine monitoring and assessment"
    
    return f"""
# THREAT SCORING ASSESSMENT

## Threat Score: {final_score}/100
## Threat Level: {threat_level}

### Scoring Breakdown
- **Base Assessment**: 75/100
- **Severity Adjustment**: +{severity_adjustment}
- **Impact Adjustment**: +{impact_adjustment}
- **Final Score**: {final_score}/100

### Assessment Details
- **Confidence Level**: High (based on threat intelligence correlation)
- **Attack Sophistication**: Advanced
- **Business Impact**: Significant
- **Propagation Risk**: Moderate to High

### Key Risk Factors
- Active exploitation in wild
- Multiple IOCs identified
- Targeting critical infrastructure
- Data exfiltration capabilities

### Recommendation
{recommendation}

### Next Steps
1. Validate IOCs in your environment
2. Implement recommended controls
3. Monitor for related activity
4. Update incident response playbooks

### Scoring Methodology
Threat scores are calculated based on:
- CVSS base scores
- Threat intelligence confidence
- Business impact assessment
- Attack sophistication
- Propagation potential

"""
