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

* Crie um plugin para configurar o arquivo data que esta localizado na pasta docs do seu app.
O pluguin deverar deixa o data.txt com a seguinte estrutura.
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

* Os dados são recebidos na hora pelo plugin. Poder ser por default ou por input do usuario.
* O usuario pode decidir se quer adicionar o prefix "42SP projects: " antes do nome do projeto.
* o pluguin sera aplicado dentro do app que voce criou. Caso você acabe aplicando o pluguin
mais de uma vez ele nao pode dublicar as informacoes que ja estao no arquivo data.txt
(not relink, estilo 42 XD)

<br> `passo 3`

* Crie um stackfile que irar chamar/criar tudo isso automaticamente.
