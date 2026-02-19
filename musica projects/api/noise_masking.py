from fastapi import APIRouter

from schemas.noise_masking import MaskingRequest, MaskingResponse, NoiseProfile
from services.noise_masking import generate_masking_audio, get_profiles
from config import settings

router = APIRouter(prefix="/masking", tags=["SilenceOS - Noise Masking"])


@router.get("/profiles", response_model=list[NoiseProfile])
def list_profiles():
    """Lista todos los perfiles de ruido disponibles para enmascaramiento."""
    return get_profiles()


@router.post("/generate", response_model=MaskingResponse)
def generate_masking(request: MaskingRequest):
    """
    Genera audio de enmascaramiento acustico.

    Tipos disponibles:
    - **white**: Ruido blanco uniforme
    - **pink**: Ruido rosa 1/f (natural, relajante)
    - **brown**: Ruido marron (graves profundos)
    - **speech-masking**: Optimizado para enmascarar conversaciones
    - **office-hum**: Zumbido sutil de oficina
    """
    audio_base64 = generate_masking_audio(
        noise_type=request.noise_type,
        intensity=request.intensity,
        duration_seconds=request.duration_seconds,
    )

    return MaskingResponse(
        noise_type=request.noise_type,
        intensity=request.intensity,
        duration_seconds=request.duration_seconds,
        sample_rate=settings.sample_rate,
        audio_base64=audio_base64,
    )
