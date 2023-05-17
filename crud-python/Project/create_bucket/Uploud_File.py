from Create_Client import *

def upload_file(file_name, bucket_name, object_name=None):
	try:
		if object_name is None:
			object_name = os.path.basename(file_name) # retorna o nome do arquivo sem o caminho
		response = s3_client.upload_file(file_name, bucket_name, object_name)
	except ClientError:
		logger.exception('Could not upload file to S3 bucket.')
		raise
	else:
		return response

def main():
	file_name = './Create_Bucket.py'
	object_name = 'Create_Bucket.py'
	bucket_name = 'hands-on-cloud-localstack-bucket'
	logger.info('Uploading file to S3 bucket in LocalStack...')
	s3 = upload_file(file_name, bucket_name, object_name)
	logger.info('File uploaded to S3 bucket successfully.')

if __name__ == '__main__':
	main()
