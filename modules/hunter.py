import requests
import dns.resolver
from urllib.parse import urlparse

class TargetHunter:
    def discover_from_domain(self, domain):
        targets = {f"https://{domain}", f"http://{domain}"}
        common_subs = ['www', 'api', 'dev', 'staging', 'admin']
        for sub in common_subs:
            targets.add(f"http://{sub}.{domain}")
        try:
            answers = dns.resolver.resolve(domain, 'A')
            for ip in answers:
                targets.add(f"http://{str(ip)}")
        except: pass
        return list(targets)[:50]
