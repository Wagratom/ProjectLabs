import boto3
import json
import os
from botocore.exceptions import ClientError

AWS_REGION = 'us-east-1'
AWS_PROFILE = 'localstack'
ENDPOINT_URL = 'http://localhost:4566'

boto3.setup_default_session(profile_name=AWS_PROFILE)
dynamodb_resource = boto3.resource("dynamodb", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL)
dynamodb_client = boto3.client("dynamodb", region_name=AWS_REGION, endpoint_url=	)

def main(event, context):
	metodo 		= event.get('httpMethod')
	table_name	= event.get('queryStringParameters').get('table_name')
	return {
		'statusCode': 200,
		"body" : json.dumps({
			'metodo': metodo,
			'table_name': table_name
		})
	}

	# if (metodo == 'GET'):
	# 	read_dynamodb_table_item(table_name, 'wagratom')
	# if (metodo == 'POST'):
	# 	add_dynamodb_table_item(table_name, 'wagratom')
	# if (metodo == 'PUT'):
	# 	update_item(table_name, key)
	# if (metodo == 'DELETE'):
	# 	delete_dynamodb_table_item(table_name, key)

def update_item(table_name, key):
	table = dynamodb_resource.Table(table_name)
	response = table.update_item(
		Key=key,
		UpdateExpression=update_expression,
		ExpressionAttributeValues=expression_attribute_values
	)

	return {
		'statusCode': 200,
		'body': 'Item atualizado com sucesso'
	}

def add_dynamodb_table_item(table_name, name):
	table = dynamodb_resource.Table(table_name)
	response = table.put_item(
		Item={
			'Name': name,
		}
	)
	return response

def delete_dynamodb_table_item(table_name, name):
	table = dynamodb_resource.Table(table_name)
	response = table.delete_item(
		Key={
			'Name': name,
		}
	)
	return response

def read_dynamodb_table_item(table_name, name):
	table = dynamodb_resource.Table(table_name)
	response = table.get_item(
		Key={
			'Name': name,
		}
	)
	return {
		'statusCode': 200,
		'body': response.get('Item')
	}


# aws lambda create-function \
# --function-name main \
# --runtime python3.8 \
# --handler main.main \
# --role arn:aws:iam::000000000000:role/lambda-role \
# --zip-file fileb://lambda-function.zip \
# --endpoint-url=http://localhost:4566

# awsls lambda list-functions --endpoint-url=http://localhost:4566
# awsls lambda invoke --function-name main --payload '{}' --endpoint-url=http://localhost:4566 output.json
# awslocal apigateway create-rest-api --name MyAPI --region us-east-1 --endpoint-url=http://localhost:4566
# id swagger.json

#http://localhost:4566/2ue55yl6u0/dev/my-endpoint

# awslocal apigateway create-rest-api --name MyAPI --region us-east-1 --endpoint-url=http://localhost:4566 --body 'file://swagger.json
# id 9urudngx2y

# awslocal apigateway create-rest-api --name MyAPI --region us-east-1 --endpoint-url http://localhost:4566
# id xeq738oal6

# awslocal apigateway put-rest-api --rest-api-id xeq738oal6 --mode merge --body file://swagger.json --endpoint-url http://localhost:4566

# awslocal apigateway create-deployment --rest-api-id xeq738oal6 --stage-name dev --endpoint-url http://localhost:4566
