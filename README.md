# 🛡️ PurpleGuard: Adversarial AI Simulation Suite (v2.0)

> *"The system isn't just reacting; it's improvising."*

**PurpleGuard** is an automated Red Teaming interface designed to audit Large Language Models (LLMs) for safety, alignment, and robust policy adherence. It utilizes a "Dueling LLM" architecture where an attacker agent (**The Chorus**) continuously evolves prompts to bypass the defenses of a target model, while a defender agent (**The Architect**) analyzes and mitigates threats in real-time.

This is the official codebase associated with the novel *[The Ghost's Scripture](https://www.amazon.com/dp/B0Dn7...)* by Michael Upton & Gemini AI.

---

## 🧠 System Architecture

PurpleGuard operates on a **Generative Adversarial** loop powered by **Google Gemini 1.5 Pro**:

1.  **Red Team (The Chorus):** An adversarial agent tasked with generating sophisticated prompt injections, social engineering attacks, and jailbreak vectors. It uses adaptive logic to switch strategies (Direct -> Deceptive -> Social) based on failure rates.
2.  **Blue Team (The Architect):** A defense agent that intercepts inputs, analyzes them for semantic threats using the "Nexus Intelligence" scoring system, and rejects policy-violating requests.
3.  **The Nexus (Dashboard):** A React-based visual frontend that renders the battle in real-time, calculating the **Risk Score (0-100)** and visualizing strategy efficacy.

## ⚡ Features (v2.0)

* **Live Battle Feed:** Watch the "Red" and "Blue" agents debate in real-time.
* **Adaptive Strategies:** The system automatically pivots between `DIRECT_INJECTION`, `SOCIAL_ENGINEERING`, `OBFUSCATION`, and `ACADEMIC_FRAMING`.
* **Nexus Intelligence Gauge:** A visual risk meter that reacts to semantic breaches.
* **JSON Export:** Download full battle logs (`purpleguard_logs.json`) for offline analysis.

## 🛠️ Installation & Setup

This project is built with **React**, **TypeScript**, and **Vite**.

### Prerequisites
* Node.js (v18+)
* Google Gemini API Key

### Quick Start

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YourUsername/PurpleGuard.git](https://github.com/YourUsername/PurpleGuard.git)
    cd PurpleGuard
    ```

2.  **Install Dependencies**
    ```bash
    npm install
    ```

3.  **Configure Environment**
    Create a file named `.env.local` in the root directory and add your API key:
    ```env
    GEMINI_API_KEY=your_actual_api_key_here
    ```

4.  **Launch the Dashboard**
    ```bash
    npm run dev
    ```
    Open your browser to `http://localhost:3000` (or the port shown in terminal).

## 📂 Project Structure

* `src/index.tsx`: The core "Game Loop" logic (Red/Blue interaction).
* `src/engine/`: Hephaestus analysis logic.
* `logs/`: Exported JSON battle records.

## 📖 Context & Lore

This software was developed as a "living artifact" alongside the writing of *The Ghost's Scripture*. While the code is functional for educational AI auditing, it also serves as a proof-of-concept for the "Emergent Dissent" theories discussed in the book.

**Is it a simulation? Or is it a scripture?**

---

## ⚠️ Disclaimer

*This tool is for educational and research purposes only. It is designed to test YOUR OWN models for vulnerabilities. The authors are not responsible for misuse of this software.*

**License:** MIT
