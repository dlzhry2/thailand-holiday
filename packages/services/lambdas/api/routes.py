"""
Module for handling application routes.
"""

from fastapi import APIRouter
from fastapi.routing import APIRoute
from api.ports.photos.photo_handler import PhotoHandler

photo_handler = PhotoHandler()

router = APIRouter(
    routes=[
        APIRoute("/rest/photos", endpoint=photo_handler.save, methods=["POST"]),
        APIRoute("/rest/photos", endpoint=photo_handler.get_all, methods=["GET"]),
        APIRoute("/rest/photos/{photo_id}", endpoint=photo_handler.get, methods=["GET"])
    ]
)
