import os
import logging
from json import JSONDecodeError
from typing import Union
from fastapi import Header
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from api.adapters.aws.blob_storage import S3Manager
from api.common.validation.validate import Validator


class PhotoHandler:

    def __init__(self):
        self.s3_manager = S3Manager("thailandphotobucket")
        self.auth_token = os.getenv("AUTH_TOKEN")
        self.headers = {"Access-Control-Allow-Origin": "*"}

    async def save(self, request: Request, x_thai_api_token: Union[str, None] = Header(default=None)):
        try:
            payload = await request.json()
        except (JSONDecodeError, TypeError) as exception:
            logging.error(exception)
            return JSONResponse({"error": "Invalid request"}, status_code=400, headers=self.headers)

        validator = Validator(payload)
        validator.validate_save_photos()

        errors = validator.get_errors()

        if errors:
            return JSONResponse(errors, status_code=400, headers=self.headers)

        if x_thai_api_token != self.auth_token:
            return JSONResponse({"error": "Not authorised"}, status_code=403, headers=self.headers)

        self.s3_manager.save(
            payload["base64Image"].encode(),
            payload["imageName"],
            {
                "caption": payload["caption"],
                "location": payload["location"]
            }
        )

        return JSONResponse({"message": "success"}, headers=self.headers)

    def get(self, photo_id: str):
        photo = self.s3_manager.get(photo_id)

        if not photo:
            return JSONResponse({"error": "Not found"}, status_code=404, headers=self.headers)

        return JSONResponse(photo, headers=self.headers)

    def get_all(self):
        photos = self.s3_manager.get_all()

        return JSONResponse({"photos": photos}, headers=self.headers)
