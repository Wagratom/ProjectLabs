# Atividade 1

### Realizar ultilizando o STK CLI

#### <br> passo 1

Não iríamos reutilizar a estrutura do projeto da atividade 1 e 2, vamos criar uma nova estrutura do zero, mas dessa vez será em C. Se anima, vai ser bom para você praticar o uso do STK CLI. <br>
Ela deverar ter a seguinte estrutura:

```
<project> -> nome do app que esta sendo criado
   ├── README.md
   ├── includes
   │   ├── <recebido pelo input>.h
   │   └── so_long.h
   ├── makefile
   ├── src
   │   └── main.c
   └── test
```

#### passo 2

Vamos criar um plugin para configurar essa estrutura criada no `passo 1`. Ja fizemos isso na atividade 1 e 2. Então vai ser facil <br>

#### main

O plugin deverar escrever uma main() que vai printar um valor recebido pelo input. <br>
E um script para executar o makefile e rodar o programa. <br>
Dica: Snippet

#### Makefile

O usuário irá escolher se quer ou não um Makefile pré-configurado. Caso ele escolha que sim, ele deverá ter as seguintes regras:

* O usuario poderar escolher se quer utilizar o gcc, g++, clang ou clang++, as flags de compilação sera passa pelo mesmo.
* O Makefile deverar compilar os objetos usando as flags passada pelo usuario
* O Makefile deverar jogar os objetos em uma pasta passada pelo usuario
* O Makefile deverar ter uma regra clean, fclean, re e all

#### Parte grafica

* Plugin deverar instalar as libs necessarias para que a minilibx possa ser utilizada
* A minilibx deverar ser instalada na pasta do projeto

#### Libft
* O usuario poderar escolher ultilizar a libft ou não.
