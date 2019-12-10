from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class PhotoStorage(S3Boto3Storage):
    location = '/'
    default_acl = 'public-read'
    file_overwrite = True
    
