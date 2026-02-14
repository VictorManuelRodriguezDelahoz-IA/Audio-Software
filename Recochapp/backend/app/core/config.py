from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Recochapp API"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "CAMBIAR_ESTO_POR_UN_SECRETO_REAL_EN_PRODUCCION"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 días
    
    # Configuración de Base de Datos (Valores por defecto para Docker)
    POSTGRES_SERVER: str = "db"
    POSTGRES_USER: str = "recochapp_user"
    POSTGRES_PASSWORD: str = "recochapp_password"
    POSTGRES_DB: str = "recochapp_db"
    
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"

settings = Settings()