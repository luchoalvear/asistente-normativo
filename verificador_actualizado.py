
import os
from dotenv import load_dotenv
from llama_index.core import StorageContext, load_index_from_storage

# Cargar la clave de OpenAI desde .env
load_dotenv()

# Cargar el índice desde almacenamiento
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

# Mostrar metadata de los primeros documentos
print("\n📄 Verificando metadata en el índice:\n")
for i, node in enumerate(index.docstore.docs.values()):
    print(f"Documento {i + 1}:")
    print(node.metadata)
    print("-" * 60)
    if i >= 4:
        break
