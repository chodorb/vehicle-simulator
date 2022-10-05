from fastapi import FastAPI
from app.endpoints import home


app = FastAPI()

COMPONENTS_ENDPOINTS = [home.endpoint]

for endpoint in COMPONENTS_ENDPOINTS:   
    app.include_router(endpoint.router,prefix=endpoint.prefix)
