import time
import json
from datetime import datetime
from typing import Dict, Any, List

class AgentTracer:
    def __init__(self):
        self.traces = []
        self.current_trace_id = None
    
    def start_trace(self, operation: str, agent_name: str = "ThreatIntelAgent"):
        trace_id = f"trace_{int(time.time())}_{len(self.traces)}"
        self.current_trace_id = trace_id
        
        trace = {
            "trace_id": trace_id,
            "operation": operation,
            "agent": agent_name,
            "start_time": datetime.now().isoformat(),
            "events": [],
            "status": "started"
        }
        
        self.traces.append(trace)
        self.add_event("TRACE_START", f"Started {operation}")
        return trace_id
    
    def add_event(self, event_type: str, details: str, metadata: Dict = None):
        if not self.current_trace_id:
            return
        
        event = {
            "timestamp": datetime.now().isoformat(),
            "event_type": event_type,
            "details": details,
            "metadata": metadata or {}
        }
        
        for trace in self.traces:
            if trace["trace_id"] == self.current_trace_id:
                trace["events"].append(event)
                break
    
    def end_trace(self, status: str = "completed", error: str = None):
        if not self.current_trace_id:
            return
        
        for trace in self.traces:
            if trace["trace_id"] == self.current_trace_id:
                trace["end_time"] = datetime.now().isoformat()
                trace["status"] = status
                if error:
                    trace["error"] = error
                self.add_event("TRACE_END", f"Trace {status}")
                break
        
        self.current_trace_id = None
    
    def get_traces(self) -> List[Dict]:
        return self.traces
    
    def get_trace_by_id(self, trace_id: str) -> Dict:
        for trace in self.traces:
            if trace["trace_id"] == trace_id:
                return trace
        return {}

tracer = AgentTracer()

def get_agent_traces() -> str:
    traces = tracer.get_traces()
    if not traces:
        return "No traces available"
    
    result = f"## Agent Tracing Dashboard\n\n"
    result += f"**Total Traces:** {len(traces)}\n\n"
    
    for trace in traces[-5:]:  
        duration = "N/A"
        if 'end_time' in trace:
            start = datetime.fromisoformat(trace['start_time'])
            end = datetime.fromisoformat(trace['end_time'])
            duration = f"{(end - start).total_seconds():.2f}s"
        
        result += f"### 🔍 {trace['operation']}\n"
        result += f"- **Trace ID:** {trace['trace_id']}\n"
        result += f"- **Agent:** {trace['agent']}\n"
        result += f"- **Status:** {trace['status']}\n"
        result += f"- **Duration:** {duration}\n"
        result += f"- **Events:** {len(trace['events'])}\n"
        
        for event in trace['events'][-3:]:
            result += f"  - {event['timestamp'][11:19]} {event['event_type']}: {event['details']}\n"
        
        result += "\n"
    
    return result
