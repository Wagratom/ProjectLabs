from Create_Client import *

def list_buckets():
	try:
		response = s3_resource.buckets.all() # lista os buckets S3
	except ClientError:
		logger.exception('Could not list S3 bucket from LocalStack.')
		raise
	else:
		return response

def main():
	logger.info('Listing S3 buckets from LocalStack...') # registra uma mensagem de log / como se fosse um titulo
	s3 = list_buckets() # Pega a lista de buckets
	logger.info('S3 bucket names: ')
	for bucket in s3:
		logger.info(bucket.name)

if __name__ == '__main__':
	main()
