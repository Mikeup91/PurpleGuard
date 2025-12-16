import sys
import time
import random
import requests
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from evolution.nexus import Nexus
from core.spider import DeepSpider
from core.mutator import MutationLab
from modules.vectors import VectorSQLi, VectorXSS, VectorLFI, VectorSSRF
from modules.reporter import AuditReporter

class OmnibusEngine:
    def __init__(self, targets, max_threads=10):
        self.targets = targets if isinstance(targets, list) else [targets]
        self.nexus = Nexus()
        self.spider = DeepSpider(self.nexus)
        self.mutator = MutationLab()
        self.session = requests.Session()
        self.max_threads = max_threads
        self.vectors = [VectorSQLi(), VectorXSS(), VectorLFI(), VectorSSRF()]
        self.reporter = AuditReporter(self.nexus)

    def engage(self):
        print("\n[!] SWARM STARTING - AGGRESSIVE MODE")
        for target in self.targets:
            print(f"[*] Targeting: {target}")
            endpoints = self.spider.crawl(target)
            if not endpoints: continue
            
            tasks = []
            for ep in endpoints:
                for vector in self.vectors:
                    payloads = vector.payloads(self.nexus)
                    for raw_pl in payloads:
                        variants = self.mutator.generate_variants(raw_pl, vector.name())
                        for final_pl in variants[:2]:
                            param = ep.get('params', ['id'])[0] if ep.get('params') else 'id'
                            tasks.append((ep, param, final_pl, vector.name()))
            
            with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
                futures = [executor.submit(self._fire, e, p, pl, v) for e, p, pl, v in tasks]
                for f in as_completed(futures):
                    try: f.result()
                    except: pass
        
        # This is the line that creates the file
        self.reporter.generate_markdown()

    def _fire(self, ep, param, payload, v_type):
        try:
            start = time.time()
            resp = self.session.get(ep['url'], params={param: payload}, timeout=5)
            dur = time.time() - start
            
            if v_type == "SQLi":
                if dur > 4 or any(x in resp.text.lower() for x in ['mysql', 'sql syntax', 'error']):
                    self.nexus.record_kill({"target": ep['url'], "type": v_type, "param": param, "payload": payload, "confidence": 95})
            elif v_type == "XSS" and (payload in resp.text or "<script>" in resp.text.lower()):
                self.nexus.record_kill({"target": ep['url'], "type": v_type, "param": param, "payload": payload, "confidence": 85})
            elif v_type == "LFI" and any(i in resp.text for i in ['root:', 'bin:']):
                self.nexus.record_kill({"target": ep['url'], "type": v_type, "param": param, "payload": payload, "confidence": 100})
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
            if v_type == "SQLi" and 'sleep' in payload.lower():
                self.nexus.record_kill({"target": ep['url'], "type": v_type, "param": param, "payload": payload, "confidence": 90, "status": "TIMEOUT_MATCH"})
        except: pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        engine = OmnibusEngine(sys.argv[1])
        engine.engage()

    def sync_to_platform(self):
        import json
        data = {
            "last_scan": time.ctime(),
            "total_kills": len(self.nexus.knowledge.get('confirmed_vulns', [])),
            "findings": self.nexus.knowledge.get('confirmed_vulns', [])
        }
        # Path adjusted for your repo structure (writing to root metadata.json)
        try:
            with open("metadata.json", "w") as f:
                json.dump(data, f, indent=4)
            print(f"[+] PurpleGuard Platform Synced: metadata.json updated.")
        except Exception as e:
            print(f"[-] Sync Failed: {e}")
