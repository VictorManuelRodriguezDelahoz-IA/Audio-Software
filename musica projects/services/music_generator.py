import base64
import io
import wave

import numpy as np

from config import settings
from schemas.atmosphere import (
    EnergyLevel,
    Genre,
    Mood,
    Scene,
)

# Pre-defined scenes for different business types
SCENES: list[Scene] = [
    Scene(
        id="hotel-lobby",
        name="Hotel Lobby",
        description="Ambient jazz suave para recepciones de hotel. Elegante y acogedor.",
        mood=Mood.calm,
        energy=EnergyLevel.low,
        genre=Genre.ambient_jazz,
        target_business="Hotels & Hospitality",
    ),
    Scene(
        id="spa-relax",
        name="Spa & Relax",
        description="Sonidos naturales y pads ambientales para maxima relajacion.",
        mood=Mood.zen,
        energy=EnergyLevel.very_low,
        genre=Genre.nature_ambient,
        target_business="Spas, Wellness Centers",
    ),
    Scene(
        id="restaurant-dinner",
        name="Restaurant Dinner",
        description="Bossa nova y lounge suave para cenas. Calido y sofisticado.",
        mood=Mood.warm,
        energy=EnergyLevel.medium,
        genre=Genre.bossa_lounge,
        target_business="Restaurants, Wine Bars",
    ),
    Scene(
        id="office-focus",
        name="Office Focus",
        description="Electronica minimal para concentracion. Sin distracciones.",
        mood=Mood.neutral,
        energy=EnergyLevel.low,
        genre=Genre.minimal_electronic,
        target_business="Offices, Coworking Spaces",
    ),
    Scene(
        id="retail-energy",
        name="Retail Energy",
        description="Pop instrumental energetico para tiendas. Estimula compras.",
        mood=Mood.upbeat,
        energy=EnergyLevel.high,
        genre=Genre.pop_instrumental,
        target_business="Retail Stores, Shopping Malls",
    ),
    Scene(
        id="cafe",
        name="Cafe",
        description="Acustico chill para cafeterias. Ambiente cozy y creativo.",
        mood=Mood.cozy,
        energy=EnergyLevel.medium_low,
        genre=Genre.acoustic_chill,
        target_business="Cafes, Bakeries, Bookstores",
    ),
]

_SCENES_MAP: dict[str, Scene] = {s.id: s for s in SCENES}

# Energy to BPM mapping
_ENERGY_BPM = {
    EnergyLevel.very_low: 50,
    EnergyLevel.low: 70,
    EnergyLevel.medium_low: 85,
    EnergyLevel.medium: 100,
    EnergyLevel.medium_high: 115,
    EnergyLevel.high: 130,
}

# Genre to musical characteristics
_GENRE_NOTES = {
    Genre.ambient_jazz: [261.63, 329.63, 392.00, 440.00, 523.25],  # C maj7
    Genre.nature_ambient: [261.63, 293.66, 392.00, 523.25],  # C sus2/5
    Genre.bossa_lounge: [261.63, 311.13, 392.00, 466.16],  # C min7
    Genre.minimal_electronic: [130.81, 196.00, 261.63, 392.00],  # C5 octaves
    Genre.pop_instrumental: [261.63, 329.63, 392.00, 493.88],  # C maj
    Genre.acoustic_chill: [246.94, 329.63, 392.00, 493.88],  # B/E chord
    Genre.deep_ambient: [65.41, 130.81, 196.00, 261.63],  # Low C octaves
    Genre.lo_fi: [261.63, 311.13, 369.99, 466.16],  # C min9
}


def get_scenes() -> list[Scene]:
    return SCENES


def get_scene(scene_id: str) -> Scene | None:
    return _SCENES_MAP.get(scene_id)


def _apply_envelope(signal: np.ndarray, attack: int, release: int) -> np.ndarray:
    """Apply fade-in (attack) and fade-out (release) to a signal."""
    env = np.ones(len(signal))
    if attack > 0:
        env[:attack] = np.linspace(0, 1, attack)
    if release > 0:
        env[-release:] = np.linspace(1, 0, release)
    return signal * env


def _generate_pad(
    notes: list[float],
    duration_seconds: int,
    sr: int,
    energy: EnergyLevel,
) -> np.ndarray:
    """Generate a warm ambient pad from chord notes with slow modulation."""
    num_samples = sr * duration_seconds
    t = np.arange(num_samples) / sr
    signal = np.zeros(num_samples)

    for i, freq in enumerate(notes):
        # Main tone
        tone = np.sin(2 * np.pi * freq * t)
        # Slow vibrato for warmth
        vibrato = 1.0 + 0.003 * np.sin(2 * np.pi * (0.1 + i * 0.05) * t)
        tone = np.sin(2 * np.pi * freq * vibrato * t)
        # Slightly detune for richness
        tone += 0.3 * np.sin(2 * np.pi * (freq * 1.002) * t)
        signal += tone / len(notes)

    # Slow amplitude modulation for organic feel
    lfo = 0.7 + 0.3 * np.sin(2 * np.pi * 0.05 * t)
    signal *= lfo

    # Apply envelope
    attack = sr * 2  # 2 second fade in
    release = sr * 3  # 3 second fade out
    signal = _apply_envelope(signal, attack, release)

    return signal / np.max(np.abs(signal))


def _add_texture(
    signal: np.ndarray,
    sr: int,
    genre: Genre,
) -> np.ndarray:
    """Add genre-specific texture to the signal."""
    num_samples = len(signal)

    if genre in (Genre.nature_ambient, Genre.deep_ambient):
        # Add filtered noise for "air" / nature feel
        noise = np.random.randn(num_samples) * 0.05
        # Simple low-pass by averaging
        kernel_size = 100
        noise = np.convolve(noise, np.ones(kernel_size) / kernel_size, mode="same")
        signal += noise

    elif genre in (Genre.minimal_electronic, Genre.lo_fi):
        # Add subtle rhythmic pulse
        t = np.arange(num_samples) / sr
        bpm = 80 if genre == Genre.lo_fi else 100
        beat_freq = bpm / 60.0
        pulse = 0.08 * np.sin(2 * np.pi * beat_freq * t) ** 8
        signal += pulse

    elif genre == Genre.bossa_lounge:
        # Add gentle rhythmic swing
        t = np.arange(num_samples) / sr
        swing = 0.06 * np.sin(2 * np.pi * 1.33 * t) ** 4  # ~80 BPM feel
        signal += swing

    return signal / np.max(np.abs(signal))


def _to_wav_base64(audio: np.ndarray, sr: int) -> str:
    """Convert numpy array to WAV base64 string."""
    audio = np.clip(audio * 0.8, -1.0, 1.0)
    pcm = (audio * 32767).astype(np.int16)

    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(pcm.tobytes())

    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode("utf-8")


def generate_ambient_music(
    scene: Scene,
    duration_seconds: int,
) -> str:
    """
    Generate ambient music based on scene parameters.

    Currently uses DSP synthesis. Designed to be swapped with MusicGen/AudioCraft
    when GPU resources are available.
    """
    sr = settings.sample_rate
    notes = _GENRE_NOTES.get(scene.genre, _GENRE_NOTES[Genre.deep_ambient])

    # Generate base pad
    audio = _generate_pad(notes, duration_seconds, sr, scene.energy)

    # Add genre-specific texture
    audio = _add_texture(audio, sr, scene.genre)

    return _to_wav_base64(audio, sr)
