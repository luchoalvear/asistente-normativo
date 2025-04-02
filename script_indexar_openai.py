
import os
import json
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Cargar metadata desde el archivo JSON
with open("metadata.json", "r", encoding="utf-8") as f:
    metadata_dict = json.load(f)

# Leer documentos PDF y asociar metadata
documents = []
for filename in os.listdir("docs"):
    if filename.endswith(".pdf"):
        file_docs = SimpleDirectoryReader(input_files=[f"docs/{filename}"]).load_data()
        for doc in file_docs:
            doc.metadata = metadata_dict.get(filename, {})
            documents.append(doc)

# Crear índice vectorial usando embeddings de OpenAI
index = VectorStoreIndex.from_documents(documents)
index.storage_context.persist()
