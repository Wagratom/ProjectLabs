from Create_Client import *

def download_file(save_path, bucket_name, object_name):
	try:
		response = s3_resource.Bucket(bucket_name).download_file(object_name, save_path) # baixa o arquivo do bucket
	except ClientError:
		logger.exception('Could not download file to S3 bucket.')
		raise
	else:
		return response

def main():
	path = './Downloads_s3/Create_Bucket.py' # caminho onde o arquivo será salvo
	object_name = 'Create_Bucket.py' # nome do arquivo no bucket
	bucket_name = 'hands-on-cloud-localstack-bucket' # nome do bucket
	logger.info('Downloading file to S3 bucket in LocalStack...')
	s3 = download_file(path, bucket_name, object_name) # baixa o arquivo do bucket
	logger.info('File downloaded from S3 bucket successfully.')

if __name__ == '__main__':
	main()

