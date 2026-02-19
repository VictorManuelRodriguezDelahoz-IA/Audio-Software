# musica projects

Laboratorio de soluciones de audio con Machine Learning e IA Generativa.

## Producto Principal: AtmoSphere

**AtmoSphere** es una plataforma B2B que combina generacion de musica ambiental con IA y enmascaramiento acustico inteligente. Diseñada para hoteles, restaurantes, spas, oficinas y retail.

Fusiona dos productos originales:
- **Atmosphere AI** - Musica generativa royalty-free adaptada al contexto
- **SilenceOS** - Enmascaramiento acustico para privacidad y concentracion

### Estado actual: MVP funcional

| Feature | Estado | Detalles |
|---------|--------|----------|
| Generacion de audio ambiental | Funcional (DSP) | 6 escenas de negocio, sintesis en tiempo real |
| Noise masking | Funcional (DSP real) | 5 perfiles (white, pink, brown, speech, office) |
| Analisis de audio | Funcional | Frecuencias low/mid/high con Librosa |
| Modelos de IA (MusicGen) | Pendiente | Arquitectura preparada para integracion |
| Base de datos | Pendiente | - |
| Autenticacion | Pendiente | - |

## Quick Start

```bash
cd "musica projects"
pip install -r requirements.txt
uvicorn main:app --reload
# Abrir http://localhost:8000/docs para Swagger UI
```

## API

### AtmoSphere - Audio Ambiental

| Metodo | Ruta | Descripcion |
|--------|------|-------------|
| `GET` | `/atmosphere/scenes` | Lista 6 escenas pre-configuradas |
| `GET` | `/atmosphere/scenes/{id}` | Detalle de una escena |
| `POST` | `/atmosphere/generate` | Genera musica ambiental |

**Escenas disponibles:** `hotel-lobby`, `spa-relax`, `restaurant-dinner`, `office-focus`, `retail-energy`, `cafe`

**Ejemplo:**
```bash
curl -X POST http://localhost:8000/atmosphere/generate \
  -H "Content-Type: application/json" \
  -d '{"scene_id": "hotel-lobby", "duration_seconds": 30}'
```

### SilenceOS - Noise Masking

| Metodo | Ruta | Descripcion |
|--------|------|-------------|
| `GET` | `/masking/profiles` | Lista 5 perfiles de ruido |
| `POST` | `/masking/generate` | Genera audio de enmascaramiento |

**Perfiles disponibles:** `white`, `pink`, `brown`, `speech-masking`, `office-hum`

**Ejemplo:**
```bash
curl -X POST http://localhost:8000/masking/generate \
  -H "Content-Type: application/json" \
  -d '{"noise_type": "pink", "intensity": 0.6, "duration_seconds": 30}'
```

### Audio Analysis

| Metodo | Ruta | Descripcion |
|--------|------|-------------|
| `POST` | `/analyze` | Analiza archivo WAV (low/mid/high frequencies) |

## Estructura

```
musica projects/
├── config.py                    # Settings (pydantic-settings)
├── main.py                      # FastAPI + CORS + routers
├── requirements.txt             # Dependencias
├── api/
│   ├── atmosphere.py            # Router: /atmosphere/*
│   ├── noise_masking.py         # Router: /masking/*
│   └── sound_analysis.py        # Router: /analyze
├── schemas/
│   ├── __init__.py              # Exports
│   ├── atmosphere.py            # Schemas de AtmoSphere
│   └── noise_masking.py         # Schemas de SilenceOS
├── services/
│   ├── music_generator.py       # Sintesis DSP + escenas
│   ├── noise_masking.py         # Ruido coloreado (DSP real)
│   └── sound_processor.py       # Analisis con Librosa
├── utils/
│   └── file_utils.py            # Utilidades
└── docs/
    ├── 01-necesidades.md        # Necesidades por producto
    ├── 02-roadmap.md            # Roadmap 5 años
    ├── 03-modelo-negocio.md     # Business model
    └── 04-ideas-adicionales.md  # Ideas experimentales
```

## Tech Stack

- **Backend:** FastAPI, Pydantic, pydantic-settings
- **DSP:** NumPy, SciPy (Butterworth filters, Voss-McCartney)
- **Audio Analysis:** Librosa
- **Futuro:** Hugging Face (MusicGen, AudioCraft), PyTorch

## Otros Productos (en roadmap)

| Producto | Target | Estado |
|----------|--------|--------|
| **Lumina-Sync** | Streamers, VTubers | Documentado, no iniciado |

## Documentacion

- [Necesidades por producto](docs/01-necesidades.md)
- [Roadmap de implementacion](docs/02-roadmap.md)
- [Modelo de negocio](docs/03-modelo-negocio.md)
- [Ideas experimentales](docs/04-ideas-adicionales.md)
- [Investigacion de mercado 2026](../docs/oportunidades-negocio/global/investigacion-audio-ai-2026.md)
