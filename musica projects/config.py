from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AtmoSphere API"
    app_version: str = "0.1.0"
    debug: bool = False

    # Audio defaults
    sample_rate: int = 44100
    bit_depth: int = 16
    max_duration_seconds: int = 300  # 5 minutes max per generation
    default_duration_seconds: int = 30

    class Config:
        env_file = ".env"


settings = Settings()
