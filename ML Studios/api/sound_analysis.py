from fastapi import APIRouter, UploadFile
from services.sound_processor import analyze_sound

router = APIRouter()

@router.post("/analyze")
async def analyze_audio(file: UploadFile):
    """
    Endpoint para analizar un archivo de audio WAV.
    """
    if file.content_type != "audio/wav":
        return {"error": "Only WAV files are supported"}
    
    analysis_result = await analyze_sound(file)
    return analysis_result
