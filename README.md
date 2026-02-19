# Audio Software

Repositorio de emprendimiento personal: proyectos de Audio, Tech y Hardware.

## Proyectos

### [musica projects](musica%20projects/) - Audio + IA (Principal)
Plataforma **AtmoSphere**: audio ambiental inteligente + noise masking para negocios.
- **Producto:** AtmoSphere (Atmosphere AI + SilenceOS fusionados)
- **Target:** Hoteles, restaurantes, spas, oficinas, retail
- **Tech:** FastAPI + NumPy + SciPy + Librosa
- **Estado:** MVP funcional (6 escenas, 5 perfiles de ruido, API completa)

### [Recochapp](Recochapp/) - Futbol Casual
Plataforma para organizar y encontrar partidos de futbol casual en tu ciudad.
- **Backend:** FastAPI + PostgreSQL + Redis
- **Frontend:** Next.js + Tailwind CSS
- **Estado:** Refactorizado, funcional

## Documentacion Global

### [docs/startup-hq/](docs/startup-hq/)
Sincronizado desde [Notion](https://www.notion.so/Startup-2ff43c54da3d8015a5ebf7992d0ceaff) - centro de comando de todos los emprendimientos.

### [docs/oportunidades-negocio/](docs/oportunidades-negocio/)
Investigacion de oportunidades en Colombia, USA y Alemania ([23 ideas iniciales](docs/oportunidades-negocio/IDEAS-INICIALES.md) + [investigacion audio+IA 2026](docs/oportunidades-negocio/global/investigacion-audio-ai-2026.md)).

### [docs/notion-sync/](docs/notion-sync/)
Configuracion de la sincronizacion automatica Notion -> GitHub.

### [ESTADO_DEL_PROYECTO.md](ESTADO_DEL_PROYECTO.md)
Estado actual completo del repositorio, decisiones tomadas, y proximos pasos.

## Sincronizacion con Notion

```bash
# Setup inicial
cp .env.local.example .env   # Agrega tu NOTION_TOKEN
pip install notion-client python-dotenv

# Sincronizar
python scripts/sync_notion.py
```

Se ejecuta automaticamente cada lunes via GitHub Actions.

## Estructura

```
├── musica projects/       # Audio + IA (AtmoSphere MVP)
│   ├── api/               # Endpoints FastAPI (atmosphere, masking, analyze)
│   ├── services/          # Logica de negocio (DSP, generacion, analisis)
│   ├── schemas/           # Pydantic models
│   └── docs/              # Documentacion del proyecto
│
├── Recochapp/
│   ├── backend/           # FastAPI (Python)
│   ├── frontend/          # Next.js (TypeScript)
│   ├── docs/              # Documentacion del proyecto
│   └── docker-compose.yml
│
├── docs/
│   ├── startup-hq/        # Sync desde Notion
│   ├── oportunidades-negocio/  # Research por pais + investigacion 2026
│   └── notion-sync/       # Config de sincronizacion
│
├── .claude/skills/        # 4 skills de asistencia (business, code, test, market)
│
└── scripts/
    └── sync_notion.py     # Script de sync
```

## Claude Skills

4 skills disponibles en `.claude/skills/`:

| Skill | Proposito |
|-------|-----------|
| **business-analyst** | Evaluar proyectos, investigar oportunidades, scoring 0-80 |
| **code-auditor** | Auditoria de codigo, seguridad, dependencias, arquitectura |
| **test-generator** | Generar y ejecutar tests (pytest, Jest, cobertura) |
| **market-researcher** | Investigar mercados, competencia, validar ideas, tendencias |
