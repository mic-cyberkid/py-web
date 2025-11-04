from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Python + GitHub Actions + Render",
    description="Auto-deployed FastAPI app",
    version="1.0.0"
)

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <h1>FastAPI + GitHub Actions + Render 🚀</h1>
    <p>Successfully deployed!</p>
    <ul>
      <li><a href="/docs">API Docs (Swagger)</a></li>
      <li><a href="/redoc">API Docs (ReDoc)</a></li>
    </ul>
    """

@app.get("/api/health")
async def health():
    return {"status": "healthy", "version": "1.0.0"}
