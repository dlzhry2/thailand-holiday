import boto3
from botocore.exceptions import ClientError


class S3Manager:
    """
    A class to manage AWS Systems Manager.
    """

    def __init__(self, bucket_name: str):
        self.aws_s3_client = boto3.client('s3')
        self.bucket_name = bucket_name

    def save(self, object_bytes: bytes, key: str, metadata: dict):
        self.aws_s3_client.put_object(Body=object_bytes, Key=key, Bucket=self.bucket_name, Metadata=metadata)

    def get(self, key: str):
        try:
            s3_response = self.aws_s3_client.get_object(Bucket=self.bucket_name, Key=key)

        except ClientError:
            return None

        photo_response = photo_payload_converter(s3_response, key)

        return photo_response

    def get_all(self) -> list:
        obj_list = self.aws_s3_client.list_objects(Bucket=self.bucket_name)["Contents"]
        photo_keys = []

        if not obj_list:
            return []

        for obj in obj_list:
            photo_keys.append(obj["Key"])

        return photo_keys


def photo_payload_converter(s3_object: dict, key: str) -> dict:
    """Converts AWS S3 object response into valid photo response object"""
    photo_bytes = s3_object["Body"].read()
    meta_data = s3_object["Metadata"]

    return {
        "base64Image": photo_bytes.decode(),
        "caption": meta_data["caption"],
        "imageFileName": key,
        "location": meta_data["location"]
    }
