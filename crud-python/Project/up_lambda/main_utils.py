import os
import logging
import json
from zipfile import ZipFile
import boto3

AWS_REGION = 'us-east-1'
AWS_PROFILE = 'localstack'
ENDPOINT_URL = os.environ.get('LOCALSTACK_ENDPOINT_URL')
LAMBDA_ZIP = './function.zip'

boto3.setup_default_session(profile_name=AWS_PROFILE)
# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')

def	get_boto3_client(service):
	try:
		lambda_client = boto3.client(service, region_name=AWS_REGION, endpoint_url=ENDPOINT_URL) # retorna o objeto client com o serviço passado
	except Exception as e:
		logger.exception('Error while connecting to LocalStack.')
		raise e
	else:
		return lambda_client

def	create_lambda_zip(function_name):
	try:
		with ZipFile(LAMBDA_ZIP, 'w') as zip: # LAMBDA_ZIP vai ser o nome do .zip criado
			zip.write(function_name + '.py') # Função que vai copiada para o .zip, exemplo: Create_Bucket.py ./teste/lambda.py e etc.
	except Exception as e:
		logger.exception('Error while creating ZIP file.')
		raise e

def	delete_lambda(function_name):
	try:
		lambda_client = get_boto3_client('lambda') # Pegando o objeto client com o serviço lambda
		lambda_client.delete_function(
			FunctionName=function_name # Deletando a função que acabamos de criar.
		)
		os.remove(LAMBDA_ZIP) # Deletando o arquivo .zip
	except Exception as e:
		logger.exception('Error while deleting lambda function')
		raise e

def	invoke_function(function_name):
	try:
		lambda_client = get_boto3_client('lambda')
		response = lambda_client.invoke(
			FunctionName=function_name) # Invocando a função que acabamos de criar. Para testar se ela está funcionando.
		return json.loads(
			response['Payload']
			.read()
			.decode('utf-8')
		)
	except Exception as e:
		logger.exception('Error while invoking function')
		raise e

def	create_lambda(function_name):
	try:
		lambda_client = get_boto3_client('lambda')			# retorna o objeto client com o serviço passado, no contexto lambda
		_ = create_lambda_zip(function_name)				# cria o arquivo zip
		with open(LAMBDA_ZIP, 'rb') as f:					# abre o arquivo zip para leitura e da o nome de f
			zipped_code = f.read()							# lê o arquivo zip e salva na variável zipped_code
		lambda_client.create_function(
			FunctionName=function_name,						# Nome que vai ser usado para se referir a função na AWS
			Runtime='python3.8',							# Versão do python que vai ser usada
			Role='arn:aws:iam::000000000000:role/my-role',	# Role que vai ser usada, no caso, a role default
			Handler=function_name + '.handler',				# Nome da função que vai ser executada, no caso, a função handler
			Code=dict(ZipFile=zipped_code)
		)
	except Exception as e:
		logger.exception('Error while creating function.')
		raise e

if __name__ == '__main__':
    create_lambda('../Create_Bucket')
