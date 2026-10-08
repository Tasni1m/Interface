from fastapi import FastAPI
from routers import segments
from sqlalchemy import text

from database import engine

app = FastAPI()


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

