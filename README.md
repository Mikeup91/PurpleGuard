# 🛡️ PurpleGuard
### **The First Self-Healing Browser Defense Platform.**
> *Powered by Dueling LLMs. Built for the Manifest V3 Era.*

---

### **🔥 The Problem**
Standard EDRs protect the OS. They are blind to the Browser.
Malicious Chrome Extensions (Manifest V3) are the new #1 vector for credential theft, bypassing MFA and encryption by living inside the trusted user context.

### **⚡ The Solution: Dueling AI**
PurpleGuard does not wait for a breach. We run a continuous, adversarial AI loop in the cloud:

1.  🔴 **The Red Engine:** An AI autonomously conceptualizes novel extension attack vectors (e.g., specific permission combinations for stealthy exfiltration).
2.  🔵 **The Blue Engine:** A counter-AI analyzes these theoretical attacks and writes **Detection Signatures** in real-time.
3.  🛡️ **The Sentry:** Your endpoints download these signatures instantly, blocking threats that haven't even been seen in the wild yet.

---

### **🚀 Architecture**
*   **Engine:** Python + Dueling Logic (Adversarial Loop)
*   **Feed:** Live JSON Threat Intelligence
*   **Agent:** Lightweight Python Sentry (Privacy-First, Local Processing)

### **🛠️ Installation (Alpha)**
```bash
git clone https://github.com/Mikeup91/PurpleGuard
cd PurpleGuard
python engine.py --duel
# PurpleGuard
