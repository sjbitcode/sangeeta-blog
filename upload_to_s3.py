import json
import os

import boto3


# Helper function to get the extension of a filename.
def get_file_ext(path):
    return path.split('.')[-1]

# Filename extension to meme-type map.
content_type = {
    'html': 'text/html',
    'css': 'text/css',
    'js': 'text/javascript',
    'json': 'application/json',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'txt': 'text/plain'
}

keys = json.load(open('keys.json'))

FILENAME = __file__
ROOT_DIR = os.path.abspath(os.path.dirname(FILENAME))
OUTPUT_DIR = os.path.join(ROOT_DIR, keys['OUTPUT_DIR_NAME'])
AWS_ACCESS_KEY_ID = keys['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = keys['AWS_SECRET_ACCESS_KEY']


s3 = boto3.resource(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)
bucket = s3.Bucket(keys['AWS_S3_BUCKET_NAME'])

# Clear bucket before uploading.
bucket.objects.all().delete()
print('Cleared bucket')

for current_dir, dirs, files in os.walk(OUTPUT_DIR):
    for file_ in files:
        # Build path of the file.
        path = os.path.join(current_dir, file_)
        # Build absolute path of the file.
        s3_path = path.replace('{}/'.format(OUTPUT_DIR), '')

        with open(path, 'rb') as data:
            # Get mime-type of file.
            try:
                ext = get_file_ext(s3_path)
                mime_type = content_type[ext]
            # Fallback to text/plain meme-type.
            except KeyError:
                mime_type = content_type['txt']

            # Upload file to bucket.
            bucket.put_object(Key=s3_path, Body=data, ContentType=mime_type)
            print('Uploaded {}: ({})'.format(s3_path, mime_type))
