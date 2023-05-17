from Create_Client import *

def empty_bucket(bucket_name):
	try:
		logger.info('Deleting all objects in the bucket...')
		bucket = s3_resource.Bucket(bucket_name) # retorna o objeto bucket
		response = bucket.objects.all().delete()
	except:
		logger.exception('Could not delete all S3 bucket objects.')
		raise
	else:
		return response

def delete_bucket(bucket_name):
	try:
		empty_bucket(bucket_name)
		response = s3_client.delete_bucket(Bucket=bucket_name)
	except ClientError:
		logger.exception('Could not delete S3 bucket locally.')
		raise
	else:
		return response

def main():
	bucket_name = "hands-on-cloud-localstack-bucket"
	logger.info('Deleting S3 bucket...')
	s3 = delete_bucket(bucket_name)
	logger.info('S3 bucket deleted.')
	logger.info(json.dumps(s3, indent=4) + '\n')

if __name__ == '__main__':
	main()

