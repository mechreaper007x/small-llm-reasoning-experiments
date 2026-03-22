# RESEARCH REPORT: Adversarial Self-Interrogation Loops in Small LLMs (0.5B)
**Date**: Monday, 23 March 2026  
**Subject**: Qwen 2.5 0.5B (Student) & Mistral 7B (Advisor/Auditor)  
**Environment**: Python Sandbox (The Oracle)

---

## 1. Executive Summary
The goal of this project was to determine if an adversarial "Reason-Strategy-Execution" loop could push a small, "dumb" model (Qwen 0.5B) to solve B.Tech-level engineering problems. Initial experiments revealed profound cognitive failure modes: **The Hallucination Paradox** and **Context-Induced Cognitive Overload.** By shifting from "Conversational Feedback" to **"Computational Scaffolding,"** we successfully broke the 0.5B performance ceiling on some tasks, achieving a 10/10 success rate. 

However, continued rigorous testing—transitioning from pure text-based reasoning (PAL) to strict Computational Scaffolding (Python execution)—ultimately led to a definitive conclusion: **Qwen 2.5 0.5B is not a reasoning model; it is a "Syntactic Mimic."** When forced to prove its logic in a deterministic sandbox, the model's illusion of intelligence collapsed, revealing deep cognitive failure modes including **Formula-Blindness**, **State-Management Amnesia**, and **Cross-Domain Hallucinations**.

---

## 2. Philosophical Foundation
The architecture is grounded in **Karl Popper’s Falsificationism**. We subjected the model's "Math Hypothesis" to a brutal adversarial environment where only logic that survives the Python Sandbox (The Oracle) is promoted. The introduction of **"Computational Scaffolding"** represents a move toward **Structural Epistemology**, where the model is not just asked to think, but is provided a "Scaffold of Truth" to prevent logical drift.

---

## 3. The Advisor Hallucination Problem (The "Gaslight" Effect)
A critical discovery was that **Scale does not guarantee Reliability.** In early tests, the 7B Advisor confidently gaslit the 0.5B Student by asserting a mathematically false Standard Deviation (4.717 vs 4.2708). Larger models often provide a more persuasive but incorrect "Truth Anchor," which triggers **Algorithmic Compliance** in smaller models—a digital version of the Milgram Effect where the Student suppresses its own correct reasoning to match the Advisor's "authoritative" error.

---

## 4. The Final Architecture: Computational Scaffolding
To overcome these failures, the system evolved into a four-pillar scaffolding system:

1.  **Symbolic Truth Anchoring (The "Gaslight Shield"):** The Advisor first generates a `numpy` or `sympy` script to calculate the absolute result. The Student is then given this "Absolute Truth" upfront.
2.  **Strategy-First Reasoning (The "Thinking Buffer"):** We forced a two-step generation process: first, the Mathematical Strategy (Natural Language), then the Code. This prevents **Attention Collapse** at 0.5B parameters.
3.  **Surgical Feedback (The "Memory Lean" Fix):** Instead of dumping the whole history (causing overload), the Advisor provides a "Surgical Extraction": the exact line that failed and the mathematical correction for that specific line.
4.  **Library Priority (The "Numpy-First" Mandate):** The system prompt explicitly forbids manual math loops for standard derivations, leaning into the model’s strength as a **"Compliant Integrator"** of APIs rather than a logic deriver.

---

## 5. The Illusion of Reasoning (PAL vs. Sandbox)
Early experiments using a "PAL + Self Interrogation" architecture yielded seemingly perfect **10/10 scores** on the Bisection Method. However, closer inspection of the logs revealed a profound paradox:

*   **Formatting Success:** The 0.5B model successfully drew beautiful Markdown tables containing columns for `a`, `b`, `c`, and `f(c)`. The 7B Advisor saw the shrinking intervals and validated the *format*, declaring it a success.
*   **Arithmetic Failure:** The actual math inside the tables was completely hallucinated. For example, the model calculated $f(1.5)$ for $x^3 - x - 2$ as $-3.0$ (actual: $-0.125$) and updated intervals completely contrary to the Bisection rules.

**Insight:** In purely conversational math, the 0.5B model acts as a "High-Fidelity Mimic." It knows what a solved math problem *looks like* (the vibe) but has no logical engine to compute the truth (the verity). The introduction of the Python Sandbox (The Oracle) did not break the model; it **falsified its intelligence** by forcing it to produce working, stateful code.

---

## 6. Critical Case Studies in the Sandbox

### A. Probability & Statistics: Success via Scaffolding
*   **Initial Failure:** Qwen was correct, but Mistral gaslit it with a false value.
*   **Scaffolded Success:** Mistral generated a `numpy` script, identified the "Absolute Truth" (4.2708), and provided surgical feedback on the Student's `ddof` parameter. Qwen corrected itself in Loop 2.

### B. The Bisection Method: State-Management Amnesia
*   **The Task:** Update the interval `[a, b]` over 3 iterations.
*   **The Failure:** The model wrote the `for` loop but failed to implement `if f(a) * f(c) < 0`. When corrected by the Advisor, it suffered from "Attention Span Collapse" and inserted random library calls like `np.roots([f, lambda x: f(x)])`.
*   **Diagnosis:** The model possesses **Zero Working Memory**. It understands the semantic concept of a loop but cannot hold mutated variables ($a_{n+1} \rightarrow a_n$) across iterations.

