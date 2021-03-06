from fastapi import FastAPI
from db import models
from db.database import engine
from routers import router_routes, service_routes, client_routes
#from auth import authentication
#from fastapi.middleware.cors import CORSMiddleware

app= FastAPI()



@app.get("/")
def root():
    return "Hello world!"

app.include_router(router_routes.router)
app.include_router(service_routes.service)
app.include_router(client_routes.client)


""" origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
) """

models.Base.metadata.create_all(engine)
