# Não terminei ainda, mas vou terminar, prometo! 🤞
Por enquanto esta inutio

# Part1 - LocalStack Basico Do Basico

#### Comecei instalando as seguintes ferramentas: 🔧⚙️
```
instalar docker ✅
instalar localstack ✅
instalar aws sam ✅
instalar aws cli ✅
instalar terraform ✅
instalar samlocal ✅
```

#### iniciei um simples hello world 🌎
para testar a ferramenta, fizemos um simples [tutorial](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html) de hello world.

```
samlocal init -> iniciar um projeto ✅
samlocal build -> buidar um projeto ✅
samlocal deploy -> fazer um deploy ✅
```

#### Tive meu primeiro problema ❌

Não estava aparecendo o hello world no navegador, então corrigimos substituindo<br>
`.amazonaws.com/Prod/hello/` por `.localhost.localstack.cloud:4566/Prod/hello/` na url gerada pelo deploy.<br>
agora sim esta local. ✅

#### Vamos para o proximo passo, parece pouco esse inicio, mas foi bem trabalhoso: 😥
Achamos um [site](https://hands-on.cloud/introduction-to-boto3-library/#what-is-the-boto3-library) que ensina a fazer um CRUD em python com localstack. Vamos tentar replicar esse site, lest Bora! 🏃

# Part 2 - Crtl C + Crtl V do site

## Passo 1 - Configurar o ambiente

#### Ele usa o boto3, então vamos instalar o boto3.

Ele configura tudo em um ambiente Python virtual. Irei instalar o boto3 globalmente, então utilizei o comando:
```
pip install --upgrade pip boto3 ✅
```

#### Agora vamos configurar algumas coisas

Primeiramente, salvei o endpoint do LocalStack em uma variável usando o comando <br>
```
export LOCALSTACK_ENDPOINT_URL=http://localhost:4566 ✅
```
Em seguida, configurei o perfil do LocalStack utilizando o comando <br>
```
aws configure --profile localstack ✅
```
Também configurei o aws, so por garantia usei o mesmos dados do localstack
```
aws configure ✅
```
Vamos usar o`aws --endpoint-url=$LOCALSTACK_ENDPOINT_URL` já que é necessário apontar as chamadas de API da AWS CLI para as implantações locais do LocalStack em vez da infraestrutura da Nuvem AWS. <br>
Para nao ficar usando esse "mostro", vamos criar um alias
```
alias awsls="aws --endpoint-url=$LOCALSTACK_ENDPOINT_URL" ✅
```
agora podemos chama-los apenas usando `awsls`<br>

#### Vamos testar?
Usaremos o alias criado acima `awsls`.<br>
Criaremos um bucket com os commandos abaixo, qualquer um dos 2 comandos cria um bucket no S3.
```
awsls s3 mb s3://<nome_do_bucket> ✅
awsls s3api create-bucket --bucket <nome_do_bucket> ✅
```
Para ver a lista do buckets criados, usamos o comando
```
awsls s3 ls ✅
```
Funcionou? Se não, você pode enviar uma mensagem para o meu [assistente](https://chat.openai.com/) pessoal e ele te responderá ✅

## passo 2, Criar um Bucket no S3 usanod AWS CLI e AWS CDK

#### Vou focar apenas nas partes que considero mais importantes

O codigo completo esta no diretorio `crud-python`, mas vou explicar as partes que considero mais importantes aqui: <br>
Escrevendo aqui, percebi que é bem simples, basta focar nas partes importantes e ignorar o resto. <br>

Vamos importar as bibliotecas necessárias para o código funcionar: <br>
```
import logging
import boto3
from botocore.exceptions import ClientError
import json
import os
```

A biblioteca `logging` é utilizada para registrar mensagens de log durante a execução de um programa, sendo útil para fins de depuração. <br>
A biblioteca `boto3` é o SDK da AWS (Amazon Web Services). <br>
A exceção `ClientError` é utilizada para capturar exceções específicas que podem ocorrer ao interagir com os serviços da AWS. <br>
A biblioteca `json` é utilizada para trabalhar com dados em formato JSON. <br>
A biblioteca `os` é utilizada para realizar operações relacionadas ao sistema operacional. <br>

Note que nos exemplos a seguir, utilizaremos principalmente o `boto3`, as demais bibliotecas são utilizadas principalmente para tratamento de erros e registros de log no código em si. <br>

#### Criando um cliente do S3 usando boto3

Ultizaremos a função `boto3.client` para criar um cliente do S3. <br>
```
AWS_REGION = 'us-east-1' # região padrão
AWS_PROFILE = 'localstack' # perfil padrão
ENDPOINT_URL = os.environ.get('LOCALSTACK_ENDPOINT_URL') # URL do localstack

s3_client = boto3.client("s3", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL)

```
"s3" é o nome do serviço que queremos criar um cliente. Tem diversos serviçoes disponiveis <br>
region_name é a região que queremos criar o cliente. <br>
endpoint_url é a URL do localstack. <br>

Usaremos esse client para seguir os proximos passos. lembre-se do seu nome `s3_client`<br>

#### Criando um bucket no S3 usando boto3

Chamamos a função `create_bucket` para criar um bucket no S3. <br>

```
response = s3_client.create_bucket(Bucket=BUCKET_NAME)
```
Lembrando que o `BUCKET_NAME` é uma variavel que contem o nome do bucket que queremos criar. <br>

Via linha de commando
```
awsls s3 mb s3://hands-on-cloud-localstack-bucket
ou
awsls s3api create-bucket --bucket hands-on-cloud-localstack-bucket
```
A diferença deles são semelhantes as diferenças do client e resource, irei sita-los mais a baixa <br>

#### Vamos lista os buckets criados

Observem que utilizamos o boto3.client para criar um cliente S3 anteriormente, e agora estamos usando o boto3.resource para criar um recurso do S3. Recomendo verificar a diferença entre eles no final do [arquivo](#client_vs_resource). Nesse cenário, o resource é melhor. <br>

Vamos usar o método `buckets.all()` do resource, que retorna um objeto iterador contendo todos os nomes de buckets do S3.
```
s3_resource = boto3.resource("s3", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL)

s3 = s3_resource.buckets.all()
for bucket in s3:
	logger.info(bucket.name)
```
Observem que ele recebe os mesmos parâmetros da função `boto3.client`. <br>

Relembrando: <br>
"s3" é o nome do serviço para o qual queremos criar um cliente. Existem vários serviços disponíveis. <br>
region_name é a região para a qual queremos criar o cliente. <br>
endpoint_url é a URL do LocalStack. <br>

Via linha de commando
```
awsls s3 ls
```

#### Vamos fazer upload um arquivo no bucket

Vamos usar a função `upload_file` do cliente S3 para fazer upload de um arquivo no bucket. <br>
```
response = s3_client.upload_file(file_name, bucket_name, object_name)
```
Filename é o nome do arquivo que queremos fazer upload. <br>
Bucket_name é o nome do bucket que queremos fazer upload. <br>
Object_name é o nome do objeto que queremos fazer upload. <br>

Supondo: se você carregou o arquivo `Luffy` no S3 com o nome de Object_name `Rei_dos_Piratas`, ao buscar o arquivo no S3, você precisará especificar o nome do Object_name como `Rei_dos_Piratas`.

Via linha de command
```
aws s3 cp Luffy.txt s3://meu-bucket/ # exemplo

aws s3 cp Luffy.txt s3://meu-bucket/Rei_dos_Piratas.txt #rename
```

Para verificar se o arquivo foi upado com sucesso
```
awsls s3 ls s3://meu-bucket
```

#### Vamos fazer download do arquivo

Vamos usar a função `download_file` do cliente S3 para fazer download de um arquivo no bucket. <br>
```
Bucket(bucket_name).download_file(object_name, save_path)
```
Bucket_name é o nome do bucket que queremos fazer download. <br>
Object_name é o nome do objeto que queremos fazer download. <br>
save_path é o caminho onde o arquivo será salvo. <br>

Via linha de command
```
aws s3 cp s3://meu-bucket/Luffy.txt caminho_local/ # exemplo

aws s3 cp s3://meu-bucket/Luffy.txt caminho_local/Rei_dos_Piratas.txt # renomeando
```

#### Vamos deletar o bucket

Vamos usar a função mais de uma função, então vamos la
```
bucket = s3_resource.Bucket(bucket_name) # retorna o objeto bucket
response = bucket.objects.all().delete() # deletando todos os objetos do bucket
```
Agora vamos deletar o bucket
```
response = s3_client.delete_bucket(Bucket=bucket_name)
```
Via linha de command
```
awsls s3 rm s3://meu-bucket/luffy.txt # deletando o arquivo

awsls s3 rb s3://meu-bucket # deletando o bucket, certifique-se que o bucket esteja vazio
```
Se o bucket não estiver vazio, você receberá um erro.<br>
Você pode usar o comando aws s3 rm em combinação com a opção --recursive para excluir todos os objetos dentro do bucket de forma recursiva:
```
awsls s3 rm s3://meu-bucket --recursive
```

## passo 3 - Criando uma função lambda

#### pytest
Ele usa o pytest para testar a função lambda, então vamos baixar <br>
```
pip install pytest
```

#### Criando a função lambda
```
import logging
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def handler(event, context):
	logging.info('Hands-on-cloud')
	return {
		"message": "Hello User!"
	}
```
Event: <br>
O parâmetro event contém informações sobre o evento que acionou a função. O formato e o conteúdo específicos do evento dependem do serviço em que a função está sendo executada.Por exemplo, em serviços como API Gateway ou S3, o evento pode conter detalhes sobre a solicitação HTTP ou a ação do objeto S3 que acionou a função.<br>

context: <br>
O parâmetro context contém informações de contexto e configurações relacionadas à execução da função. <br>
Alguns dos atributos presentes no objeto context são:<br>
* context.aws_request_id: O ID exclusivo da solicitação atual.
* context.function_name: O nome da função lambda.
* context.function_version: A versão da função lambda.
* context.invoked_function_arn: O ARN (Amazon Resource Name) da função lambda.
* context.memory_limit_in_mb: O limite de memória configurado para a função lambda.
* context.log_group_name: O nome do grupo de logs do CloudWatch associado à função lambda.
* context.log_stream_name: O nome do stream de logs do CloudWatch associado à função lambda.
* context.get_remaining_time_in_millis(): Método para obter o tempo restante de execução antes de a função ser encerrada.

### Criando uma main
Uma função para zipar o arquivo da função lambda, para que possamos fazer o upload para o AWS Lambda. <br>
```
def	create_lambda_zip(function_name):
	try:
		with ZipFile(LAMBDA_ZIP, 'w') as zip:
			zip.write(function_name + '.py')
	except Exception as e:
		logger.exception('Error while creating ZIP file.')
		raise e
```
O parâmetro LAMBDA_ZIP é o caminho e nome do arquivo ZIP que será gerado. <br>
O parâmetro function_name é o nome do arquivo que serar zipado. <br>

Deixei o codigo todo comendado, para que você possa entender melhor o que cada função faz. <br>
Não vou anotar tudo aqui porque ficaria muito grande, então vou olhem o main_utils.py <br>

### Testando A Função Do AWS Lambda Interagindo Com O S3


# ENDD
# end














### client_vs_resource

O boto3.client fornece uma interface de nível mais baixo e direta para interagir com os serviços da AWS. Ele permite que você faça chamadas de API específicas do serviço, fornecendo métodos para executar ações específicas. Com o cliente, você tem mais controle sobre as chamadas de API e pode acessar recursos específicos do serviço que podem não estar disponíveis no nível de recurso.

Por outro lado, o boto3.resource fornece uma interface de nível mais alto e orientada a objetos para interagir com os serviços da AWS. Ele encapsula o cliente subjacente e fornece métodos e atributos convenientes para realizar operações comuns. Com o recurso, você pode manipular objetos e recursos da AWS de forma mais semelhante a objetos nativos do Python, o que torna o código mais intuitivo e legível.

Em resumo, se você precisa de um controle mais granular sobre as chamadas de API e precisa acessar recursos específicos do serviço, use o boto3.client. Se você deseja uma interface mais amigável e orientada a objetos para realizar operações comuns, use o boto3.resource. A escolha entre eles depende do nível de controle e da conveniência que você deseja em suas interações com os serviços da AWS.

### create-bucket
Ambos os comandos podem ser usados para criar um bucket no LocalStack usando a AWS CLI. A escolha entre eles depende das suas necessidades e da quantidade de personalização que você deseja aplicar ao criar o bucket. Se você precisar de maior controle sobre as configurações do bucket, o uso do comando s3api create-bucket é mais adequado. Caso contrário, o comando s3 mb pode ser mais simples e direto para criar um bucket.


























sam local start-api -> iniciar o api localmente
cat ~/.aws/credentials -> printa as credencias da aws

aws --endpoint-url=$LOCALSTACK_ENDPOINT_URL s3 ls -> lista os buckets
alias awsls="aws --endpoint-url=$LOCALSTACK_ENDPOINT_URL"
awsls s3api list-objects --bucket hands-on-cloud-localstack-bucket


export LOCALSTACK_ENDPOINT_URL=http://localhost:4566
