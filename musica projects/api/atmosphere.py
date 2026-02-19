from fastapi import APIRouter, HTTPException

from schemas.atmosphere import GenerateRequest, GenerateResponse, Scene
from services.music_generator import generate_ambient_music, get_scene, get_scenes
from config import settings

router = APIRouter(prefix="/atmosphere", tags=["AtmoSphere - Audio Ambiental"])


@router.get("/scenes", response_model=list[Scene])
def list_scenes():
    """Lista todas las escenas pre-configuradas por tipo de negocio."""
    return get_scenes()


@router.get("/scenes/{scene_id}", response_model=Scene)
def get_scene_detail(scene_id: str):
    """Obtiene el detalle de una escena especifica."""
    scene = get_scene(scene_id)
    if not scene:
        raise HTTPException(status_code=404, detail=f"Escena '{scene_id}' no encontrada")
    return scene


@router.post("/generate", response_model=GenerateResponse)
def generate_audio(request: GenerateRequest):
    """
    Genera audio ambiental segun los parametros o una escena pre-configurada.

    Si se provee `scene_id`, se usan los parametros de esa escena.
    Si no, se deben proveer `mood`, `energy` y `genre`.
    """
    if request.scene_id:
        scene = get_scene(request.scene_id)
        if not scene:
            raise HTTPException(
                status_code=404,
                detail=f"Escena '{request.scene_id}' no encontrada",
            )
    elif request.mood and request.energy and request.genre:
        scene = Scene(
            id="custom",
            name="Custom Scene",
            description="Escena personalizada",
            mood=request.mood,
            energy=request.energy,
            genre=request.genre,
            target_business="Custom",
        )
    else:
        raise HTTPException(
            status_code=422,
            detail="Debes proveer 'scene_id' o los campos 'mood', 'energy' y 'genre'",
        )

    audio_base64 = generate_ambient_music(scene, request.duration_seconds)

    return GenerateResponse(
        scene=scene,
        duration_seconds=request.duration_seconds,
        sample_rate=settings.sample_rate,
        audio_base64=audio_base64,
    )
