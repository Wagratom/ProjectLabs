import boto3

dynamodb = boto3.resource('dynamodb')

def update_item(event, context):
	table_name = 'NomeDaTabela'
	key = event['queryStringParameters']['key']  
	update_expression = event['body']['update_expression']
	expression_attribute_values = event['body']['expression_attribute_values']

	table = dynamodb.Table(table_name)
	response = table.update_item(
		Key=key,
		UpdateExpression=update_expression,
		ExpressionAttributeValues=expression_attribute_values
	)

	return {
		'statusCode': 200,
		'body': 'Item atualizado com sucesso'
	}

