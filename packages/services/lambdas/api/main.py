"""
Module for app initialisation.
"""
from fastapi import FastAPI
from mangum import Mangum
from api.routes import router

app = FastAPI(docs_url=None)
app.include_router(router)

handler = Mangum(app)
