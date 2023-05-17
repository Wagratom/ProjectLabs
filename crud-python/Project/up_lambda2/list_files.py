import glob
import os
import logging
import json
from zipfile import ZipFile
import boto3

AWS_REGION = 'us-east-1' # região padrão
AWS_PROFILE = 'localstack' # perfil padrão
ENDPOINT_URL = os.environ.get('LOCALSTACK_ENDPOINT_URL') # URL do localstack

def	create_e_print_bucket(bucket_name):
	s3_client = boto3.client("s3", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL) # cria um cliente S3
	s3_client.create_bucket(Bucket=bucket_name)
	s3_client.upload_file('lambda.py', bucket_name, 'lambda.py')
	s3_client.upload_file('main_utils.py', bucket_name, 'main_utils.py')
	s3_resource = boto3.resource("s3", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL)
	bucket = s3_resource.Bucket(bucket_name)
	for obj in bucket.objects.all():
		print(obj.key, obj.last_modified)

if __name__ == '__main__':
	create_e_print_bucket('hands-on-cloud-bucket')

