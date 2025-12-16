import threading

class Nexus:
    def __init__(self):
        self.knowledge = {
            "technologies": set(),
            "confirmed_vulns": [],
            "failed_vectors": [],
            "waf_patterns": set(),
            "response_times": []
        }
        self.lock = threading.Lock()

    def ingest_intel(self, url, headers, body):
        with self.lock:
            h_str, body_str = str(headers).lower(), str(body).lower()
            tech_map = {
                'PHP': ['php', 'x-powered-by: php', '.php'],
                'ASP.NET': ['asp.net', 'x-aspnet-version', '.aspx'],
                'Node.js': ['x-powered-by: express', 'node.js'],
                'Java': ['jsessionid', 'servlet', 'jsp'],
                'Python': ['python', 'django', 'flask'],
                'Nginx': ['nginx'], 'Apache': ['apache'], 'IIS': ['microsoft-iis']
            }
            for tech, indicators in tech_map.items():
                if any(ind in h_str or ind in body_str for ind in indicators):
                    self.knowledge['technologies'].add(tech)
            if 'wordpress' in body_str: self.knowledge['technologies'].add('WordPress')

    def record_kill(self, vuln_data):
        with self.lock:
            self.knowledge['confirmed_vulns'].append(vuln_data)
            print(f"[NEXUS] KILL CONFIRMED: {vuln_data['type']} at {vuln_data['target']}")

    def record_waf(self, pattern):
        with self.lock: self.knowledge['waf_patterns'].add(pattern)

    def get_tech_context(self):
        with self.lock: return list(self.knowledge['technologies'])
