import base64
import io
import struct
import wave

import numpy as np
from scipy.signal import butter, sosfilt

from config import settings
from schemas.noise_masking import NoiseProfile, NoiseType

# Pre-defined noise profiles
NOISE_PROFILES: list[NoiseProfile] = [
    NoiseProfile(
        id="white",
        name="White Noise",
        description="Ruido blanco uniforme. Todas las frecuencias con igual energia.",
        noise_type=NoiseType.white,
        recommended_for="Concentracion general, bloqueo de ruido ambiental",
        frequency_range="20 Hz - 20 kHz (uniforme)",
    ),
    NoiseProfile(
        id="pink",
        name="Pink Noise",
        description="Ruido rosa (1/f). Mas graves, menos agudos. Sonido natural y relajante.",
        noise_type=NoiseType.pink,
        recommended_for="Oficinas, salas de espera, ambientes de trabajo",
        frequency_range="20 Hz - 20 kHz (enfasis en graves)",
    ),
    NoiseProfile(
        id="brown",
        name="Brown Noise",
        description="Ruido marron (browniano). Graves profundos, muy relajante.",
        noise_type=NoiseType.brown,
        recommended_for="Spas, meditacion, salas de descanso, dormir",
        frequency_range="20 Hz - 5 kHz (graves dominantes)",
    ),
    NoiseProfile(
        id="speech-masking",
        name="Speech Masking",
        description="Optimizado para enmascarar conversaciones. Filtra frecuencias vocales.",
        noise_type=NoiseType.speech_masking,
        recommended_for="Call centers, oficinas abiertas, salas de reuniones",
        frequency_range="300 Hz - 3 kHz (banda vocal)",
    ),
    NoiseProfile(
        id="office-hum",
        name="Office Hum",
        description="Simulacion del zumbido suave de oficina. HVAC + electronica.",
        noise_type=NoiseType.office_hum,
        recommended_for="Oficinas silenciosas que necesitan ruido de fondo sutil",
        frequency_range="50 Hz - 500 Hz (baja frecuencia)",
    ),
]


def get_profiles() -> list[NoiseProfile]:
    return NOISE_PROFILES


def _generate_white_noise(num_samples: int) -> np.ndarray:
    return np.random.randn(num_samples)


def _generate_pink_noise(num_samples: int) -> np.ndarray:
    """Pink noise using the Voss-McCartney algorithm."""
    num_rows = 16
    array = np.full((num_rows, num_samples), np.nan)
    array[0, :] = np.random.randn(num_samples)
    array[:, 0] = np.random.randn(num_rows)

    cols = np.random.geometric(0.5, num_samples)
    cols = np.clip(cols, 0, num_rows - 1)

    for i in range(1, num_samples):
        array[:, i] = array[:, i - 1]
        col = cols[i]
        array[col, i] = np.random.randn()

    result = np.nansum(array, axis=0)
    # Normalize
    result = result / np.max(np.abs(result))
    return result


def _generate_brown_noise(num_samples: int) -> np.ndarray:
    """Brown noise via cumulative sum of white noise."""
    white = np.random.randn(num_samples)
    brown = np.cumsum(white)
    # Normalize to [-1, 1]
    brown = brown / np.max(np.abs(brown))
    return brown


def _generate_speech_masking(num_samples: int, sr: int) -> np.ndarray:
    """Band-pass filtered noise targeting speech frequencies (300-3000 Hz)."""
    white = np.random.randn(num_samples)
    sos = butter(4, [300, 3000], btype="band", fs=sr, output="sos")
    filtered = sosfilt(sos, white)
    filtered = filtered / np.max(np.abs(filtered))
    return filtered


def _generate_office_hum(num_samples: int, sr: int) -> np.ndarray:
    """Low-frequency hum simulating HVAC and electronics."""
    white = np.random.randn(num_samples)
    sos = butter(4, 500, btype="low", fs=sr, output="sos")
    filtered = sosfilt(sos, white)

    # Add subtle 60Hz hum (electrical frequency)
    t = np.arange(num_samples) / sr
    hum = 0.15 * np.sin(2 * np.pi * 60 * t)
    hum += 0.08 * np.sin(2 * np.pi * 120 * t)  # 2nd harmonic

    result = filtered + hum
    result = result / np.max(np.abs(result))
    return result


def _to_wav_base64(audio: np.ndarray, sr: int, intensity: float) -> str:
    """Convert numpy array to WAV base64 string."""
    # Apply intensity and convert to 16-bit PCM
    audio = audio * intensity * 0.8  # 0.8 headroom to avoid clipping
    audio = np.clip(audio, -1.0, 1.0)
    pcm = (audio * 32767).astype(np.int16)

    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sr)
        wf.writeframes(pcm.tobytes())

    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode("utf-8")


def generate_masking_audio(
    noise_type: NoiseType,
    intensity: float,
    duration_seconds: int,
) -> str:
    """Generate masking noise audio and return as base64 WAV."""
    sr = settings.sample_rate
    num_samples = sr * duration_seconds

    generators = {
        NoiseType.white: lambda: _generate_white_noise(num_samples),
        NoiseType.pink: lambda: _generate_pink_noise(num_samples),
        NoiseType.brown: lambda: _generate_brown_noise(num_samples),
        NoiseType.speech_masking: lambda: _generate_speech_masking(num_samples, sr),
        NoiseType.office_hum: lambda: _generate_office_hum(num_samples, sr),
    }

    audio = generators[noise_type]()
    return _to_wav_base64(audio, sr, intensity)
