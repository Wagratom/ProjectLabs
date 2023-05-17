from Create_Client import *

def create_bucket(bucket_name):
	try:
		response = s3_client.create_bucket( Bucket=bucket_name) # cria um bucket S3
	except ClientError:
		logger.exception('Could not create S3 bucket locally.') # registra uma mensagem de log
		raise # levanta a exceção
	else:
		return response

def main():
	bucket_name = "hands-on-cloud-localstack-bucket"
	logger.info('Creating S3 bucket locally using LocalStack...') # registra uma mensagem de log / como se fosse um titulo
	s3 = create_bucket(bucket_name) # cria um bucket S3
	logger.info('S3 bucket created.')
	logger.info(json.dumps(s3, indent=4) + '\n') # registra uma mensagem de log / exibe o conteúdo do objeto s3 em formato json

if __name__ == '__main__':
	main()
