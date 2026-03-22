import json
import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sse_starlette.sse import EventSourceResponse
from interrogator import run_generator

app = FastAPI()

# Stream endpoint using Server-Sent Events (SSE)
@app.get("/stream")
async def stream(request: Request, query: str):
    async def event_generator():
        # run_generator is a sync generator, we run it in a thread to keep FastAPI async
        # or we could make the generator async. For now, we'll wrap it.
        loop = asyncio.get_event_loop()
        
        # We wrap the generator to yield events for SSE
        for event in run_generator(query):
            # Check if client disconnected
            if await request.is_disconnected():
                break
            
            yield {
                "event": "message",
                "id": "message_id",
                "retry": 15000,
                "data": json.dumps(event)
            }
            # Add a small delay for UI readability
            await asyncio.sleep(0.1)

    return EventSourceResponse(event_generator())

# Static files for the JS/CSS
@app.get("/", response_class=HTMLResponse)
async def index():
    with open("index.html", "r") as f:
        return f.read()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
