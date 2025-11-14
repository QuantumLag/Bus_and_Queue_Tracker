from fastapi import FastAPI
from database import engine
import models
from routers import bus

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(bus.router)
