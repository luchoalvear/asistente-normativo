
import os
from llama_index.core import SimpleDirectoryReader, StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.text_splitter import TokenTextSplitter

# Ruta a la carpeta de almacenamiento del índice
persist_dir = "storage"

# Verifica si ya existe un índice guardado
if os.path.exists(os.path.join(persist_dir, "docstore.json")):
    print("📦 Cargando índice existente desde disco...")
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
    index = load_index_from_storage(storage_context)
else:
    print("🆕 No se encontró índice existente. Generando nuevo índice...")
    documents = SimpleDirectoryReader("docs").load_data()
    
    # Usamos un TextSplitter con configuración avanzada (puedes ajustar valores)
    splitter = TokenTextSplitter(separator="\n", chunk_size=512, chunk_overlap=100)
    
    # Embeddings avanzados (OpenAI por defecto)
    embed_model = OpenAIEmbedding(model="text-embedding-3-small")  # Ajustable

    index = VectorStoreIndex.from_documents(
        documents,
        embed_model=embed_model,
        transformations=[splitter]
    )

    # Guardamos el índice
    index.storage_context.persist(persist_dir=persist_dir)

print("✅ Proceso de indexación completado.")
