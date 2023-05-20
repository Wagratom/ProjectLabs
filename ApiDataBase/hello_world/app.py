import json
import boto3

################################################################################
# 						Funções auxiliares
################################################################################
def return_bad_request(message):
	if message:
		return {
			'statusCode': 400,
			'body': message
		}
	else:
		return {
			'statusCode': 400,
			'body': "Bad Request: Algum parâmetro está faltando. ou está incorreto."
		}

def get_extra_paraments(event):
	extras = {}
	body = json.loads(event['body'])
	for key, value in body.items():
		if key not in ['TableName', 'Id', 'Name']:
			extras[key] = value
	return extras

def get_parameters(event):
	try:
		body = json.loads(event['body'])
		table = body['TableName']
		id = body['Id']
		name = body['Name']
		extras = get_extra_paraments(event)
		return table, id, name, extras
	except:
		table = event['queryStringParameters']['TableName']
		id = event['queryStringParameters']['Id']
		name = event['queryStringParameters']['Name']
		return table, id, name, {}

################################################################################
# 						handler methods
################################################################################

def handle_get(event):
	table, id, name, extra = get_parameters(event)
	item = get_item(table, id, name)
	return {
		'statusCode': 200,
		'body': json.dumps(item)
	}

def handle_post(event):
	table, id, name, extras = get_parameters(event)
	status = add_item(table, id, name, extras)
	return {
		'statusCode': 200,
		'body': status
	}

def handle_delete(event):
	table, id, name, extras = get_parameters(event)
	delete_item_table(table, id, name)
	return {
		'statusCode': 200,
		'body': f'Item {id} deletado com sucesso!'
	}

def handle_put(event):
	table, id, name, extras = get_parameters(event)
	status = update_item_table(table, id, name, extras)
	return {
		'statusCode': 200,
		'body': status
	}

def	lambda_handler(event, context):
	try:
		print('\n\n')
		if (event['httpMethod'] == 'GET'):
			return handle_get(event)
		elif (event['httpMethod'] == 'POST'):
			return handle_post(event)
		elif (event['httpMethod'] == 'DELETE'):
			return handle_delete(event)
		elif (event['httpMethod'] == 'PUT'):
			return handle_put(event)
	except Exception as e:
		return return_bad_request(str(e))

def	get_table(table):
	dynamodb = boto3.resource('dynamodb', endpoint_url='http://host.docker.internal:4566')
	table = dynamodb.Table(table)
	return table

def	get_item(table, id, name):
	item = get_table(table).get_item(
		Key={
			'Id': id,
			'Name': name,
		}
	)
	return item['Item']

def add_item(table, id, name, extras):
	try:
		get_item(table, id, name)	# se não der erro, o item já existe
		return f'Item "Id": "{id}" "Name": "{name}" já existe!'
	except: 						# se der erro, o item não existe e pode ser adicionado
		get_table(table).put_item(
			Item={
				'Id': id,
				'Name': name,
				**extras
			}
		)
		return f'Item "Id": "{id}" "Name": "{name}" adicionado com sucesso!'

def delete_item_table(table, id, key):
	response = get_table(table).delete_item(
		Key={
			'Id': id,
			'Name': key,
		}
	)

def generate_update_expression_and_values(extras): # extras = {"Anime": "Luffy king of pirates", "Manga": "One Piece"}
	update_expression_parts = []
	expression_attribute_values = {}

	for key, value in extras.items():
		placeholder = f':{key}'  # exemplo: :Anime, :Manga
		update_expression_parts.append(f'{key} = {placeholder}') # exemplo: [Anime = :Anime | Manga = :Manga]
		expression_attribute_values[placeholder] = value # exemplo: {"":Anime": "Luffy king of pirates" | ":Manga:" "One Piece"}
	update_expression = 'SET ' + ', '.join(update_expression_parts) # exemplo: SET Anime = :Anime, Manga = :Manga
	return update_expression, expression_attribute_values

def	update_item_table(table, id, name, extras):
	try:
		get_item(table, id, name)
		update_expression, expression_attribute_values = generate_update_expression_and_values(extras)
		get_table(table).update_item(
			Key={
				'Id': id,
				'Name': name,
			},
			UpdateExpression=update_expression,
			ExpressionAttributeValues=expression_attribute_values
		)
		return (f'Item "Id": "{id}" "Name": "{name}" atualizado com sucesso!')
	except:
		return (f'Item "Id": "{id}" "Name": "{name}" não existe!')

	# get_table(table).update_item(
	# 	Key={
	# 		'Id': id,
	# 		'Name': name,
	# 	},
	# 	UpdateExpression='SET Anime = :val1',
	# 	ExpressionAttributeValues={
	# 		':val1': 'Luffy king of pirates',
	# 	}
	# )

# {
#     "TableName":"wallas",
#     "Id":"1",
#     "Name":"lucas",
#     "Animes":"LuffyRebaixado|GonBersek|SaitamaCareca",
#     "NewAnime":"Mashle|Demon|Dr.Pedra|JJtsuu"
# }
