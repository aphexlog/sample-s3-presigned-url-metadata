import os
import boto3
import json
import requests
from botocore.exceptions import ClientError

s3_client = boto3.client("s3")


def get_presigned_url(bucket_name, object_name, expiration=3600):
    try:
        response = s3_client.generate_presigned_url(
            "put_object",
            Params={"Bucket": bucket_name, "Key": object_name},
            ExpiresIn=expiration,
        )
        return response
    except ClientError as err:
        print(f"An error occurred: {err}")
        raise err


def lambda_handler(event, context):
    try:
        bucket_name = os.environ["BUCKET_NAME"]
        object_name = os.environ["OBJECT_NAME"]
        expiration = 3600  # seconds

        url = get_presigned_url(bucket_name, object_name, expiration)

        response = requests.put(url, data="Hello, World!")

        if response.status_code == 200:
            # Add metadata to the object
            s3_client.put_object(
                Bucket=bucket_name,
                Key=object_name,
                Metadata={"userId": "user123"},
            )

            return {
                "statusCode": 200,
                "body": json.dumps(
                    f"Successfully uploaded object {object_name} to bucket {bucket_name}."
                ),
                "response": f"{response.text}",
            }
        else:
            return {
                "statusCode": 500,
                "body": json.dumps(
                    f"Failed to upload object {object_name} to bucket {bucket_name}."
                ),
                "response": f"{response.text}",
            }
    except Exception as err:
        return {
            "statusCode": 500,
            "body": json.dumps(
                "An exception occurred. Check logs for more details."
            ),
            "response": str(err),
        }
