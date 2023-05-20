import boto3

dynamodb = boto3.resource('dynamodb')

def delete_item(event, context):
	table_name = 'NomeDaTabela'
	key = event['queryStringParameters']['key']  # Supondo que o parâmetro 'key' seja passado na URL da requisição

	table = dynamodb.Table(table_name)
	response = table.delete_item(Key=key)

	return {
		'statusCode': 200,
		'body': 'Item excluído com sucesso'
	}
