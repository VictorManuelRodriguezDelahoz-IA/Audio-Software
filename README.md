# Audio Software

Repositorio de emprendimiento personal: proyectos de Audio, Tech y Hardware.

## Proyectos

### [Recochapp](Recochapp/) - Fútbol Casual
Plataforma para organizar y encontrar partidos de fútbol casual en tu ciudad.
- **Backend:** FastAPI + PostgreSQL + Redis
- **Frontend:** Next.js + Tailwind CSS
- **Estado:** En desarrollo

### [ML Studios](ML%20Studios/) - Audio + IA
Laboratorio de soluciones de audio con Machine Learning.
- **Productos:** SilenceOS (oficinas), Lumina-Sync (streamers), Atmosphere AI (hospitality)
- **Tech:** FastAPI + Hugging Face + Librosa
- **Estado:** Refactorización

## Documentación Global

### [docs/startup-hq/](docs/startup-hq/)
Sincronizado desde [Notion](https://www.notion.so/Startup-2ff43c54da3d8015a5ebf7992d0ceaff) - centro de comando de todos los emprendimientos.

### [docs/oportunidades-negocio/](docs/oportunidades-negocio/)
Investigación de oportunidades en Colombia, USA y Alemania ([23 ideas iniciales](docs/oportunidades-negocio/IDEAS-INICIALES.md)).

### [docs/notion-sync/](docs/notion-sync/)
Configuración de la sincronización automática Notion → GitHub.

## Sincronización con Notion

```bash
# Setup inicial
cp .env.local.example .env   # Agrega tu NOTION_TOKEN
pip install notion-client python-dotenv

# Sincronizar
python scripts/sync_notion.py
```

Se ejecuta automáticamente cada lunes vía GitHub Actions.

## Estructura

```
├── Recochapp/
│   ├── backend/         # FastAPI (Python)
│   ├── frontend/        # Next.js (TypeScript)
│   ├── docs/            # Documentación del proyecto
│   └── docker-compose.yml
│
├── ML Studios/
│   ├── api/             # Endpoints FastAPI
│   ├── services/        # Procesamiento de audio
│   └── docs/            # Documentación del proyecto
│
├── docs/
│   ├── startup-hq/      # Sync desde Notion
│   ├── oportunidades-negocio/  # Research por país
│   └── notion-sync/     # Config de sincronización
│
└── scripts/
    └── sync_notion.py   # Script de sync
```

## Skills

La skill **business-analyst** (`.claude/skills/`) permite:
- Evaluar proyectos existentes
- Investigar oportunidades por mercado/sector
- Analizar y comparar ideas de negocio
