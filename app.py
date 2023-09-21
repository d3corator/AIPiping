from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from ai.routes import router

from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse


app = FastAPI(
    docs_url='/docs',
    redoc_url='/re-docs'
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": "FastAPI"})


app.include_router(router)
