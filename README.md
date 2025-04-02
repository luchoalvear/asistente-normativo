
# ProyectaGPT – Indexador de Documentos con Metadata

Este proyecto te permite cargar documentos PDF relacionados con normativa urbana y proyectos de inversión pública en Chile, junto con su metadata, para construir un índice vectorial usando LlamaIndex.

---

## 📁 Estructura de carpetas recomendada

```
/tu-proyecto/
├── docs/                   ← Carpeta con los archivos PDF
│   ├── DECRETO-548.pdf
│   ├── OGUC.pdf
│   └── ...
├── metadata.json           ← Archivo con metadata para cada PDF
├── script_indexar.py       ← Script para indexar documentos
└── README.md
```

---

## 🧠 ¿Qué contiene la metadata?

Cada entrada del `metadata.json` contiene:

- `nombre`: Nombre del documento
- `tipo`: General, Específico, Instructivo, etc.
- `descripcion`: Breve resumen del documento

La metadata se utiliza para enriquecer las respuestas del agente y mejorar su comprensión de los documentos cargados.

---

## ▶️ ¿Cómo usar el script?

1. Asegúrate de tener instaladas las dependencias de LlamaIndex:
```bash
pip install llama-index
```

2. Ejecuta el script:
```bash
python script_indexar.py
```

Esto generará una carpeta de almacenamiento con el índice listo para ser cargado en tu servidor FastAPI.

---

## 🧩 Integración con el servidor FastAPI

Para cargar el índice en tu API:

```python
from llama_index.core import StorageContext, load_index_from_storage

storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)
```

---

## 📝 Contacto

Desarrollado por Luis Gonzalo Alvear — Consultor en Inversión Pública y Transformación Digital.
