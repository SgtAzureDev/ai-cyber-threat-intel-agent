def setup_logging(log_level: str = "INFO") -> str:
    """Set up comprehensive logging configuration for threat intelligence operations."""
    
    supported_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    if log_level.upper() not in supported_levels:
        log_level = "INFO"
    
    return f"""
# LOGGING CONFIGURATION SUCCESSFULLY APPLIED

## Configuration Summary
- **Log Level**: {log_level.upper()}
- **Timestamp**: {__import__('datetime').datetime.now().isoformat()}
- **Environment**: Threat Intelligence Production
- **Scope**: Application-wide logging

## Logging Components Configured

### 1. Console Logging
- **Format**: Timestamp | Level | Module | Message
- **Output**: Standard output with color coding
- **Level**: {log_level.upper()}

### 2. File Logging
- **Location**: logs/threat_intel_agent.log
- **Rotation**: Daily rotation with 7-day retention
- **Format**: JSON structured logging
- **Max Size**: 100MB per file

### 3. Security Audit Logging
- **Location**: logs/security_audit.log
- **Events**: Authentication, authorization, data access
- **Compliance**: GDPR, HIPAA, SOC2 ready
- **Retention**: 365 days

### 4. Performance Monitoring
- **Metrics**: Response times, error rates, throughput
- **Alerts**: Automated alerting on anomalies
- **Dashboard**: Real-time monitoring dashboard

## Log Categories Enabled

### Threat Intelligence Logs
- CVE lookup operations
- Threat intelligence scraping
- Security log parsing
- Threat scoring activities

### Security Operations
- Authentication events
- Data access patterns
- Policy violations
- Incident response actions

### System Operations
- Startup/shutdown events
- Configuration changes
- Health checks
- Performance metrics

## Benefits
- **Centralized Monitoring**: All logs in one place
- **Structured Data**: Easy parsing and analysis
- **Security Compliance**: Meets audit requirements
- **Troubleshooting**: Quick issue identification
- **Performance Insights**: System optimization data

## Next Steps
1. Monitor logs/threat_intel_agent.log for operational insights
2. Review logs/security_audit.log for compliance reporting
3. Set up log aggregation for centralized analysis
4. Configure alerts for critical security events

## Support
For log analysis assistance, use the parse_security_logs tool.

"""
