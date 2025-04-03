from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, ServiceContext
from llama_index.llms import OpenAI
from dotenv import load_dotenv
import os
import shutil

print("Limpiando carpeta storage...")
if os.path.exists("storage"):
    shutil.rmtree("storage")

print("Generando índice vectorial...")

load_dotenv()

# Cargar documentos
documents = SimpleDirectoryReader("docs").load_data()

# Crear contexto de servicio con modelo OpenAI
llm = OpenAI(temperature=0, model="gpt-3.5-turbo")
service_context = ServiceContext.from_defaults(llm=llm)

# Construir índice vectorial
index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)

# Persistir índice
index.storage_context.persist()
print("✅ Índice vectorial generado y almacenado correctamente.")
