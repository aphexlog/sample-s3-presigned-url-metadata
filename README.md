# S3 Presigned URL with Metadata Project

his Serverless Python project demonstrates how to extend an S3 presigned URL with metadata, which can later be retrieved during the object's lifecycle. It consists of two AWS Lambda functions:

- `get_presigned_url` - Returns a presigned URL for uploading an object to an S3 bucket.
- `get_metadata` - Returns the metadata of an object in an S3 bucket.

## Requirements

- AWS Account
- Python 3.x
- AWS CLI
- Serverless Framework

## Setup & Deployment

1. Clone the repository.
  ```bash
  git clone <repository_url>
  ```

2. Navigate to the project directory.
  ```bash
  cd s3-presigned-url-with-metadata
  ```

3. Run `sam build` to build the application.
  ```bash
  serverless deploy
  ```

## Architecture

- **AWS S3**: Storage service to host objects.
- **AWS Lambda**: Two functions for generating presigned URLs and fetching metadata.

## Limitations

- Presigned URLs are time-sensitive.
- Metadata is attached during the PUT operation and cannot be modified afterwards.

## Contributing

Feel free to contribute by submitting pull requests or by reporting issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
