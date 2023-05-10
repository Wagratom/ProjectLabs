# Stackspot e STK CLI

## [Stackspot](https://docs.stackspot.com/docs/getting-started/how-it-works/)
Stackspot é uma ferramenta de automação que permite preparar ambientes para desenvolvimento ou produção,
integrando diferentes ferramentas e serviços em um único lugar. Com Stackspot, você pode configurar,
gerenciar e orquestrar infraestrutura em nuvem, como máquinas virtuais, bancos de dados, balanceadores de carga,
entre outros.

## [Template](https://docs.stackspot.com/docs/use-stacks/user-tutorials/create-project/)
Template é um modelo que define a configuração de um ambiente, geralmente usado para configurar a infraestrutura de forma padronizada e automatizada.
No contexto do Stackspot, um template pode conter scripts de instalação, configurações de rede,
definições de segurança e outras configurações que permitam preparar o ambiente de forma rápida e consistente.

## [Plugin](https://docs.stackspot.com/docs/use-stacks/user-tutorials/apply-plugin/)
Plugin é um componente que pode ser adicionado a um ambiente para adicionar funcionalidades específicas.
No contexto do Stackspot, os plugins podem ser adicionados ao ambiente para estender as funcionalidades do Stack.

## [Stackfiles](https://docs.stackspot.com/docs/use-stacks/user-tutorials/use-stackfile/)
Stackfiles são arquivos YAML que definem o ambiente completo, incluindo a configuração do template,
plugins e outras configurações. Com Stackfiles, é possível versionar e compartilhar a configuração do ambiente.

## [Stack](https://docs.stackspot.com/docs/create-stacks/quickstart/)
Stack é o ambiente criado a partir da configuração de Plugins, Templates, e Stackfiles que, quando usados em conjunto. Ele pode ser uma máquina virtual,
um contêiner Docker ou qualquer outro tipo de ambiente que possa ser gerenciado pelo Stackspot.

## STK CLI
O STK CLI é a ferramenta de interface de linha de comando da StackSpot. É o principal canal que permite você usar e criar Stacks, além de acessar as demais funcionalidades da plataforma. O STK CLI garante simplicidade e velocidade ao usar a StackSpot. Pelo STK CLI você pode executar comandos para criar e usar:

[Stacks](#stackspot)<br>
[Templates](#template)<br>
[Plugins](#plugin)<br>
[App](#stack)<br>
[Basic commands](https://gist.github.com/wwwwelton/ec2d8b41333d105752859200a541be7b)

# Atividades

Aqui esta algumas atividades para você praticar o uso do STK CLI. Você pode executar as atividades em qualquer ordem, mas recomendamos que você siga a ordem sugerida.</br>

## Vamos Configurar alguns arquivos? lest bora!

A atividade 1 e 2 envolvem a criação de um ambiente com diretorios especificos e a criação de um plugin para configurar um arquivo de texto com informações capturadas do usuario.<br>
Pontos Fortes: Pode ser usado para automatizar a criação de estruturas de ambientes e a configuração de arquivos pré existentes.<br>
Foco: `Hooks do tipo edit` -> `search` `insert` `condicion` `snippet` `when` e etc.

## Estrutura cub3d pronta? Como assim não tem? Então bora criar!

Vai me dizer que você nunca estressou tentando baixar e configurar a minilibx?
Ou que nunca teve que ficar configurando o Makefile para compilar o cub3d e joga os objetos em uma pasta especifica?
Então essa atividade é para você!<br>

Pontos fortes: Pode ser usado para automatizar a criação de estruturas de ambientes e a configuração de arquivos pré-existentes. Peraí, você já fez isso, né? Se não, volte umas atividades. Se sim, vamos complementar configurando o ambiente de forma geral, com dependências, bibliotecas e configurações de arquivos. Lest bora de atividade 3 e 4!<br>
