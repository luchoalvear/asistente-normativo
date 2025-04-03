from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, StorageContext, Document
import os
import shutil

# Ruta base
ruta_base = os.path.dirname(os.path.abspath(__file__))

# Carpeta de documentos
ruta_docs = os.path.join(ruta_base, "docs")

# Carpeta de almacenamiento
ruta_storage = os.path.join(ruta_base, "storage")

# Eliminar carpeta storage si existe
print("Limpiando carpeta storage...")
if os.path.exists(ruta_storage):
    shutil.rmtree(ruta_storage)

# Leer documentos
print("Generando índice vectorial...")
documentos = SimpleDirectoryReader(ruta_docs).load_data()

# Crear índice
index = GPTVectorStoreIndex.from_documents(documentos)

# Guardar índice
index.storage_context.persist(persist_dir=ruta_storage)
