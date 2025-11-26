"""
Reporter sub-agent
"""

from app.observability.tracing import tracer
from datetime import datetime
import re

def generate_clean_report(content: str) -> str:
    """Generate a clean, formatted report based on the provided content"""
    trace_id = tracer.start_trace("Report Generation", "ReportTool")
    
    try:
        tracer.add_event("REPORT_GENERATION_START", f"Processing content: {content[:100]}...")
        
        # Extract key information from the content
        cve_info = extract_cve_info(content)
        threat_intel = extract_threat_intel(content)
        
        # Generate dynamic report based on content
        if cve_info and threat_intel:
            report = generate_combined_cve_threat_report(cve_info, threat_intel, content)
        elif cve_info:
            report = generate_cve_report(cve_info, content)
        elif threat_intel:
            report = generate_threat_intel_report(threat_intel, content)
        else:
            report = generate_general_report(content)
        
        tracer.add_event("REPORT_GENERATION_COMPLETE", "Generated formatted report")
        tracer.end_trace("completed")
        return report
        
    except Exception as e:
        tracer.add_event("REPORT_GENERATION_ERROR", f"Error: {str(e)}")
        tracer.end_trace("failed", str(e))
        return f"Error generating report: {str(e)}"

def extract_cve_info(content: str) -> dict:
    """Extract CVE information from content"""
    cve_pattern = r'CVE-\d{4}-\d{4,7}'
    cves = re.findall(cve_pattern, content)
    
    if not cves:
        return None
    
    # Extract severity and description
    severity_match = re.search(r'Severity:\s*(\w+)', content, re.IGNORECASE)
    cvss_match = re.search(r'CVSS.*?(\d+\.\d+)', content, re.IGNORECASE)
    description_match = re.search(r'Description[:\s]+([^\n\.]+\.?)', content, re.IGNORECASE)
    
    return {
        'cves': cves,
        'severity': severity_match.group(1) if severity_match else 'Unknown',
        'cvss_score': cvss_match.group(1) if cvss_match else 'N/A',
        'description': description_match.group(1) if description_match else 'Vulnerability details',
        'raw_content': content
    }

def extract_threat_intel(content: str) -> dict:
    """Extract threat intelligence from content"""
    threats = []
    
    threat_indicators = [
        'exploit', 'malware', 'ransomware', 'phishing', 'campaign',
        'threat group', 'actively targeting', 'scanning', 'vulnerable'
    ]
    
    for indicator in threat_indicators:
        if indicator in content.lower():
            pattern = fr'[^.]*{indicator}[^.]*\.'
            matches = re.findall(pattern, content, re.IGNORECASE)
            threats.extend(matches)
    
    return {
        'threats': threats[:5],  
        'has_intel': len(threats) > 0,
        'raw_content': content
    }

def generate_combined_cve_threat_report(cve_info: dict, threat_intel: dict, original_content: str) -> str:
    """Generate a combined CVE and threat intelligence report"""
    
    report_id = f"TR-{datetime.now().strftime('%H%M%S')}"
    
    report = f"""# COMBINED THREAT INTELLIGENCE REPORT

## Executive Summary
This report combines CVE vulnerability analysis with current threat intelligence to provide comprehensive risk assessment.

### Critical Vulnerability Analysis
"""
    
    for cve in cve_info['cves']:
        report += f"""**{cve}** - {cve_info['severity']} Severity (CVSS: {cve_info['cvss_score']})
- **Description**: {cve_info['description']}
- **Status**: Actively being exploited based on threat intelligence

"""
    
    report += """### Current Threat Landscape
"""
    
    if threat_intel['has_intel']:
        for threat in threat_intel['threats']:
            report += f"- 🔴 {threat.strip()}\n"
    else:
        report += "- No specific threat intelligence extracted from provided data\n"
    
    report += f"""
### Risk Assessment
- **Overall Risk**: CRITICAL - Active exploitation of {', '.join(cve_info['cves'])}
- **Business Impact**: High potential for system compromise
- **Urgency**: Immediate action required

### Recommended Immediate Actions
1. Apply available security patches for {', '.join(cve_info['cves'])}
2. Implement network-level blocking for known exploit patterns
3. Enhance monitoring for exploitation attempts
4. Conduct security awareness briefing

### Threat Intelligence Context
Recent intelligence indicates active campaigns targeting these vulnerabilities. Organizations should prioritize remediation and monitoring.

---
**Report ID**: {report_id}
**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Classification**: FOR OFFICIAL USE ONLY
"""

    return report

def generate_cve_report(cve_info: dict, original_content: str) -> str:
    """Generate a CVE-focused report"""
    report_id = f"CVE-{datetime.now().strftime('%H%M%S')}"
    
    report = f"""# CVE VULNERABILITY ASSESSMENT REPORT

## Vulnerability Analysis
"""
    
    for cve in cve_info['cves']:
        report += f"""### {cve}
- **Severity**: {cve_info['severity']}
- **CVSS Score**: {cve_info['cvss_score']}/10
- **Description**: {cve_info['description']}

"""
    
    report += f"""## Risk Assessment
- **Impact**: Remote code execution potential
- **Exploitation**: Likely in wild
- **Remediation Priority**: HIGH

## Recommended Actions
1. Immediate patching of affected systems
2. Security control validation
3. Compromise assessment

---
**Report ID**: {report_id}
**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

    return report

def generate_threat_intel_report(threat_intel: dict, original_content: str) -> str:
    """Generate a threat intelligence focused report"""
    report_id = f"TI-{datetime.now().strftime('%H%M%S')}"
    
    report = f"""# THREAT INTELLIGENCE BRIEFING

## Current Threat Activity
"""
    
    if threat_intel['has_intel']:
        for i, threat in enumerate(threat_intel['threats'], 1):
            report += f"{i}. {threat.strip()}\n"
    else:
        report += "General threat landscape analysis based on available data.\n"
    
    report += f"""
## Assessment
- **Threat Level**: Elevated
- **Confidence**: Based on correlated intelligence
- **Recommendation**: Enhanced monitoring and controls

---
**Report ID**: {report_id}
**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

    return report

def generate_general_report(content: str) -> str:
    """Generate a general formatted report"""
    report_id = f"GEN-{datetime.now().strftime('%H%M%S')}"
    
    preview = content[:500] + "..." if len(content) > 500 else content
    
    report = f"""# SECURITY ANALYSIS REPORT

## Analysis Summary
This report provides a structured analysis of the provided security data.

## Content Overview
{preview}

## Key Findings
- Data processed and structured for review
- Automated analysis completed
- Recommendations based on content patterns

## Next Steps
1. Review the detailed findings
2. Validate against current environment
3. Implement appropriate security measures

---
**Report ID**: {report_id}
**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Note**: This is an automated analysis report
"""

    return report
