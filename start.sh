#!/bin/bash

# Limpiar carpeta storage
echo "Limpiando carpeta storage..."
python limpiar_storage.py

# Generar índice vectorial
echo "Generando índice vectorial..."
python script_indexar_openai.py

# Iniciar servidor FastAPI
echo "Iniciando servidor FastAPI..."
uvicorn main:app --host 0.0.0.0 --port $PORT