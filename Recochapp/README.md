# Recochapp

Plataforma para organizar y encontrar partidos de fútbol casual ("recochas") en tu ciudad.

## Estructura

```
Recochapp/
├── backend/                 # API REST (Python)
│   ├── app/
│   │   ├── main.py          # Entry point FastAPI
│   │   ├── api/
│   │   │   ├── api.py       # Router principal
│   │   │   ├── deps.py      # Dependencies (auth, db)
│   │   │   └── v1/endpoints/
│   │   │       ├── login.py
│   │   │       ├── users.py
│   │   │       └── matches.py
│   │   ├── core/
│   │   │   ├── config.py    # Settings (DB, JWT)
│   │   │   └── security.py  # JWT + bcrypt
│   │   ├── db/
│   │   │   ├── base.py      # Alembic imports
│   │   │   ├── base_class.py # SQLAlchemy Base
│   │   │   └── session.py   # DB session
│   │   ├── models/
│   │   │   └── user.py      # SQLAlchemy models
│   │   └── schemas/
│   │       ├── user.py      # Pydantic schemas
│   │       ├── match.py
│   │       └── token.py
│   ├── tests/
│   │   ├── test_api.py
│   │   └── locustfile.py    # Load testing
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/                # Web App (TypeScript)
│   ├── app/
│   │   ├── page.tsx         # Home page
│   │   ├── login/page.tsx   # Login page
│   │   └── globals.css
│   ├── Dockerfile
│   ├── package.json
│   └── tailwind.config.js
│
├── docs/                    # Documentación
│   ├── 01-necesidades.md
│   ├── 02-roadmap.md
│   ├── 03-modelo-negocio.md
│   └── 04-ideas-features.md
│
└── docker-compose.yml       # Orquestación (db + redis + backend + frontend)
```

## Quick Start

```bash
# Levantar todo con Docker
docker-compose up -d

# Backend: http://localhost:8000
# Frontend: http://localhost:3000
# DB: PostgreSQL en puerto 5432
# Cache: Redis en puerto 6379
```

## Tech Stack

**Backend:** FastAPI, SQLAlchemy, PostgreSQL, Redis, JWT (python-jose)
**Frontend:** Next.js 14, React 18, Tailwind CSS, Lucide Icons
**Infra:** Docker Compose, Alembic (migraciones)

## API Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Health check |
| POST | `/api/v1/login/access-token` | Login (OAuth2) |
| GET | `/api/v1/users/` | Listar usuarios |
| POST | `/api/v1/users/` | Crear usuario |
| GET | `/api/v1/matches/` | Listar recochas |
| POST | `/api/v1/matches/` | Crear recocha (auth) |

## Concepto

- **Jugador:** Busca partidos cerca, ve cupos, se une
- **Organizador:** Crea partido, gestiona jugadores, define cancha/horario
- **Futuro:** Rankings, badges, torneos, perfil de jugador

## Documentación

- [Necesidades y requisitos](docs/01-necesidades.md)
- [Roadmap de implementación](docs/02-roadmap.md)
- [Modelo de negocio](docs/03-modelo-negocio.md)
- [Ideas y features futuros](docs/04-ideas-features.md)
