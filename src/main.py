from fastapi import FastAPI
from . import models
from .database import engine

# create database tables
models.Base.metadata.create_all(bind=engine)

# initialize the fastapi application
app = FastAPI(
    title="CommodityPiper API",
    description="Data pipeline for international commodity trading",
    version="1.0.0"
)

# root health check endpoint
@app.get("/")
def read_root():
    return {"status": "healthy", "pipeline": "commoditypiper active"}