# Implementation Plan: Web Frontend & API for Interrogator

## Objective
Provide a visual dashboard to watch the self-interrogation loop in real-time. This includes seeing the generated code, its sandbox execution (stdout/stderr), and the "Brutal Falsifier's" JSON attacks.

## Proposed Solution
1. **Backend**: A FastAPI server (`server.py`) that wraps the `interrogator.py` logic. It will use **Server-Sent Events (SSE)** to stream the internal state of each loop (Generating -> Executing -> Interrogating) to the frontend.
2. **Frontend**: A modern, dark-themed dashboard (`index.html` + `script.js`) that:
   - Takes a user query.
   - Displays a live "Thinking Trace" with expandable cards for each loop.
   - Highlights the "Survival Score" and "Fatal Flaws" using color-coded badges.

## Key Components
- **`server.py`**:
  - Endpoint `/stream?query=...`: Returns a `text/event-stream`.
  - Refactors `interrogator.py` to `yield` status updates as JSON events.
- **`index.html`**:
  - Simple UI with a query input and a "Begin Interrogation" button.
  - A scrollable container for the loop cards.
- **`style.css`**:
  - Dark mode aesthetics, using a monospace font for code and logs.
- **`script.js`**:
  - Uses `EventSource` to listen to the SSE stream and dynamically append the UI components.

## Implementation Steps
1. Install `fastapi` and `uvicorn`.
2. Refactor `interrogator.py` into a generator function `run_generator(query)` that yields loop data.
3. Create `server.py` with the FastAPI app and the SSE endpoint.
4. Create the frontend assets (`index.html`, `style.css`, `script.js`).
5. Update `interrogator.py` to be import-friendly (no hard-coded `__main__` logic).

## Verification
- Start the server: `python server.py`.
- Open the UI in a browser.
- Run a query like "Write a Python script to compute the 100th Fibonacci number."
- Observe the real-time feedback as the loops execute.
