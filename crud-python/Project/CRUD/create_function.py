import boto3
import json
import os

AWS_REGION = 'us-east-1'
AWS_PROFILE = 'localstack'
ENDPOINT_URL = 'http://localhost:4566'

boto3.setup_default_session(profile_name=AWS_PROFILE)
dynamodb_client = boto3.resource("dynamodb", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL)

def create_item(name, email):
	table_name = 'NomeDaTabela'
	item = event['body']  # Supondo que o corpo da requisição contenha os dados do item a ser criado

	table = dynamodb_client.Table(table_name)
	response = table.put_item(
		 Item={
			'Name': name,
			'Email': email
		}
	)

	return {
		'statusCode': 200,
		'body': 'Item criado com sucesso'
	}
