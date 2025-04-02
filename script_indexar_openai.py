import os
import json
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, ServiceContext
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.text_splitter import TokenTextSplitter

# Cargar API Key desde .env
load_dotenv()

# Configurar modelo de embeddings y LLM
embed_model = OpenAIEmbedding(model="text-embedding-3-small")
llm = OpenAI(model="gpt-3.5-turbo", temperature=0)

# Dividir texto en fragmentos (chunks)
text_splitter = TokenTextSplitter(chunk_size=512, chunk_overlap=30)

# Crear contexto de servicio con configuraciones personalizadas
service_context = ServiceContext.from_defaults(
    embed_model=embed_model,
    llm=llm,
    text_splitter=text_splitter
)

# Cargar metadata desde archivo
with open("metadata.json", "r", encoding="utf-8") as f:
    metadata_dict = json.load(f)

# Cargar documentos PDF y asignar metadata
documents = []
for filename in os.listdir("docs"):
    if filename.endswith(".pdf"):
        file_docs = SimpleDirectoryReader(input_files=[f"docs/{filename}"]).load_data()
        for doc in file_docs:
            doc.metadata = metadata_dict.get(filename, {})
            documents.append(doc)

# Crear índice vectorial con contexto personalizado
index = VectorStoreIndex.from_documents(documents, service_context=service_context)
index.storage_context.persist()
