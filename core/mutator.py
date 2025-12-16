import random

class MutationLab:
    def __init__(self):
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15',
            'curl/7.68.0'
        ]
    
    def get_random_ua(self):
        return random.choice(self.user_agents)
    
    def generate_variants(self, payload, context):
        variants = [payload]
        variants.append(payload.replace("<", "%253c").replace(">", "%253e"))
        if context == "SQLi":
            variants.extend([payload.replace("OR", "O/**/R"), payload.replace("UNION", "UNI/**/ON")])
        unique_variants = list(dict.fromkeys(variants))
        return unique_variants[:10]
