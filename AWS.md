# AWS

AWS significa Amazon Web Services e é a plataforma de computação em nuvem oferecida pela Amazon. A AWS oferece uma ampla gama de serviços em nuvem, incluindo armazenamento, banco de dados, análise, computação, redes, machine learning e muito mais. Esses serviços são disponibilizados aos usuários por meio de diferentes modelos de entrega, incluindo Infraestrutura como Serviço
[IaaS](https://cloud.google.com/learn/what-is-iaas?hl=pt-br) Plataforma como Serviço [PaaS](https://cloud.google.com/learn/what-is-paas?hl=pt-br) e Software como Serviço [SaaS](https://www.salesforce.com/br/saas/). A AWS é considerada uma das principais provedoras de serviços em nuvem do mundo e é amplamente utilizada por empresas de todos os tamanhos.

![Hierarquia Iaas PaaS Iaas](./.github/images/SaaS_PaaS_Iaas.png)

### AWS CLI

A AWS CLI (Command Line Interface) é uma interface de linha de comando para a AWS (Amazon Web Services) que permite que você gerencie seus recursos da AWS usando comandos em vez de clicar em menus em um console. A AWS CLI está disponível para Windows, macOS e Linux, e é instalada através do pacote de instalação do Python pip.

A AWS CLI fornece acesso direto às APIs públicas dos serviços da AWS. Você pode explorar as capacidades de um serviço com a AWS CLI e desenvolver scripts de shell para gerenciar seus recursos. Além dos comandos de baixo nível equivalentes à API, vários serviços da AWS fornecem personalizações para a AWS CLI. As personalizações podem incluir comandos de nível superior que simplificam o uso de um serviço com uma API complexa."

### AWS SAM

O  AWS SAM (Serverless Application Model) é um modelo open source que permite que você desenvolva, testa e implante aplicativos serverless na AWS. O AWS SAM é baseado no AWS CloudFormation.

Com o AWS SAM, você pode definir suas funções serverless, APIs REST, eventos e recursos de infraestrutura usando um único arquivo de template YAML ou JSON. O modelo SAM também inclui convenções de nomenclatura e estrutura de diretórios que ajudam a organizar e gerenciar seus recursos de aplicativo serverless de maneira mais eficiente.

Ao usar o AWS SAM, você pode implantar rapidamente seus aplicativos serverless na AWS, sem se preocupar com a infraestrutura subjacente. O AWS SAM também inclui um conjunto de ferramentas de linha de comando para ajudar a criar, testar e depurar seus aplicativos serverless localmente.

O AWS SAM é compatível com várias linguagens de programação, como Node.js, Python, Java, Ruby e Go, entre outras.

### AWS CloudFormation

O AWS CloudFormation é um serviço de infraestrutura como código que permite criar, gerenciar e provisionar recursos de infraestrutura na AWS de maneira automatizada e consistente. Com o CloudFormation, você pode definir sua infraestrutura como código em um arquivo JSON ou YAML e usar esse modelo para criar e provisionar recursos na AWS de maneira repetível e escalável.

Em certo sentido, o AWS CloudFormation pode ser comparado com um Dockerfile, pois ambos são ferramentas de infraestrutura como código que permitem definir e gerenciar recursos de infraestrutura de maneira automatizada e repetível.

### aplicativos serverless

Aplicativos serverless são aplicativos que são executados em plataformas de computação sem [servidor](#adicionais1), como o AWS Lambda, o Azure Functions e o Google Cloud Functions. Essas plataformas permitem que os desenvolvedores escrevam código de aplicativo sem se preocupar com a infraestrutura subjacente, como servidores, redes e balanceadores de carga.

Ao contrário dos aplicativos tradicionais que são implantados em servidores, os aplicativos serverless são executados em um ambiente altamente escalável e elástico. Isso significa que a plataforma de computação sem servidor provisiona automaticamente os recursos necessários para executar o código, e escala automaticamente para lidar com picos de tráfego. Quando não há tráfego, os recursos são liberados e o aplicativo não consome recursos desnecessários.

Os aplicativos serverless têm muitas vantagens em relação aos aplicativos tradicionais, como redução de custos, facilidade de escalabilidade, tempo de desenvolvimento mais rápido e menor sobrecarga operacional. No entanto, eles também têm algumas desvantagens, como restrições de tempo de execução e limitações de recursos, o que pode limitar a complexidade dos aplicativos.


# Dados complementares

### adicionais1

Em uma plataforma sem servidor, o usuário não precisa se preocupar com a infraestrutura subjacente, como a configuração de servidores, redes, balanceadores de carga, etc. Em vez disso, ele apenas escreve o código do aplicativo e define como ele deve ser executado em resposta a determinados eventos, como uma solicitação HTTP, uma mensagem em uma fila, uma alteração em um banco de dados, etc. Mas tem um servidor viu gente 😵. O servidor está lá, mas é gerenciado pela plataforma de computação sem servidor. O usuário não precisa se preocupar com isso.



