from pydantic import BaseModel, Field
from enum import Enum


class NoiseType(str, Enum):
    white = "white"
    pink = "pink"
    brown = "brown"
    speech_masking = "speech-masking"
    office_hum = "office-hum"


class NoiseProfile(BaseModel):
    id: str
    name: str
    description: str
    noise_type: NoiseType
    recommended_for: str
    frequency_range: str


class MaskingRequest(BaseModel):
    noise_type: NoiseType = Field(
        NoiseType.pink,
        description="Tipo de ruido para enmascaramiento",
    )
    intensity: float = Field(
        0.5,
        ge=0.0,
        le=1.0,
        description="Intensidad del enmascaramiento (0.0 = silencio, 1.0 = maximo)",
    )
    duration_seconds: int = Field(
        30,
        ge=5,
        le=300,
        description="Duracion en segundos (5-300)",
    )


class MaskingResponse(BaseModel):
    noise_type: NoiseType
    intensity: float
    duration_seconds: int
    sample_rate: int
    format: str = "wav"
    audio_base64: str = Field(description="Audio WAV codificado en base64")
    message: str = "Audio de enmascaramiento generado exitosamente"
