# Laboratório 2: Creating a VPC and Launching a Web Application in an Amazon EC2 Instance

© 2025 Amazon Web Services, Inc. ou suas afiliadas. Todos os direitos reservados. Este trabalho não pode ser reproduzido ou redistribuído, no todo ou em parte, sem a permissão prévia por escrito da Amazon Web Services, Inc. Todas as marcas comerciais pertencem a seus proprietários.

> **Observação:** não inclua nenhuma informação pessoal, de identificação ou confidencial no ambiente do laboratório. As informações inseridas podem estar visíveis para outras pessoas.

Correções, feedback ou outras dúvidas? Entre em contato com **AWS Training and Certification**.

---

## Visão geral do laboratório

Neste cenário, você criará a arquitetura de rede subjacente necessária para executar uma aplicação web em uma instância do Amazon EC2. Depois de criar a rede, você iniciará a instância do EC2 usada para hospedar sua aplicação web e realizará um teste simples para verificar se é possível acessá-la usando um navegador da web.

---

## Objetivos

Ao final deste laboratório, você deverá ser capaz de:

- Criar uma Amazon VPC com duas sub-redes públicas.
- Criar um gateway da internet.
- Criar uma tabela de rotas com uma rota pública para a internet.
- Criar um grupo de segurança.
- Iniciar uma instância do Amazon Elastic Compute Cloud (Amazon EC2).
- Configurar uma instância do EC2 para hospedar uma aplicação web usando um script de dados do usuário.

---

## Pré-requisitos

Este laboratório requer:

- Notebook com Wi-Fi e Microsoft Windows, macOS ou Linux (Ubuntu, SuSE ou Red Hat)
- Acesso com nível de administrador (usuários do Microsoft Windows)
- Navegador de internet, como Chrome, Firefox ou Edge

> **Observação:** não é possível acessar o ambiente do laboratório usando tablets, embora eles possam exibir os guias do aluno.

---

## Lista de ícones

- **Saída esperada:** um exemplo que você pode usar para verificar a saída de um comando ou arquivo editado.
- **Observação:** uma observação, dica ou orientação importante.
- **Atenção:** informações de interesse ou importância especial.
- **Tarefa concluída:** uma conclusão ou resumo no laboratório.

---

## Iniciar laboratório

1. Selecione **Start Lab (Iniciar laboratório)** na parte superior da página.
2. Aguarde até o fim da provisão dos serviços da AWS.
3. Para abrir o laboratório, selecione **Open Console (Abrir console)**. Você será conectado automaticamente ao AWS Management Console.

> **Não altere a Região**, a menos que instruam você a fazê-lo.

### Erros comuns de login

- **Erro:** "You must first log out before logging into a different AWS account"  
  **Solução:**  
  1. Clique no link **click here**.  
  2. Feche a guia do navegador AWS Sign In.  
  3. Volte à página inicial do laboratório e clique em **Open Console** novamente.

- **Erro:** Nada acontece ao clicar em **Start Lab**  
  **Solução:**  
  1. Desative bloqueadores de pop-up ou scripts ou adicione o domínio do laboratório à lista de permissões.  
  2. Atualize a página e tente novamente.

---

## Tarefa 1: Criar uma nuvem privada virtual

> **Observação:** use a mesma Região em todo o laboratório.

Nesta tarefa, você criará uma VPC, um gateway da internet, uma tabela de rotas pública e duas sub-redes públicas em duas Zonas de Disponibilidade (AZs) separadas.

- **VPC:** Rede virtual que permite iniciar recursos da AWS como se fosse um data center.
- **Gateway de Internet:** Permite comunicação entre sua VPC e a internet.
- **Sub-redes:** Intervalos de endereços IP em cada AZ. Usar sub-redes públicas para recursos conectados à internet.

### Tarefa 1.1: Criar VPC, sub-redes públicas, tabela de rotas e gateway da internet

1. No AWS Management Console, pesquise e escolha **VPC**.
2. Clique em **Criar VPC**.
3. Em **Configurações da VPC**, selecione **VPC e muito mais**.
4. Em **Geração automática da etiqueta de nome**, selecione **Gerar automaticamente** e insira `lab-2`.
5. Em **IPv4 CIDR block**, insira `10.0.0.0/16`.
6. Em **IPv6 CIDR block**, selecione **No IPv6 CIDR block**.
7. Locação: **Padrão**.
8. Número de Zonas de Disponibilidade (AZs): 2.
9. Sub-redes públicas: 2. Sub-redes privadas: 0.
10. Personalize blocos CIDR de sub-redes:
    - Sub-rede 1: `10.0.0.0/24`
    - Sub-rede 2: `10.0.1.0/24`
11. Gateways NAT: Nenhum. Endpoints da VPC: Nenhum.
12. Opções de DNS: **Habilitar nomes de host DNS** e **Habilitar resolução de DNS**.
13. Clique em **Criar VPC**.

> **Saída esperada:** A tela de fluxo de trabalho de VPC indica que tudo foi criado com êxito.

**Tarefa concluída:** VPC criada com sucesso, incluindo sub-redes, tabela de rotas e gateway da internet.

---

## Tarefa 2: Criar um grupo de segurança da VPC

Um grupo de segurança funciona como um firewall para controlar o tráfego de entrada e saída dos recursos.

1. No painel esquerdo, escolha **Grupos de segurança**.
2. Clique em **Criar grupo de segurança**.
3. Preencha os detalhes:
    - Nome: `Web Security Group`
    - Descrição: `Enable HTTP access from anywhere`
    - VPC: selecione a `lab-2-vpc`
4. Adicione uma regra de entrada:
    - Tipo: HTTP
    - Origem: Anywhere-IPv4
    - Destino: `Allow web requests from anywhere`
5. Tags (opcional):
    - Chave: Name
    - Valor: WebAppSG
6. Clique em **Criar grupo de segurança**.

**Tarefa concluída:** Grupo de segurança personalizado criado, permitindo tráfego HTTP de qualquer lugar.

---

## Tarefa 3: Iniciar a instância do Amazon EC2

Nesta tarefa, você criará uma instância EC2 e fornecerá um script de bootstrap para instalar e configurar a aplicação web.

### Passos principais

1. Pesquise e escolha **EC2** no console.
2. No painel esquerdo, clique em **Instâncias → Executar instâncias**.
3. Configurações:
    - Nome: `Web Application`
    - AMI: **Amazon Linux 2023 AMI**
    - Arquitetura: 64-bit (x86)
    - Tipo de instância: t3.micro
    - Par de chaves: **Prosseguir sem par de chaves** (não recomendado)
4. Configurações de rede:
    - VPC: `lab-2-vpc`
    - Sub-rede: `lab-2-subnet-public-1-[az-a]`
    - Atribuir IP público automaticamente: **Enable**
5. Firewall (grupos de segurança): selecione o **Web Security Group**
6. Detalhes avançados → Dados do usuário: Cole o script abaixo:

```bash
#!/bin/bash -ex

# Update yum
yum -y update

# installs nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

# download and install Node.js
nvm install 20

# Create a dedicated directory for the application
mkdir -p /var/app

# Get the app from S3
wget https://aws-tc-largeobjects.s3-us-west-2.amazonaws.com/ILT-TF-100-TECESS-5/app/app.zip

# Extract it
unzip app.zip -d /var/app/
cd /var/app/

# Install dependencies
npm install

# Start the app
npm start
```
7. Número de instâncias: 1 → Iniciar instância.
8. Aguarde até a instância mudar para Executando e verifique 3/3 checks passed.
9. Copie o Public IPv4 address e abra no navegador usando http://.


