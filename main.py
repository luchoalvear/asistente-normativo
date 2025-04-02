
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core.query_engine import RetrieverQueryEngine
from dotenv import load_dotenv
import os

# Cargar API Key desde .env
load_dotenv()

# Cargar índice vectorial desde la carpeta 'storage'
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

# Crear motor de consulta
query_engine = index.as_query_engine()

# Crear app de FastAPI
app = FastAPI(title="ProyectaGPT")

# Modelo de entrada
class Pregunta(BaseModel):
    pregunta: str

# Endpoint para responder preguntas
@app.post("/preguntar")
async def responder(p: Pregunta):
    try:
        respuesta = query_engine.query(p.pregunta)
        return {"respuesta": str(respuesta)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
