from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms import OpenAI
from llama_index.storage.storage_context import StorageContext
from dotenv import load_dotenv
import os
import shutil

load_dotenv()

# Limpia la carpeta de índices
if os.path.exists("storage"):
    shutil.rmtree("storage")

documents = SimpleDirectoryReader("docs").load_data()

service_context = ServiceContext.from_defaults(
    llm=OpenAI(model="gpt-3.5-turbo", temperature=0),
    embed_model=OpenAIEmbedding()
)

index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
index.storage_context.persist()

print("✅ Índice generado correctamente.")
