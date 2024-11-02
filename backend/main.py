# backend/main.py
from fastapi import FastAPI
from routers import sdr_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the NOAA Satellite API!"}

app.include_router(sdr_router.router)
