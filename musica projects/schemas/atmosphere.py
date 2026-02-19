from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional


class Mood(str, Enum):
    calm = "calm"
    zen = "zen"
    warm = "warm"
    neutral = "neutral"
    upbeat = "upbeat"
    cozy = "cozy"
    energetic = "energetic"


class EnergyLevel(str, Enum):
    very_low = "very-low"
    low = "low"
    medium_low = "medium-low"
    medium = "medium"
    medium_high = "medium-high"
    high = "high"


class Genre(str, Enum):
    ambient_jazz = "ambient-jazz"
    nature_ambient = "nature-ambient"
    bossa_lounge = "bossa-lounge"
    minimal_electronic = "minimal-electronic"
    pop_instrumental = "pop-instrumental"
    acoustic_chill = "acoustic-chill"
    deep_ambient = "deep-ambient"
    lo_fi = "lo-fi"


class Scene(BaseModel):
    id: str
    name: str
    description: str
    mood: Mood
    energy: EnergyLevel
    genre: Genre
    target_business: str

    model_config = {"json_schema_extra": {
        "examples": [{
            "id": "hotel-lobby",
            "name": "Hotel Lobby",
            "description": "Ambient jazz suave para recepciones de hotel",
            "mood": "calm",
            "energy": "low",
            "genre": "ambient-jazz",
            "target_business": "Hotels & Hospitality",
        }]
    }}


class GenerateRequest(BaseModel):
    scene_id: Optional[str] = Field(
        None,
        description="ID de escena pre-configurada. Si se provee, sobreescribe mood/energy/genre.",
    )
    mood: Optional[Mood] = Field(None, description="Estado de animo del audio")
    energy: Optional[EnergyLevel] = Field(None, description="Nivel de energia")
    genre: Optional[Genre] = Field(None, description="Genero musical")
    duration_seconds: int = Field(
        30,
        ge=5,
        le=300,
        description="Duracion en segundos (5-300)",
    )


class GenerateResponse(BaseModel):
    scene: Scene
    duration_seconds: int
    sample_rate: int
    format: str = "wav"
    audio_base64: str = Field(description="Audio WAV codificado en base64")
    message: str = "Audio generado exitosamente"
