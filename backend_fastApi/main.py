from fastapi import FastAPI
from routers import segments
from sqlalchemy import text

from database import engine

app = FastAPI()

app.include_router(segments.router)    


@app.get("/")
def accueil():
    return {"message": "FastAPI fonctionne"}




@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        postgis_version = connection.execute(
            text("SELECT PostGIS_Version();")
        ).scalar()

    return {
        "connexion": "PostgreSQL connecté",
        "postgis": postgis_version
    }

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import segments


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)