import boto3

dynamodb = boto3.resource('dynamodb')

def get_item(event, context):
	table_name = 'NomeDaTabela'
	key = event['queryStringParameters']['key']  # Supondo que o parâmetro 'key' seja passado na URL da requisição

	table = dynamodb.Table(table_name)
	response = table.get_item(Key=key)
	item = response.get('Item')

	return {
		'statusCode': 200,
		'body': item
	}
