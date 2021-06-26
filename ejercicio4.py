from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import json

app = FastAPI(title = "FastAPI con Jinja2")

app.mount("/rutarecursos", StaticFiles(directory="recursos"), name="mirecurso")

miPlantilla = Jinja2Templates(directory="plantillas")
    
@app.get("/inicio/", response_class=HTMLResponse)
async def read_item(request: Request):
    return miPlantilla.TemplateResponse("index.html",{"request":request})

@app.get("/lista", response_class=HTMLResponse)
async def iniciar(request: Request):
    with open('lista_alumnos.json') as f:
        datos = json.load(f)
    return miPlantilla.TemplateResponse("listaIntegrantes.html",{"request":request,"lista":datos})
