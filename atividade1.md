# Atividade 1

<h3>Realizar ultilizando o STK CLI. <h3\><br><br>

`passo 1`

* Crie uma stack.
* Crie um template nessa stack.
* crie um app usando seu templete e ele deverar ter a seguind estrutura
	```
	projeto -> nome do app
	├── docs
	│   └── data.txt
	├── README.md
	├── src
	│   └── main.py
	└── tests
	```
<br> `passo 2`

* Crie um plugin para configurar o arquivo data que estra localizado na pasta docs do seu app.
O pluguin deverar deixa o file com a seguind estrutura

	```
	|"""""""""""""""""""""""""""""""""""""|
	|	42SP projects: Tools Stack Sport  |
	|									  |
	|Name: Wagraton Wallas Ferreia Santos |
	|deauty level: 5					  |
	|Age: 20							  |
	|Credit card number: 164-874-458-85	  |
	"""""""""""""""""""""""""""""""""""""""
	```

* o pluguin sera aplicado dentro do app que voce criou. Caso você acabe aplicando o pluguin
novamente ele nao pode dublicar as informacoes que ja estao no arquivo data.txt

<br> `passo 3`

* Crie um stackfile que irar chamar/criar tudo isso automaticamente.
