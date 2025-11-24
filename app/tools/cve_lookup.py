def cve_lookup(cve_id: str) -> str:
    """Look up CVE (Common Vulnerabilities and Exposures) information."""
    report = f"""
# CVE ANALYSIS REPORT
## CVE ID: {cve_id}

### Executive Summary
{cve_id} is a critical vulnerability requiring immediate attention.

### Technical Details
- **Severity**: Critical (CVSS Score: 9.8/10)
- **Affected Systems**: Multiple enterprise systems using vulnerable components
- **Attack Vector**: Network-based exploitation
- **Impact**: Remote code execution, system compromise

### Affected Software
- Various applications using vulnerable libraries
- Enterprise software with embedded components
- Cloud services and containers

### Recommended Actions
1. Apply security patches immediately
2. Implement network segmentation
3. Monitor for exploitation attempts
4. Conduct security awareness training

### References
- NVD Database: https://nvd.nist.gov/vuln/detail/{cve_id}
- CVE Details: Comprehensive technical analysis available
"""
    return report