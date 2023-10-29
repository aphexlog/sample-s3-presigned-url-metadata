"""Get metadata from S3 object."""
import os
import boto3
from botocore.client import ClientError

s3_client = boto3.client("s3")


# Get metadata from S3 object
def get_metadata(bucket_name, object_name):
    try:
        response = s3_client.head_object(Bucket=bucket_name, Key=object_name)
    except ClientError as err:
        print(err)
        return None

    return response


def lambda_handler(event, context):
    bucket_name = os.environ["BUCKET_NAME"]
    object_name = os.environ["OBJECT_NAME"]

    metadata = get_metadata(bucket_name, object_name)

    if metadata:
        print(f"Metadata: {metadata}")

    return {
        "statusCode": 200,
        "Metadata": metadata,
        "body": "Hello from Lambda!",
    }
