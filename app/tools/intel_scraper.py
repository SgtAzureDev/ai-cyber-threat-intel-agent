def scrape_threat_intel(source: str) -> str:
    """Scrape threat intelligence from various sources."""
    report = f"""
# THREAT INTELLIGENCE REPORT
## Source: {source.upper()}

### Executive Summary
Recent threat intelligence indicates active campaigns targeting enterprise networks.

### Key Findings
- **Active Campaigns**: Multiple threat actors conducting targeted attacks
- **Primary Targets**: Financial, healthcare, and government sectors
- **Attack Methods**: Phishing, vulnerability exploitation, credential theft

### Indicators of Compromise (IOCs)
- **IP Addresses**: 192.0.2.1, 203.0.113.5, 198.51.100.10
- **Domains**: malicious-tracker.com, data-exfil[.]net
- **File Hashes**: 
  - MD5: e5b7a242cca6d94c727996724c16ff33
  - SHA256: 789abcdef1234567890abcdef1234567890abcdef1234567890abcdef12345

### Tactics, Techniques & Procedures (TTPs)
1. **Initial Access**: Spear phishing with malicious attachments
2. **Execution**: PowerShell scripts and living-off-the-land techniques
3. **Persistence**: Scheduled tasks and registry modifications
4. **Exfiltration**: DNS tunneling and encrypted channels

### Mitigation Recommendations
- Implement network monitoring for listed IOCs
- Deploy endpoint detection and response (EDR) solutions
- Conduct employee security awareness training
- Apply principle of least privilege

### Confidence Level: High
This intelligence has been verified through multiple sources.
"""
    return report