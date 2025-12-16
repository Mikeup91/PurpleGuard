import json
import time

class AuditReporter:
    def __init__(self, nexus):
        self.nexus = nexus

    def generate_markdown(self, filename="audit_report.md"):
        vulns = self.nexus.knowledge.get('confirmed_vulns', [])
        tech = list(self.nexus.knowledge.get('technologies', []))
        
        with open(filename, "w") as f:
            f.write(f"# PURPLE GUARD SECURITY AUDIT\n")
            f.write(f"**Date:** {time.ctime()}\n\n")
            f.write(f"## 1. Technical Stack\n")
            f.write(f"- Identified: {', '.join(tech) if tech else 'Unknown'}\n\n")
            f.write(f"## 2. Vulnerability Summary\n")
            f.write(f"| Type | Target URL | Parameter | Confidence |\n")
            f.write(f"| :--- | :--- | :--- | :--- |\n")
            for v in vulns:
                f.write(f"| {v['type']} | {v['target']} | {v.get('param', 'N/A')} | {v.get('confidence', 100)}% |\n")
            
            f.write(f"\n## 3. Evidence Log\n")
            for i, v in enumerate(vulns):
                f.write(f"### Finding {i+1}: {v['type']}\n")
                f.write(f"- **URL:** {v['target']}\n")
                f.write(f"- **Payload:** `{v['payload']}`\n")
                if 'status' in v: f.write(f"- **Note:** {v['status']}\n")
                f.write(f"---\n")
        
        print(f"\n[+] Professional Audit Report Generated: {filename}")
