"""
Threat intake sub-agent + helper utilities.
- Provides a IOC extractor and normalization.
"""

import re
from typing import Dict, List
from google.adk.agents.llm_agent import LlmAgent

_RE_IPV4 = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
_RE_DOMAIN = re.compile(
    r"\b((?:[a-zA-Z0-9\-]+\.)+(?:[a-zA-Z]{2,63}))\b"
)
_RE_SHA256 = re.compile(r"\b[a-fA-F0-9]{64}\b")
_RE_SHA1 = re.compile(r"\b[a-fA-F0-9]{40}\b")
_RE_MD5 = re.compile(r"\b[a-fA-F0-9]{32}\b")
_RE_URL = re.compile(r"\bhttps?://[^\s,;]+", re.IGNORECASE)

def normalize_text(text: str) -> str:
    s = " ".join(text.split())
    return s.strip()

def extract_iocs(text: str) -> Dict[str, List[str]]:
    t = text or ""
    ips = _RE_IPV4.findall(t)
    urls = _RE_URL.findall(t)
    domains = _RE_DOMAIN.findall(t)
    sha256 = _RE_SHA256.findall(t)
    sha1 = _RE_SHA1.findall(t)
    md5 = _RE_MD5.findall(t)

    def _uniq(seq):
        seen = set()
        out = []
        for item in seq:
            if item not in seen:
                seen.add(item)
                out.append(item)
        return out

    return {
        "ips": _uniq(ips),
        "urls": _uniq(urls),
        "domains": _uniq(domains),
        "sha256": _uniq(sha256),
        "sha1": _uniq(sha1),
        "md5": _uniq(md5),
    }

intake_agent = LlmAgent(
    name="ThreatIntakeAgent",
    model="gemini-2.0-flash",
)