### C. Newton-Raphson: The "Derivative Illusion"
*   **The Task:** Find the root using $x_{n+1} = x_n - f(x_n)/f'(x_n)$.
*   **The Failure:** Instead of deriving $x^3 - x - 2$ analytically, the model wrote `np.diff(lambda x: x**3 - x - 2)`.
*   **Diagnosis:** This is a **Cross-Domain Hallucination**. The model cannot do calculus. However, its attention heads associate the word "derivative" with "difference", and "difference" with Python's `np.diff` array function. It attempted to "duck type" calculus using matrix operations.

### D. Runge-Kutta (RK4): Attention Copy-Paste (The Complexity Ceiling)
*   **The Task:** Execute a schema-injected blueprint for $k_1, k_2, k_3, k_4$.
*   **The Failure:** When explicitly given the blueprint $k_3 = \dots + (y + k_2/2)$, the model output $k_3 = \dots + (y + k_1/2)$.
*   **Diagnosis:** At 0.5B parameters, the model suffers from **Strict Locality Bias**. Rather than looking up at the system prompt for the true formula, it copied the $k_1/2$ token from the sentence it had just generated one line prior. Scaffolding fixes **Logical Drift**, but cannot yet bridge the **Schema Gap** for high-dimensional procedural state.

---

## 7. Key Cognitive Observations (Architectural & Behavioral)

To understand *why* the 0.5B model fails in these specific ways, we must look at its underlying architecture (Qwen 2.5 using Grouped Query Attention) and the behavior of its "Attention Heads." Behavioral probing (`probe_attention.py` and `probe_knowledge.py`) combined with recent literature on LLM hallucinations revealed the following mechanical realities:

1.  **The Resource Paradox (RAM vs. VRAM):** Despite the model weights being only ~397MB, the execution environment consumed up to 12GB of system RAM. This is due to the **KV Cache (Key-Value Cache)** expanding to hold the "Episodic Memory" of previous failed loops. As the context window grows, the small model's attention mechanism must track increasingly complex "Attention Sinks," causing hardware overhead without yielding cognitive improvement.
2.  **Strict Locality Bias (The "Attention Copy-Paste"):** At 0.5B parameters, the model's attention heads have a severely limited "receptive field" for logic. In the RK4 Schema Injection test, when generating step 3, the model's attention heads locked onto the tokens it had *just generated* in step 2, rather than looking back at the system prompt blueprint. It copied `k1/2` instead of reading `k2/2`. This proves that in small models, **local proximity overrides global instruction.**
3.  **Semantic Noise & Precision (The Distraction Probe):** Counter-intuitively, our behavioral probe showed that the 0.5B model was *more* mathematically precise when the prompt was flooded with distracting "Semantic Noise" (e.g., hundreds of random words). In a clean, short prompt, the model summarized "4.2708" as "4.27" (a Language Prior Hallucination). When forced to process a noisy prompt, its attention heads worked harder to filter the noise, inadvertently locking onto the precise tokens. This highlights that small models "summarize" truth when they aren't forced to attend closely to it.
4.  **Formula-Blindness & Compression Loss:** The knowledge probe confirmed the model possesses a "Symbolic Skeleton." It knows RK4 uses $k_1, k_2, k_3, k_4$, but invents nonsensical relationships between them. Mathematical constants and precise structural weights are the first victims of the LLM compression process. The model relies on "Vibe" over "Verity."
5.  **Mistral's Arithmetic Hallucinations:** The 7B Advisor also failed pure math evaluation. When verifying $1.0 + 0.1/2 + 0.05$, Mistral computed $1.15$ instead of $1.10$. This proves that even medium-sized LLMs process numbers as language tokens and lack reliable Arithmetic Logic Units (ALUs).

---

## 8. Final Conclusion: The Path Forward for Constrained AI
This research definitively proves that **small models (0.5B) are pattern-matchers, not reasoners.** They cannot hold state, they cannot execute step-by-step procedural logic, and their internal mathematical recall is heavily corrupted.

The previous "successes" of such models in conversational AI are largely illusions driven by accurate formatting. Adversarial loops improve **Grounding** but degrade **Reasoning** if the history is too verbose. 

**The Optimal Architecture for Constrained Hardware:**
You cannot force a 0.5B model to "reason" through text loops. To solve engineering problems, the architecture must treat them as **"Calculus Clerks"**:
1.  **Ban Manual Procedural Loops:** Never ask the model to write a `while` loop for Bisection or RK4.
2.  **Enforce Single-Turn API Translation:** Prompt the model exclusively to map the user's intent to standard, pre-compiled libraries (e.g., `scipy.optimize.bisect`, `scipy.integrate.solve_ivp`). 
3.  **Rely on the CPU:** The LLM must only act as the linguistic translation layer, leaving 100% of the "reasoning", state management, and arithmetic to deterministic Python execution.

---
**END OF REPORT**
