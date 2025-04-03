#!/bin/bash
set -e

echo "Limpiando carpeta storage..."
python limpiar_storage.py

echo "Generando índice vectorial..."
python script_indexar_openai.py

echo "Iniciando servidor FastAPI..."
uvicorn main:app --host 0.0.0.0 --port $PORT
