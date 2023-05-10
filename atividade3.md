# Atividade 1

### Realizar ultilizando o STK CLI

### <br> `passo 1`
<br>

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

Agora vamos para o `passo 2`

Vamos criar um plugin para configurar essa estrutura criada no `passo 1`. Ja fizemos isso na atividade 1 e 2. Então vai ser facil <br>

`main`

O plugin deverar escrever uma main() que vai printar um valor recebido pelo input.

Dica: Snippet

	Makefile

O usuario ira escolher se que ou não um Makefile pre configurado, caso ele escolha que sim, ele deverar ter as seguintes regras:

O makefile deverar ja esta pronto para compilar o projeto, ele deverar ter as seguintes regras:

* O Makefile deverar ter uma variavel cflgs que sera passada pelo input
* O Makefile deverar compilar os objetos usando as cflags e gerar um executavel com o nome do projeto
* O Makefile deverar ter uma regra clean, fclean, re e all
* Os objetos deverar ser gerados na pasta obj
