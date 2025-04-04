from fastapi import FastAPI, HTTPException
from llama_index import StorageContext, load_index_from_storage
import os

app = FastAPI()
PERSIST_DIR = "./storage"

if os.path.exists(os.path.join(PERSIST_DIR, "docstore.json")):
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)
else:
    index = None

@app.get("/preguntar")
def preguntar(texto: str):
    if not index:
        raise HTTPException(status_code=503, detail="El índice aún no ha sido generado.")
    respuesta = index.query(texto)
    return {"respuesta": str(respuesta)}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
