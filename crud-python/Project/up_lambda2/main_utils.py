import glob
import os
import logging
import json
from zipfile import ZipFile
import boto3

AWS_REGION = 'us-east-1'
AWS_PROFILE = 'localstack'
LAMBDA_ZIP = './function.zip'
LOCALSTACK_ENDPOINT_URL = os.environ.get('LOCALSTACK_ENDPOINT_URL', 'http://localhost:4566')

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
					format='%(asctime)s: %(levelname)s: %(message)s')

boto3.setup_default_session(profile_name=AWS_PROFILE)

def get_boto3_client(service):
	try:
		return boto3.client(
			service,
			region_name=AWS_REGION,
			endpoint_url=LOCALSTACK_ENDPOINT_URL
		)
	except Exception as e:
		logger.exception('Error while connecting to LocalStack.')
		raise e
	else:
		return client

def get_boto3_resource(service):
	try:
		return boto3.resource(
			service,
			region_name=AWS_REGION,
			endpoint_url=LOCALSTACK_ENDPOINT_URL
		)
	except Exception as e:
		logger.exception('Error while connecting to LocalStack.')
		raise e
	else:
		return resource

def create_lambda_zip(function_name):
	try:
		with ZipFile(LAMBDA_ZIP, 'w') as zip:
			py_files = glob.glob('*.py')
			for f in py_files:
				zip.write(f)
	except Exception as e:
		logger.exception('Error while creating ZIP file.')
		raise e

def create_lambda(function_name, **kw_args):
	try:
		lambda_client = get_boto3_client('lambda')
		_ = create_lambda_zip(function_name)
		# create zip file for lambda function.
		with open(LAMBDA_ZIP, 'rb') as f:
			zipped_code = f.read()
		lambda_client.create_function(
			FunctionName=function_name,
			Runtime='python3.8',
			Role='arn:aws:iam::000000000000:role/my-role',
			Handler=function_name + '.handler',
			Code=dict(ZipFile=zipped_code),
			**kw_args
		)
	except Exception as e:
		logger.exception('Error while creating function.')
		raise e

def delete_lambda(function_name):
	try:
		lambda_client = get_boto3_client('lambda')
		lambda_client.delete_function(
			FunctionName=function_name
		)
		# remove the lambda function zip file
		os.remove(LAMBDA_ZIP)
	except Exception as e:
		logger.exception('Error while deleting lambda function')
		raise e

def invoke_function(function_name):
	try:
		lambda_client = get_boto3_client('lambda')
		response = lambda_client.invoke(
			FunctionName=function_name)
		return (response['Payload']
				.read()
				.decode('utf-8')
				)
	except Exception as e:
		logger.exception('Error while invoking function')
		raise e

def create_bucket(bucket_name):
	try:
		s3_client = get_boto3_client('s3')
		s3_client.create_bucket(
			Bucket=bucket_name
		)
	except Exception as e:
		logger.exception('Error while creating s3 bucket')
		raise e

def s3_upload_file(bucket_name, object_name, content):
	try:
		s3_client = get_boto3_client('s3')
		s3_client.put_object(
			Bucket=bucket_name,
			Key=object_name,
			Body=content
		)
	except Exception as e:
		logger.exception('Error while uploading s3 object')
		raise e

def list_s3_bucket_objects(bucket_name):
	try:
		s3_resource = get_boto3_resource('s3')
		return [
			obj.key for obj in s3_resource.Bucket(bucket_name).objects.all()
		]
	except Exception as e:
		logger.exception('Error while listing s3 bucket objects')
		raise e

def delete_bucket(bucket_name):
	try:
		s3_resource = get_boto3_resource('s3')
		# empty the bucket before deleting
		s3_resource.Bucket(bucket_name).objects.all().delete()
		s3_resource.Bucket(bucket_name).delete()
	except Exception as e:
		logger.exception('Error while deleting s3 bucket')
		raise e
