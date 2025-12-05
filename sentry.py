"""
PurpleGuard Sentry v0.1
Client-side scanner. Checks local extensions against the Threat Feed.
"""

import json
import os
import sys

# In production, this pulls from https://api.purpleguard.io/feed
# For the demo, we use local mock data if the feed file doesn't exist.
MOCK_FEED = [
    {"signature": {"target_vector": "Crypto Wallet Drainer", "banned_combination": ["storage", "activeTab"]}}
]

def load_threats():
    try:
        if os.path.exists("threat_feed.json"):
            with open("threat_feed.json", "r") as f:
                # Handle line-by-line JSON (NDJSON) or standard JSON
                content = f.read().strip()
                if content.startswith("["):
                    return json.loads(content)
                else:
                    return [json.loads(line) for line in content.splitlines()]
    except:
        return MOCK_FEED
    return MOCK_FEED

def scan_system():
    print("🛡️ PurpleGuard Sentry Active.")
    print("⬇️  Syncing with Threat Intelligence Feed...")
    
    threats = load_threats()
    print(f"✅ Loaded {len(threats)} active detection signatures.\n")
    
    print("🔍 Scanning Browser Extensions...")
    # MOCKING A SCAN for the demo (since we can't access Chrome on GitHub/Mobile)
    # In a real deployment, this parses the Chrome 'Preferences' file.
    
    my_extensions = [
        {"name": "Google Docs Offline", "perms": ["clipboardRead"]},
        {"name": "Sketchy VPN", "perms": ["storage", "activeTab"]} # This should trigger an alert
    ]
    
    issues_found = 0
    
    for ext in my_extensions:
        print(f"   Checking: {ext['name']}...", end=" ")
        is_clean = True
        
        for rule in threats:
            # Accessing nested dictionary safely
            sig = rule.get('signature', rule) 
            banned = sig.get('banned_combination', [])
            
            # Check if extension has ALL banned perms
            if all(p in ext['perms'] for p in banned):
                print(f"🚨 DETECTED!")
                print(f"      [!] MATCH: {sig.get('target_vector')}")
                print(f"      [!] ACTION: Process Terminated.")
                is_clean = False
                issues_found += 1
                break
        
        if is_clean:
            print("OK.")

    print("\n" + "="*30)
    if issues_found > 0:
        print(f"❌ SYSTEM COMPROMISED. {issues_found} Threats Isolated.")
        sys.exit(1)
    else:
        print("✅ SYSTEM CLEAN. PurpleGuard protecting.")
        sys.exit(0)

if __name__ == "__main__":
    scan_system()
  
