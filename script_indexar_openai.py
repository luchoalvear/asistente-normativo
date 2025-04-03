import os
import shutil
import json
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, Document

from llama_index.core.text_splitter import TokenTextSplitter
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.extractors import (
    TitleExtractor,
    QuestionsAnsweredExtractor,
    SummaryExtractor,
)
from llama_index.core import Settings

PERSIST_DIR = "./storage"

# Limpiar índice anterior
if os.path.exists(PERSIST_DIR):
    shutil.rmtree(PERSIST_DIR)

# Cargar metadatos desde metadata.json
metadata_map = {}
if os.path.exists("docs/metadata.json"):
    with open("docs/metadata.json", "r", encoding="utf-8") as f:
        metadata_list = json.load(f)
        for item in metadata_list:
            metadata_map[item["nombre"].lower()] = item

# Configurar modelo de embedding
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
Settings.chunk_size = 512
Settings.chunk_overlap = 64

# Pipeline de procesamiento
pipeline = IngestionPipeline(
    transformations=[
        TitleExtractor(nodes=5),
        QuestionsAnsweredExtractor(questions=3),
        SummaryExtractor(summaries=["prev", "self"]),
        SentenceSplitter(),
    ]
)

# Leer y enriquecer documentos con metadatos
raw_docs = SimpleDirectoryReader(input_dir="docs", required_exts=['.pdf']).load_data()
documentos = []
for doc in raw_docs:
    basename = os.path.splitext(os.path.basename(doc.metadata.get("file_path", "")))[0].lower()
    extra_metadata = metadata_map.get(basename, {})
    doc.metadata.update(extra_metadata)
    documentos.append(doc)

# Ejecutar pipeline
nodes = pipeline.run(documents=documentos)

# Crear índice
index = VectorStoreIndex(nodes)
index.storage_context.persist(persist_dir=PERSIST_DIR)

print("✅ Índice generado con metadatos y guardado correctamente.")
