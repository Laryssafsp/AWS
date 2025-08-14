# 🧪 Resumo do Funcionamento do Laboratório 2 (Criar VPC e Iniciar Aplicação Web em EC2)

## 🎯 Objetivo Principal
Construir a infraestrutura básica para uma aplicação web hospedada em uma instância EC2, criando manualmente uma **VPC personalizada com sub-redes públicas** e configurando **acesso à internet**, **segurança** e **deploy da aplicação via script**.

---

## ✅ Etapas e Funcionamento

### 🔹 1. Criação da VPC Personalizada
Você cria uma **Amazon VPC** com os seguintes componentes:
- CIDR da VPC: `10.0.0.0/16`
- Duas **sub-redes públicas** em AZs diferentes:
  - Sub-rede 1: `10.0.0.0/24`
  - Sub-rede 2: `10.0.1.0/24`
- Um **Internet Gateway** e uma **tabela de rotas pública** para acesso externo.
- Nomes DNS e resolução de DNS habilitados.

> ✅ **Saída esperada:** Todos os recursos da VPC foram criados com sucesso.

---

### 🔹 2. Criação do Grupo de Segurança
Você configura um **Security Group personalizado** para permitir tráfego HTTP:

- Nome: `Web Security Group`
- Regra de entrada:
  - Tipo: HTTP (porta 80)
  - Origem: Anywhere-IPv4 (`0.0.0.0/0`)

> ✅ **Tarefa concluída:** Grupo de segurança criado, permitindo acesso à aplicação via navegador.

---

### 🔹 3. Lançamento da Instância EC2
Você cria uma instância EC2 com as seguintes configurações:
- AMI: **Amazon Linux 2023**
- Tipo: `t3.micro`
- Sub-rede: `lab-2-subnet-public-1-[az-a]`
- IP público automático: **Ativado**
- Grupo de segurança: `Web Security Group`

#### Script de inicialização (user data):
- Instala o **Node.js** com `nvm`
- Baixa e extrai a aplicação de um bucket S3
- Instala dependências (`npm install`)
- Inicia a aplicação (`npm start`)

> ✅ **Saída esperada:** Aplicação iniciada automaticamente na porta 80.

---

## 🧠 Como tudo funciona junto

| Componente                  | Função no sistema                                                               |
|-----------------------------|----------------------------------------------------------------------------------|
| **Amazon VPC**              | Isola e estrutura logicamente os recursos em uma rede virtual.                  |
| **Sub-redes Públicas**      | Hospedam recursos acessíveis via internet.                                      |
| **Internet Gateway**        | Permite comunicação entre instâncias e a internet.                              |
| **Tabela de Rotas Pública** | Direciona tráfego da VPC para a internet via IGW.                               |
| **Security Group**          | Controla o tráfego permitido para a instância EC2 (porta 80 liberada).          |
| **EC2 Instance**            | Hospeda a aplicação Node.js após ser iniciada via script.                       |
| **User Data Script**        | Automatiza a configuração da aplicação no momento do boot da instância.         |

---

## 🚀 Resultado Final

- Aplicação web está acessível via navegador usando o IP público da instância EC2.
- Infraestrutura de rede criada manualmente com boas práticas (VPC, sub-redes, rotas e segurança).
- Aplicação configurada automaticamente via **script de bootstrap**.
- Ambiente pronto para escalabilidade futura e integração com outros serviços AWS.
