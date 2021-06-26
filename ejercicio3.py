from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

lista_integrantes = [{'item_id': 1, 'matricula': 91810227, 'nombre':'Micheli', 'edad':22}, 
                     {'item_id': 2, 'matricula': 91810589, 'nombre':'Jorge', 'edad':22}, 
                     {'item_id': 3, 'matricula': 91810098, 'nombre':'Irma', 'edad':20}, 
                     {'item_id': 4, 'matricula': 91811679, 'nombre':'Ana', 'edad':20}]

@app.get("/integrantes")
async def leer_integrante(item_id: int):
    for diccionario in lista_integrantes:
        if diccionario.get('item_id') == item_id:
            respuesta = f"""
                <html>
                <head>
                    <title>{diccionario.get('nombre')}</title>
                </head>
                <body>
                    <h3>sitio personal</h3>
                    <ul>
                        <li>Matricula: {diccionario.get('matricula')}</li>
                        <li>Nombre: {diccionario.get('nombre')}</li>
                        <li>Edad: {diccionario.get('edad')}</li>
                    </ul>
                </body>
                </html>
            """
            return HTMLResponse(content=respuesta, status_code=200)
    return "No se encontró el registro"



# async def buscar_integrante(lista: Iterable[dict], clave: Hashable, valor: Any) -> Optional[dict]:
#     for diccionario in lista:
#         if diccionario.get(clave) == valor:
#             print(diccionario)
#             return json.dumps(diccionario)
#     return None

#@app.get("/data")
#async def get_data(start_indx: int = 1, step: int = 8):
#	return lista_integrantes[start_indx : start_indx+step]
async def get_data(indice: int = 0):
	return lista_integrantes[indice]
	
	
	