from fastapi import FastAPI
from routers import segments
app = FastAPI()


@app.get("/")
def accueil():
    return {"message": "FastAPI fonctionne"}


    app.include_router(segments.router)