from app.observability.tracing import tracer
import re
from datetime import datetime

def parse_security_logs(log_data: str) -> str:
    """Parse and analyze security logs for threats"""
    trace_id = tracer.start_trace("Log Analysis", "LogParser")
    
    try:
        tracer.add_event("LOG_PARSE_START", f"Parsing {len(log_data)} characters of log data")
        
        findings = {
            "failed_logins": 0,
            "suspicious_ips": [],
            "error_patterns": [],
            "successful_logins": 0,
            "security_events": []
        }
        
        lines = log_data.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            if any(pattern in line.lower() for pattern in ['failed', 'denied', 'invalid', 'unauthorized']):
                findings["failed_logins"] += 1
                findings["security_events"].append(f"Failed authentication: {line}")
                
                ip_match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
                if ip_match and ip_match.group() not in findings["suspicious_ips"]:
                    findings["suspicious_ips"].append(ip_match.group())
            
            elif any(pattern in line.lower() for pattern in ['success', 'accepted', 'authenticated']):
                findings["successful_logins"] += 1
            
            elif any(pattern in line.lower() for pattern in ['error', 'exception', 'timeout', 'crash']):
                findings["error_patterns"].append(line)
        
        result = f"""# SECURITY LOG ANALYSIS REPORT
## Analysis Summary
**Log Entries Processed**: {len(lines)}
**Analysis Timestamp**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Key Findings
- **Failed Login Attempts**: {findings['failed_logins']}
- **Successful Logins**: {findings['successful_logins']}
- **Suspicious IPs Detected**: {len(findings['suspicious_ips'])}
- **Error Patterns Found**: {len(findings['error_patterns'])}

## Detailed Analysis"""

        if findings['suspicious_ips']:
            result += "\n### Suspicious IP Addresses:\n"
            for ip in findings['suspicious_ips']:
                result += f"- {ip}\n"

        if findings['failed_logins'] > 5:
            result += f"\n### ⚠️ SECURITY ALERT\nHigh number of failed logins ({findings['failed_logins']}) detected. Possible brute force attack."

        if findings['error_patterns']:
            result += "\n### Error Patterns:\n"
            for error in findings['error_patterns'][:5]:  
                result += f"- {error}\n"

        if not any([findings['failed_logins'], findings['suspicious_ips'], findings['error_patterns']]):
            result += "\n### ✅ No significant security issues detected in provided logs."

        tracer.add_event("LOG_PARSE_COMPLETE", f"Found {findings['failed_logins']} failed logins, {len(findings['suspicious_ips'])} suspicious IPs")
        tracer.end_trace("completed")
        return result
        
    except Exception as e:
        tracer.add_event("LOG_PARSE_ERROR", f"Error: {str(e)}")
        tracer.end_trace("failed", str(e))
        return f"Error parsing logs: {str(e)}"
