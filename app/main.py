from fastapi import FastAPI
from app.endpoints import home
import app.models
from app.db import engine

app.models.Base.metadata.create_all(bind=engine)

app = FastAPI()

COMPONENTS_ENDPOINTS = [home.endpoint]

for endpoint in COMPONENTS_ENDPOINTS:   
    app.include_router(endpoint.router,prefix=endpoint.prefix)
