from app.observability.tracing import tracer
import random
from datetime import datetime

def scrape_threat_intel(topic: str) -> str:
    """Scrape threat intelligence about specific topics"""
    trace_id = tracer.start_trace(f"Threat Intel: {topic}", "IntelScraper")
    
    try:
        tracer.add_event("INTEL_SCRAPE_START", f"Scraping intelligence about {topic}")        
        threat_data = {
            "ransomware": [
                "LockBit 3.0 actively targeting healthcare sector",
                "BlackCat ransomware using new encryption methods",
                "Clop ransomware exploiting MOVEit vulnerabilities"
            ],
            "phishing": [
                "Microsoft 365 credential phishing campaigns increased 45%",
                "Multi-factor authentication bypass techniques being deployed",
                "Business email compromise targeting financial departments"
            ],
            "log4j": [
                "Multiple threat groups exploiting CVE-2021-44228",
                "New Log4Shell variants bypassing traditional defenses",
                "Botnets actively scanning for vulnerable Log4j instances"
            ],
            "malware": [
                "Emotet resurgence with new delivery mechanisms",
                "QakBot infrastructure rebuilding after takedown",
                "InfoStealers targeting cryptocurrency wallets"
            ]
        }
        
        topic_lower = topic.lower()
        result = f"# THREAT INTELLIGENCE REPORT\n## Topic: {topic}\n### Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        
        if any(keyword in topic_lower for keyword in ['ransomware', 'malware', 'phishing', 'log4j']):
            for key, threats in threat_data.items():
                if key in topic_lower:
                    result += f"### Recent {key.title()} Threats:\n"
                    for threat in threats:
                        result += f"- 🔴 {threat}\n"
                    break
            else:
                # Default to general threats
                result += "### Current Cyber Threat Landscape:\n"
                for key, threats in threat_data.items():
                    result += f"#### {key.title()}:\n"
                    for threat in threats[:2]:
                        result += f"- {threat}\n"
        else:
            result += "### General Threat Intelligence:\n"
            result += "- Increased state-sponsored cyber espionage activities\n"
            result += "- Supply chain attacks targeting software dependencies\n"
            result += "- Cloud infrastructure misconfigurations leading to data breaches\n"
            result += "- AI-powered social engineering campaigns\n"
        
        result += f"\n**Source**: Simulated OSINT aggregation"
        
        tracer.add_event("INTEL_SCRAPE_COMPLETE", f"Scraped {topic} intelligence")
        tracer.end_trace("completed")
        return result
        
    except Exception as e:
        tracer.add_event("INTEL_SCRAPE_ERROR", f"Error: {str(e)}")
        tracer.end_trace("failed", str(e))
        return f"Error scraping threat intelligence: {str(e)}"
