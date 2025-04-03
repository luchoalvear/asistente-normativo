import os
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms import OpenAI
from llama_index.node_parser import SimpleNodeParser
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar modelos
llm = OpenAI(model="gpt-3.5-turbo")
embed_model = OpenAIEmbedding(model="text-embedding-ada-002")
node_parser = SimpleNodeParser()

# Crear contexto de servicio compatible
service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model=embed_model,
    node_parser=node_parser
)

# Cargar documentos
documents = SimpleDirectoryReader("docs").load_data()

# Crear índice con el contexto
index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)

# Guardar índice en disco
index.storage_context.persist()

print("✅ Índice generado y almacenado con éxito.")
