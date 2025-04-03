from llama_index.readers import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
import os

persist_dir = "./storage"

# Si el índice ya existe, se carga desde almacenamiento
if os.path.exists(persist_dir):
    print("Cargando índice existente desde almacenamiento...")
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
    index = load_index_from_storage(storage_context)
else:
    print("Generando índice vectorial...")
    reader = SimpleDirectoryReader(input_dir="./docs", recursive=True)
    documents = reader.load_data()
    index = VectorStoreIndex.from_documents(documents, show_progress=True)
    index.storage_context.persist(persist_dir=persist_dir)

print("Índice listo para ser consultado.")
