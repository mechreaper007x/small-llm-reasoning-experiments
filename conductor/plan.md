# Implementation Plan: VM Sandbox Integration

## Background & Motivation
The core philosophy is that hypotheses must survive genuine attacks. For code generation or mathematical reasoning, static LLM critique is insufficient—we need real consequences. Integrating a sandbox allows the loop to execute generated code, capture tracebacks and standard output, and use these as incontrovertible constraints for the next iteration if the hypothesis (code) fails.

## Key Files & Context
- `interrogator.py`: The existing pure reasoning loop.

## Proposed Solution
1. **Code Extraction & Execution**:
   - Implement `extract_python_code(text)` to pull code blocks from the generated answer.
   - Implement `execute_sandbox(code)` using Python's `subprocess` module. We'll run the code in an isolated subprocess with a strict timeout (e.g., 5-10 seconds).
   - Capture `stdout`, `stderr`, and the exit code.

2. **Integration into the Self-Interrogation Loop**:
   - After the `generate` step, automatically check for Python code.
   - If code exists, execute it.
   - **Scenario A (Execution Fails)**: If the subprocess returns a non-zero exit code or times out, this is an automatic fatal flaw. We bypass the `interrogate` step (or feed the error directly into it), assign a survival score of `0`, and append the `stderr` traceback as a hard constraint for the next loop.
   - **Scenario B (Execution Succeeds)**: If it runs successfully, we pass the `stdout` to the `interrogate` function. The Brutal Falsifier now has empirical evidence to evaluate whether the code actually solved the query.

3. **Prompt Adjustments**:
   - Update the `interrogate` system prompt to accept and analyze execution output.

## Implementation Steps
1. Add `subprocess` and `re` imports to `interrogator.py`.
2. Write the `extract_python_code(answer: str) -> str` helper function.
3. Write the `execute_sandbox(code: str, timeout: int = 5) -> dict` helper function.
4. Modify `run(query: str)` to interject the sandbox execution right after `generate()`.
5. Modify `interrogate(query, answer, execution_result=None)` to factor in sandbox outcomes.

## Verification
- Test with a query that requires code (e.g., "Write a function to compute the 100th Fibonacci number and print it.").
- Intentionally provide a query that usually causes models to write buggy code to verify the loop catches the traceback, feeds it back, and fixes it in a subsequent iteration.