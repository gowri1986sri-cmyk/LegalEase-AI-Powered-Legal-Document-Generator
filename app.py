from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create FastAPI application
app = FastAPI(
    title="LegalEaseAI",
    description="AI-Powered Legal Document Generator",
    version="1.0"
)

# Connect templates folder
templates = Jinja2Templates(directory="templates")

# Connect static folder
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# -----------------------------
# Home Page
# -----------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


# -----------------------------
# Generate Legal Document
# -----------------------------
@app.post("/generate", response_class=HTMLResponse)
async def generate_document(
    request: Request,
    document_type: str = Form(...),
    parties: str = Form(...),
    terms: str = Form(...),
    effective_date: str