# 🧪 Resumo do Funcionamento do Laboratório 4 (Alta Disponibilidade)

## 🎯 Objetivo Principal
Transformar uma aplicação web (**Employee Directory**) que roda em uma única instância **EC2** em uma aplicação **altamente disponível**, que **escala automaticamente** conforme a demanda.

---

## ✅ Etapas e Funcionamento

### 🔹 1. Análise Inicial da Instância
- Verifica-se a aplicação web rodando em uma única instância **EC2**.
- A aplicação está acessível via **URL público**.

### 🔹 2. Criação do Load Balancer
- Cria-se um **Application Load Balancer (ALB)** que:
  - Distribui o tráfego entre múltiplas instâncias.
  - Usa um **grupo de destino** com **health checks**.
  - Permite acesso centralizado à aplicação via **DNS do ALB**.

### 🔹 3. Criação do Modelo de Execução
- Criação de um **Launch Template** com:
  - AMI, tipo da instância, grupo de segurança.
  - Script de inicialização no campo **user data** que:
    - Instala dependências.
    - Baixa e inicia a aplicação.
    - Permite testes de carga (*stress*).

### 🔹 4. Configuração do Auto Scaling
- Criação de um **Auto Scaling Group (ASG)** com:
  - Mínimo de **2 instâncias**, máximo de **4**.
  - Política de scaling baseada em **uso de CPU (alvo: 30%)**.
  - Ligado ao **grupo de destino do ALB**.
  - Configuração de **notificações por e-mail** em eventos de scaling.

### 🔹 5. Teste de Escalabilidade
- Acesso à aplicação via ALB mostra instâncias de diferentes **Zonas de Disponibilidade**.
- Realiza-se teste de carga por **10 minutos**.
- O **Auto Scaling** detecta o aumento do uso da CPU e cria novas instâncias automaticamente.
- Verificação no console da AWS confirma instâncias adicionais.
- Recebimento de **notificação por e-mail** informando o scaling.

---

## 🧠 Como tudo funciona junto

| Componente                | Função no sistema                                                                 |
|---------------------------|-----------------------------------------------------------------------------------|
| **EC2 Launch Template**   | Define como novas instâncias serão criadas.                                       |
| **Application Load Balancer** | Distribui o tráfego entre instâncias em múltiplas Zonas de Disponibilidade.   |
| **Auto Scaling Group**    | Cria e termina instâncias automaticamente conforme a carga da aplicação.         |
| **S3 + IAM Role**         | Fornece arquivos da aplicação e permissões para acessá-los.                      |
| **Health Checks**         | Garantem que somente instâncias saudáveis recebam tráfego.                       |

---

## 🚀 Resultado Final
- A aplicação é acessível via **Load Balancer** (**alta disponibilidade**).
- Escala automaticamente (**Auto Scaling**) conforme o uso da CPU.
- Instâncias estão distribuídas em **múltiplas zonas de disponibilidade**.
- A **instância original** é removida, e o ambiente passa a operar de forma **escalável e resiliente**.
