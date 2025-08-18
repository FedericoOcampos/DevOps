from fastapi import FastAPI
from app.api.time import router as time_router

app = FastAPI()

app.include_router(time_router)

@app.get("/")
def read_root():
    return {"message": "Que onda perros!"}