import json
import logging
import os
import boto3
from botocore.exceptions import ClientError
AWS_REGION = 'us-east-1'
AWS_PROFILE = 'localstack'
ENDPOINT_URL = os.environ.get('LOCALSTACK_ENDPOINT_URL')
# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')
boto3.setup_default_session(profile_name=AWS_PROFILE)
dynamodb_resource = boto3.resource("dynamodb", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL)

def update_dynamodb_table_item(table_name, name, email, phone_number):
	try:
		table = dynamodb_resource.Table(table_name)
		response = table.update_item(
			Key={
				'Name': name,
				'Email': email
			},
			UpdateExpression="set phone_number=:ph",
			ExpressionAttributeValues={
				':ph': phone_number
			}
		)
	except ClientError:
		logger.exception('Could not update the item.')
		raise
	else:
		return response

def main():
	table_name = 'hands-on-cloud-dynamodb-table'
	name = 'hands-on-cloud'
	email = 'example@cloud.com'
	phone_number = '123-456-1234'
	logger.info('updateing item...')
	dynamodb = update_dynamodb_table_item(
		table_name, name, email, phone_number)
	logger.info(
		f'Item details: {json.dumps(dynamodb, indent=4)}')

if __name__ == '__main__':
	main()
