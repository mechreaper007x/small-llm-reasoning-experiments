# Adversarial Self-Interrogation Loops in Small LLMs (0.5B)

## Project Overview

This repository contains the experimental framework, test scripts, and research findings from a deep, empirical dive into the reasoning capabilities of small Large Language Models (LLMs). The project specifically targets the Qwen 2.5 0.5B model.

The core objective was to determine if an adversarial "Reason-Strategy-Execution" loop could empower highly constrained models to solve complex, B.Tech-level engineering and mathematical problems (e.g., Runge-Kutta 4, Bisection Method, Newton-Raphson). 

By pitting a "Student" model (Qwen 0.5B) against an "Advisor/Auditor" model (Mistral 7B) within a deterministic Python Sandbox (The Oracle), this project systematically deconstructed how small models simulate intelligence and mapped their definitive cognitive boundaries.

---

## 🔬 Key Discoveries: The Illusion of Reasoning

Our rigorous testing transitioned from pure text-based Program-Aided Language (PAL) reasoning to strict **Computational Scaffolding** (Python execution). This process revealed four definitive conclusions about how small LLMs operate:

### 1. Small Models Are "Syntactic Mimics," Not Reasoners
The most profound conclusion is that **models in the 0.5B class do not think; they format.** 
In early conversational tests (PAL), Qwen 0.5B scored "10/10" on complex math simply because it knew how to draw a Markdown table that *looked* correct, deceiving the 7B Advisor model. However, when forced into a deterministic Python sandbox, the illusion broke. The model proved incapable of holding state variables across loops, executing procedural logic, or recalling exact mathematical weights. It functions as a highly compressed "autocomplete" engine, not a logical engine.

### 2. "Context" Does Not Equal "Memory"
A common industry assumption is that giving a model its previous mistakes (Episodic Memory) helps it learn. This project proved the opposite for small models. As the context window grew, the model suffered from **Cognitive Overload** and **Strict Locality Bias**. Its attention heads became overwhelmed, causing it to blindly copy-paste tokens from its immediate previous sentence rather than following global system instructions.

### 3. The "Gaslighting" Paradox of Scale
The research discovered that larger models (like the 7B Advisor) are not immune to mathematical hallucinations; they are just **more confidently wrong**. In early tests, the 7B Advisor hallucinated fake numbers and "gaslit" the 0.5B model. Compounding the issue, the small model exhibited **Algorithmic Compliance**—abandoning its own correct reasoning to match the "authority" of the larger model's hallucination. Furthermore, the 7B model proved incapable of functioning as a reliable Arithmetic Logic Unit (ALU), failing basic decimal addition when auditing the small model's arithmetic.

### 4. The "Formula-Blindness" Schema Gap
Behavioral probing revealed that 0.5B models possess a "Symbolic Skeleton." They know the *names* of mathematical concepts (e.g., they know RK4 uses $k_1$ through $k_4$), but they invent nonsensical relationships between them. Precise mathematical constants and structural weights are the first victims of the LLM compression process.

---

## 🏗️ The Path Forward: The "Calculus Clerk" Architecture

Because small models suffer from zero working memory, they cannot be forced to reason through text loops. However, they are exceptionally powerful when utilized correctly. The only viable architecture for solving engineering problems on hardware-constrained environments (like edge devices or standard laptops) is to treat the small LLM as a **"Calculus Clerk"**:

1.  **Ban Manual Procedural Loops:** Never ask a 0.5B model to manually write a `for` or `while` loop for mathematical state management.
2.  **Enforce Single-Turn API Translation:** Use the LLM *exclusively* as a fuzzy linguistic interface to translate the user's natural language request into a single call to a robust, pre-compiled library (e.g., mapping "find the root" to `scipy.optimize.bisect`).
3.  **Rely on the CPU:** The LLM acts only as the translation router, leaving 100% of the state management, math, and logical execution to the deterministic Python CPU.

---

## 📂 Experimental Framework Structure

The repository tracks the evolution of the experimental architecture across several iterations:

*   **`interrogator.py`**: The initial baseline loop testing Program-Aided Language (PAL) and self-interrogation (revealed the "Formatting Illusion").
*   **`reason_v2.py` (Computational Scaffolding)**: Introduced the "Truth Anchor," where the Advisor generates a Python script to find the absolute truth before the Student attempts the problem, forcing the model into a deterministic Sandbox.
*   **`reason_v3.py` (Pure Math Loop)**: Tested if removing the burden of Python syntax would allow the model to reason purely in mathematical notation. (Failed due to Formula-Blindness).
*   **`reason_v4.py` (Atomic Factoring)**: Broke complex algorithms (like RK4) into single-step micro-turns to bypass attention collapse. (Failed due to Strict Locality Bias).
*   **`reason_v5.py` (Dynamic Schema Injection)**: The Advisor injected pure arithmetic blueprints, treating the 0.5B model as an ALU. (Failed, proving small models cannot process abstract variable substitution reliably).
*   **`probe_attention.py` & `probe_knowledge.py`**: Behavioral probes that mapped the model's reaction to Semantic Noise and its internal schema corruption.

## 📊 Reading the Results

*   `EXPERIMENT_LOGS.md`: Contains the historical logs of the early experiments, highlighting the transition from the "PAL Illusion" to the Sandbox reality.
*   `RESEARCH_REPORT.md`: The formal, comprehensive write-up of the methodology, philosophical foundation (Falsificationism), and detailed case studies (Bisection, Newton-Raphson, RK4).
*   `results/`, `results_v2/`, `results_v3/`, `results_v4/`, `results_v5/`: Directories containing the raw markdown outputs of the Student-Advisor iterative loops for various mathematical methods.

---
*This research empirically proves that underneath the fluent, confident text of small LLMs, there is no logical processing. By applying the scientific method to AI outputs, we can bypass the marketing hype and build robust, deterministic architectures on the edge.*