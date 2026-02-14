# Importar todos los modelos aquí para que Alembic (migraciones) los detecte
from app.db.base_class import Base
from app.models.user import User
from app.models.match import Match