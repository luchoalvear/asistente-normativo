from fastapi import FastAPI, Query
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Cargar documentos y construir el índice
documents = SimpleDirectoryReader("./").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# Iniciar FastAPI
app = FastAPI()

@app.get("/preguntar")
def preguntar(texto: str = Query(..., description="Tu pregunta")):
    respuesta = query_engine.query(texto)
    return {"respuesta": str(respuesta)}
