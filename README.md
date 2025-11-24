# AI Cyber Threat Intelligence Agent
# Google AI Agents Intensive Capstone Project

## Overview
In today's rapidly evolving threat landscape, security operations centers (SOCs) face overwhelming volumes of security data and alerts. This AI-powered threat intelligence agent automates critical aspects of threat investigation, correlation, and reporting, reducing mean time to detection (MTTD) and enabling security teams to focus on high value analysis.

## The Challenge
**Security analysts typically spend hours manually:**
- Researching CVEs and vulnerability impacts
- Correlating threat indicators across multiple sources
- Investigating security incidents across disparate log sources
- Documenting findings for compliance and reporting
**This agent streamlines these workflows through intelligent automation while maintaining the context and precision required for enterprise security operations.**

## Technical Architecture
### Core Agent Framework
Primary Intelligence Engine: ThreatIntelAgent powered by Gemini 2.0 Flash
Modular Processing Pipeline: Specialized sub-agents for discrete analysis phases. Threat Intake, Analyzer, Reporter
Extensible Tool Ecosystem: Purpose-built security tools for common investigation tasks.  CVE lookup, threat intel scraping, log parsing
Memory storing: Session storage + long-term threat intelligence storage

## Key Features Demonstrated
1. **Threat Intelligence Gathering**: Automated OSINT collection and correlation
2. **Vulnerability Assessment**: Real-time CVE analysis and impact assessment
3. **Security Log Analysis**: Pattern recognition across diverse log formats
4. **Investigation Memory**: Persistent session context and historical intelligence
5. **Processing Window**: Threat Intake → IOC Extraction → Threat Scoring → Intelligence Reporting

## Enterprise Features
- Session persistence for complex investigations
- Configurable analysis pipelines
- Extensible architecture for organization-specific requirements

## Project Value
### For Security Teams
- 60-80% reduction in initial investigation time
- Consistent threat analysis methodology
- Automated documentation and reporting
- Scalable to handle increasing alert volumes

### For Organizations
- Improved security posture through faster response
- Reduced operational costs for tier-1 analysis
- Audit-ready investigation documentation
- Knowledge retention through investigation memory

## Technical Requirements
Python 3.13.9 (venv)
Google ADK Framework
Gemini API Access (GoogleAIStudio)

## Deployment
### Clone repository
```bash
  git clone https://github.com/SgtAzureDev/ai-cyber-threat-intel-agent.git
```
### Install dependencies 
```bash
  pip install -r requirements.txt
```
### Google AI Studio API Key in .env file

### Launch web interface
```bash
  adk web .
```

## Demo
link to demo

## Usage/Examples
```bash
example queries
```
