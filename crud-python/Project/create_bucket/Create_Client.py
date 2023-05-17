import logging
import boto3
from botocore.exceptions import ClientError
import json
import os

AWS_REGION = 'us-east-1' # região padrão
AWS_PROFILE = 'localstack' # perfil padrão
ENDPOINT_URL = os.environ.get('LOCALSTACK_ENDPOINT_URL') # URL do localstack

# logger config
logger = logging.getLogger() # retorna um objeto logger que pode ser usado para registrar mensagens de log
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s') # configura o logger para registrar mensagens de log

boto3.setup_default_session(profile_name=AWS_PROFILE) # configura a sessão padrão do boto3
s3_client = boto3.client("s3", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL) # cria um cliente S3
s3_resource = boto3.resource("s3", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL) # cria um recurso S3

