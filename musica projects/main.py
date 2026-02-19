from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import sound_analysis, atmosphere, noise_masking
from config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "AtmoSphere: Audio ambiental inteligente para negocios. "
        "Combina generacion de musica con IA y enmascaramiento acustico (SilenceOS). "
        "Ideal para hoteles, restaurantes, spas, oficinas y retail."
    ),
)

# CORS - permitir acceso desde cualquier origen en desarrollo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(atmosphere.router)
app.include_router(noise_masking.router)
app.include_router(sound_analysis.router, tags=["Audio Analysis"])


@app.get("/", tags=["Health"])
def read_root():
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "status": "running",
        "products": {
            "atmosphere": "Audio ambiental generativo para negocios",
            "silence_os": "Enmascaramiento acustico inteligente",
        },
        "docs": "/docs",
    }
