from fastapi import FastAPI
from api import sound_analysis

app = FastAPI()

# Registrar los endpoints
app.include_router(sound_analysis.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to musica projects API"}
