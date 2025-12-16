# PURPLE GUARD | OMNIBUS ENGINE V2
**High-Performance Multi-Vector Vulnerability Orchestration Framework**

## Overview
Purple Guard is a modular, multi-threaded security engine designed for high-density vulnerability discovery. It utilizes a centralized intelligence core (Nexus) to coordinate reconnaissance, payload mutation, and multi-vector swarming.

## Core Modules
- **Nexus (evolution/):** Centralized state machine for cross-vector intelligence.
- **DeepSpider (core/):** Topology mapping and endpoint discovery.
- **MutationLab (core/):** Context-aware payload obfuscation for WAF evasion.
- **Vector Swarm (modules/):** Parallel execution of SQLi, XSS, and LFI vectors.
- **AuditReporter (modules/):** Automated Markdown and evidence logging.

## Technical Specifications
- **Concurrency:** ThreadPoolExecutor with dynamic worker scaling.
- **Detection:** Multi-factor confidence scoring (Time-based + Pattern matching).
- **Environment:** Optimized for mobile (Termux) and Linux environments.

## Quick Start
1. `pip install -r requirements.txt`
2. `python3 omnibus.py <target_url>`
