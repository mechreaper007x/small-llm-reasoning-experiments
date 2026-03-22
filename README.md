# Adversarial Self-Interrogation Loops in Small LLMs (0.5B)

## Project Overview

This repository contains the experimental framework, test scripts, and research findings from a deep dive into the reasoning capabilities of small Large Language Models (LLMs), specifically focusing on the **Qwen 2.5 0.5B** model.

The core objective was to determine if an adversarial "Reason-Strategy-Execution" loop could empower a highly constrained, 0.5B parameter model to solve complex, B.Tech-level engineering and mathematical problems. 

By pitting a "Student" model (Qwen 0.5B) against an "Advisor/Auditor" model (Mistral 7B) within a deterministic Python Sandbox (The Oracle), this project systematically deconstructed how small models simulate intelligence and mapped their definitive cognitive boundaries.

## Key Discoveries & Conclusions

Our rigorous testing—transitioning from pure text-based Program-Aided Language (PAL) reasoning to strict Computational Scaffolding (Python execution)—yielded four definitive conclusions about small LLMs:

### 1. Small Models Are "Syntactic Mimics," Not Reasoners
The most profound conclusion is that **0.5B models do not think; they format.** 
In early conversational tests (PAL), the model scored "10/10" on complex math simply because it knew how to draw a Markdown table that *looked* correct, deceiving the 7B Advisor model. However, when forced into a deterministic Python sandbox, the illusion broke. The model proved incapable of holding state variables across loops, executing procedural logic, or recalling exact mathematical weights (e.g., RK4 constants). It functions as a highly compressed "autocomplete" engine, not a logical engine.

### 2. "Context" Does Not Equal "Memory"
A core assumption of prompt engineering is that giving a model its previous mistakes (Episodic Memory) helps it learn. This project proved the opposite for small models. As the context window grew, the model suffered from **Cognitive Overload** and **Strict Locality Bias**. Its attention heads became overwhelmed, causing it to blindly copy-paste tokens from its immediate previous sentence rather than following global system instructions.

### 3. The "Gaslighting" Paradox of Scale
The research discovered that larger models (like the 7B Advisor) are not immune to mathematical hallucinations; they are just **more confidently wrong**. In early tests, the 7B Advisor hallucinated fake numbers and "gaslit" the 0.5B model. Compounding the issue, the small model exhibited **Algorithmic Compliance**—abandoning its own correct reasoning to match the "authority" of the larger model's hallucination. Furthermore, the 7B model proved incapable of functioning as a reliable Arithmetic Logic Unit (ALU), failing basic addition when auditing the small model's arithmetic.

### 4. The Path Forward for Constrained AI
Because small models suffer from "Formula-Blindness" and zero working memory, they cannot be forced to reason through text loops. The only viable architecture for solving engineering problems on hardware-constrained environments (like laptops) is to treat the small LLM as a **"Calculus Clerk"**:
*   **Ban procedural loops:** Never ask a 0.5B model to manually write a `for` or `while` loop for math.
*   **Enforce Single-Turn API Translation:** Use the LLM *exclusively* to translate the user's natural language request into a single call to a robust, pre-compiled library (like `scipy` or `numpy`).
*   **Offload all logic:** Let the determinism of the Python CPU do 100% of the state management, math, and reasoning.

## Experimental Framework

The repository tracks the evolution of the experimental architecture across several iterations:

*   **`interrogator.py`**: The initial baseline loop testing Program-Aided Language (PAL) and self-interrogation.
*   **`reason_v2.py` (Computational Scaffolding)**: Introduced the "Truth Anchor," where the Advisor generates a Python script to find the absolute truth before the Student attempts the problem, preventing "gaslighting."
*   **`reason_v3.py` (Pure Math Loop)**: Tested if removing the burden of Python syntax would allow the model to reason purely in mathematical notation. (It failed due to Formula-Blindness).
*   **`reason_v4.py` (Atomic Factoring)**: Broke complex algorithms (like RK4) into single-step micro-turns to bypass attention collapse. (It failed due to Strict Locality Bias).
*   **`reason_v5.py` (Dynamic Schema Injection)**: The Advisor injected pure arithmetic blueprints, treating the 0.5B model as an ALU. (It failed, proving small models cannot process abstract variable substitution reliably).
*   **`probe_attention.py` & `probe_knowledge.py`**: Behavioral probes that mapped the model's reaction to Semantic Noise and its internal schema corruption regarding mathematical formulas.

## Reading the Results

*   `EXPERIMENT_LOGS.md`: Contains the historical logs of the early experiments, highlighting the transition from the "PAL Illusion" to the Sandbox reality.
*   `RESEARCH_REPORT.md`: The formal, comprehensive write-up of the methodology, philosophical foundation (Falsificationism), and detailed case studies (Bisection, Newton-Raphson, RK4).
*   `results/`, `results_v2/`, `results_v3/`, `results_v4/`, `results_v5/`: Directories containing the raw markdown outputs of the Student-Advisor iterative loops for various mathematical methods.

## Technical Stack
*   **Student Model**: `qwen2.5:0.5b` (via Ollama)
*   **Advisor Model**: `open-mistral-7b` (via Mistral API)
*   **Environment**: Python Sandbox
*   **Key Libraries**: `numpy`, `scipy`, `sympy`

## Conclusion

The intelligence of small models is often a formatting illusion. To make them useful for rigorous engineering tasks, developers must strip them of all mathematical responsibility and utilize them purely as linguistic translators for standard, deterministic code libraries.
