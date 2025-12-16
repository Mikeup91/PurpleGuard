import requests, random, time, threading
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

class DeepSpider:
    def __init__(self, nexus):
        self.nexus = nexus
        self.session = requests.Session()
        self.visited_lock = threading.Lock()

    def crawl(self, target, max_depth=3):
        visited = set()
        endpoints = []
        def _crawl_recursive(url, depth=0):
            if depth >= max_depth or url in visited: return
            visited.add(url)
            time.sleep(random.uniform(0.5, 1.5))
            try:
                resp = self.session.get(url, timeout=5)
                self.nexus.ingest_intel(url, resp.headers, resp.text)
                soup = BeautifulSoup(resp.text, 'html.parser')
                for a in soup.find_all('a', href=True):
                    full_url = urljoin(url, a['href'])
                    if urlparse(full_url).netloc == urlparse(target).netloc:
                        endpoints.append({"url": full_url, "method": "GET", "params": []})
                        _crawl_recursive(full_url, depth + 1)
            except: pass
        _crawl_recursive(target)
        return endpoints
