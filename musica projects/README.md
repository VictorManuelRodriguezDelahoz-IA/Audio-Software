# musica projects

Laboratorio de soluciones de audio con Machine Learning e IA Generativa.

## Productos

| Producto | Target | Concepto |
|----------|--------|----------|
| **SilenceOS** | Call centers, oficinas | Enmascaramiento acústico adaptativo |
| **Lumina-Sync** | Streamers, VTubers | Viewers controlan entorno físico del streamer |
| **Atmosphere AI** | Hoteles, spas, retail | Música generativa libre de derechos |

## Estructura

```
musica projects/
├── api/
│   └── sound_analysis.py    # Endpoint de análisis de audio
├── services/
│   └── sound_processor.py   # Procesamiento con Librosa (STFT, frecuencias)
├── schemas/
│   └── __init__.py
├── utils/
│   └── file_utils.py        # Utilidades de archivos
├── docs/                    # Documentación del proyecto
├── main.py                  # Entry point FastAPI
└── requirements.txt
```

## Quick Start

```bash
cd "musica projects"
pip install -r requirements.txt
uvicorn main:app --reload

# POST /analyze → Sube un WAV, devuelve análisis de frecuencias
```

## API

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Health check |
| POST | `/analyze` | Analiza archivo WAV (low/mid/high frequencies) |

## Tech Stack

**Backend:** FastAPI, Librosa, NumPy
**Modelos:** Hugging Face (MusicGen, AudioCraft, Riffusion)
**Hardware futuro:** ESP32 "NeuroSense" (micrófono IoT)

## Documentación

- [Necesidades por producto](docs/01-necesidades.md)
- [Roadmap de implementación](docs/02-roadmap.md)
- [Modelo de negocio](docs/03-modelo-negocio.md)
- [Ideas experimentales](docs/04-ideas-adicionales.md)
