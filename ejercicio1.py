from fastapi import FastAPI
from typing import Optional
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def mostar_inicio():
    contenido_html = """
    <html>
    <head>
        <title>Equipo5</title>
    </head>
    <body>
        <h3>Bienvenidos</h3>
        <p>Este sitio pertenece al Equipo5 y mostrará los datos de los integrantes</p>
		<a href="Micheli.html"> Micheli </a>
    </body>
	</html>
    """
    return HTMLResponse(content=contenido_html, status_code=200)
	
@app.get("/integrantes/{item_id}")
async def leer_integrante(item_id: int, matricula: int, nombre: str, edad: Optional[int] = None):
	respuesta = f"""
	<html>
    <head>
        <title>{nombre}</title>
    </head>
    <body>
        <h3>sitio personal</h3>
        <ul>
            <li>Matricula: {matricula}</li>
            <li>Nombre: {nombre}</li>
            <li>Edad: {edad}</li>
        </ul>
    </body>
	</html>
	"""
	return HTMLResponse(content=respuesta, status_code=200)



@app.get('/buscar/')
async def get_data(start_indx: int = 1, step: int = 10):
	return data_dict[start_indx : start_indx+step]
