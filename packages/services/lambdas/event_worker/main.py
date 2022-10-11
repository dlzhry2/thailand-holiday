"""
Module for app initialisation.
"""
import logging
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from api.adapters.aws.blob_storage import S3Manager


def lambda_handler(event, context):
    """Handles events triggered by the EventBus"""

    s3_manager = S3Manager("thailandphotobucket")
    _, video_keys = s3_manager.get_all()

    if not video_keys:
        return None

    with ThreadPoolExecutor(max_workers=len(video_keys)) as executor:
        futures = [executor.submit(s3_manager.delete, vid_key) for vid_key in video_keys]

        for future in as_completed(futures):
            # get the downloaded url data
            result = future.result()

            if not result:
                logging.info("Failed to delete object")

    return True
