#!/usr/bin/env python
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.text_splitter import TokenTextSplitter

persist_dir = "storage"
if os.path.exists(os.path.join(persist_dir, "docstore.json")):
    print("🔁 Cargando índice desde almacenamiento existente...")
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
    index = load_index_from_storage(storage_context)
else:
    print("📚 Creando nuevo índice desde documentos...")
    documents = SimpleDirectoryReader("docs").load_data()
    splitter = TokenTextSplitter(chunk_size=512, chunk_overlap=50)
    index = VectorStoreIndex.from_documents(documents, transformations=[splitter])
    index.storage_context.persist(persist_dir=persist_dir)
