import boto3
from botocore.exceptions import NoCredentialsError
import os
import logging

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

LOCAL_FILE = os.getenv('LOCAL_FILE')
BUCKET = os.getenv('BUCKET')
S3_FILE = os.getenv('S3_FILE')


logging.basicConfig(format='%(levelname)s %(asctime)s: %(message)s', level=logging.INFO)

logging.info(f"LOCAL_FILE {LOCAL_FILE}")
logging.info(f"BUCKET {BUCKET}")
logging.info(f"S3_FILE {S3_FILE}")


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    try:
        s3.upload_file(local_file, bucket, s3_file)
        logging.info('Upload Successful')
    except FileNotFoundError:
        logging.error(f"The file {local_file} was not found")
        raise SystemExit(1)
    except NoCredentialsError:
        logging.error('Credentials not available')
        raise SystemExit(1)


logging.info('start')
upload_to_aws(LOCAL_FILE, BUCKET, S3_FILE)
logging.info('done')
