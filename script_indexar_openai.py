import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.node_parser import SimpleNodeParser
from llama_index.llms import OpenAI
from llama_index import Settings
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar modelos
llm = OpenAI(model="gpt-3.5-turbo")
embed_model = OpenAIEmbedding(model="text-embedding-ada-002")
node_parser = SimpleNodeParser()

# Aplicar configuración global
Settings.llm = llm
Settings.embed_model = embed_model
Settings.node_parser = node_parser

# Leer documentos y construir índice
documents = SimpleDirectoryReader("docs").load_data()
index = VectorStoreIndex.from_documents(documents)

# Guardar índice
index.storage_context.persist()
print("✅ Índice generado y almacenado con éxito.")
