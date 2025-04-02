import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
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

print("📦 Generando índice vectorial...")

# Embedding y parser
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
Settings.chunk_size = 512
Settings.chunk_overlap = 64

pipeline = IngestionPipeline(
    transformations=[
        TitleExtractor(nodes=5),
        QuestionsAnsweredExtractor(questions=3),
        SummaryExtractor(summaries=["prev", "self"]),
        SentenceSplitter(),
    ]
)

docs = SimpleDirectoryReader("./docs").load_data()
nodes = pipeline.run(documents=docs)
index = VectorStoreIndex(nodes)

index.storage_context.persist(persist_dir=PERSIST_DIR)
print("✅ Índice generado y guardado correctamente.")
