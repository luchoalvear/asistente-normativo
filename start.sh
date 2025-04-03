#!/bin/bash
set -e

echo "Limpiando carpeta storage..."
python limpiar_storage.py

echo "Iniciando servidor FastAPI..."
uvicorn main:app --host 0.0.0.0 --port $PORT
