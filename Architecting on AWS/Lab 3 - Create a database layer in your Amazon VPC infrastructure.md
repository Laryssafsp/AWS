## Lab 3 - Create a database layer in your Amazon VPC infrastructure 
**In this lab, you create an Amazon RDS database, view the database metadata, create an Application Load Balancer, configure the target group, register an existing Amazon EC2 instance as a target with the target group and test the load balancer.**

# Lab 3: Criando uma Camada de Banco de Dados na Sua Infraestrutura Amazon VPC

© 2025 Amazon Web Services, Inc. ou suas afiliadas. Todos os direitos reservados.

---

## Visão Geral do Lab

Um banco de dados backend desempenha um papel importante em qualquer ambiente, e a segurança e o controle de acesso a este recurso crítico são vitais para qualquer arquitetura. Neste lab, você criará um cluster de banco de dados Amazon Aurora para gerenciar um banco de dados MySQL e um Application Load Balancer (ALB). O ALB encaminha o tráfego para instâncias Amazon EC2 saudáveis que hospedam a aplicação front-end.

## Objetivos

* Criar uma instância de banco de dados Amazon RDS.
* Criar um Application Load Balancer.
* Criar um listener HTTP para o ALB.
* Criar um grupo de destino (target group).
* Registrar alvos em um grupo de destino.
* Testar o load balancer e a conectividade da aplicação ao banco de dados.
* Revisar os metadados da instância Amazon RDS através do console.
* Opcional: Criar uma réplica de leitura Amazon RDS em uma região AWS diferente.

## Pré-requisitos

* Notebook com Wi-Fi e Windows/macOS/Linux
* Navegador de internet (Chrome, Firefox, Edge)
* Editor de texto simples

---

## Tarefa 1: Criar um Banco de Dados Amazon RDS

1. No Console de Gerenciamento AWS, pesquise e escolha **RDS**.
2. Navegue para **Databases** → **Create database**.
3. Selecione **Standard create**.
4. Opções do mecanismo: **Aurora (MySQL Compatible)**.
5. Template: **Dev/Test**.
6. Configurações:

   * Identificador do cluster de banco de dados: `aurora`
   * Nome de usuário mestre: `dbadmin`
   * Gerenciamento de credenciais: **Self managed**
   * Senha mestre: `LabPassword` (fornecida nas instruções do lab)
7. Configuração da instância:

   * Classe da instância DB: `db.t3.medium`
   * Multi-AZ deployment: **Não criar uma réplica Aurora**
8. Conectividade:

   * VPC: `LabVPC`
   * DB subnet group: `labdbsubnetgroup`
   * Acesso público: **Não**
   * Security group: `LabDBSecurityGroup`
9. Configurações adicionais:

   * Nome do banco inicial: `inventory`
   * DB cluster parameter group: selecione o valor correto conforme instruções do lab
   * Desmarque **Enable encryption**
   * Desmarque **Enable auto minor version upgrade**
10. Clique em **Create database**.
11. Feche a janela de sugestões adicionais.

> Parabéns! Você criou com sucesso um banco de dados Amazon RDS.

---

## Tarefa 2: Criar e Configurar um Application Load Balancer

### Tarefa 2.1: Criar um Grupo de Destino

1. No console, pesquise e escolha **EC2**.
2. Navegue para **Load Balancing** → **Target Groups** → **Create target group**.
3. Configurações básicas:

   * Tipo de alvo: **Instances**
   * Nome do grupo de destino: `ALBTargetGroup`
   * VPC: `LabVPC`
4. Registrar instâncias:

   * Selecione `AppServer1` e `AppServer2`
   * Clique em **Include as pending below**
5. Clique em **Create target group**.

### Tarefa 2.2: Criar um Application Load Balancer

1. Navegue para **Load Balancers** → **Create load balancer**.
2. Tipo de load balancer: **Application Load Balancer**
3. Configurações básicas:

   * Nome: `LabAppALB`
   * VPC: `LabVPC`
   * Subnets: `PublicSubnet1` e `PublicSubnet2`
   * Security group: `LabALBSecurityGroup`
   * Listener HTTP:80 → Ação padrão: `ALBTargetGroup`
4. Clique em **Create load balancer**

> Parabéns! Você criou o ALB, o grupo de destino e registrou as instâncias EC2.

---

## Tarefa 3: Revisar os Metadados da Instância RDS

1. No console AWS, pesquise e escolha **RDS** → **Databases**.
2. Selecione o cluster `aurora`.
3. Guia **Connectivity & Security**: copie o endpoint da instância writer.
4. Verifique que o status do endpoint está **Available**.
5. Guia **Monitoring**: verifique métricas de conexões, leituras/escritas, memória, CPU e tráfego.

> Parabéns! Você revisou os metadados da instância RDS.

---

## Tarefa 4: Testar a Conectividade da Aplicação ao Banco

1. No console AWS, vá para **Target Groups** → selecione `ALBTargetGroup`
2. Aguarde até que o status das instâncias esteja **healthy**
3. Navegue para **Load Balancers**, copie o DNS e abra no navegador.
4. Configurações da aplicação:

   * Endpoint: cole o endpoint writer do RDS
   * Database: `inventory`
   * Username: `dbadmin`
   * Password: `LabPassword`
5. Clique em **Save**

> Parabéns! Você acessou a aplicação através do ALB e ela está conectada ao banco de dados.

---

## Tarefa Opcional: Criar uma Réplica de Leitura Amazon RDS em Outra Região

1. No console RDS, selecione a instância `aurora` → **Actions** → **Create cross-Region read replica**
2. Multi-AZ: **Don't create an Aurora Replica**
3. Configurações:

   * Região de destino: `RemoteRegion` (conforme instruções)
   * VPC: `LabVPC`
   * Acesso público: **Não**
   * Security group: `LabDBSecurityGroup`
   * Identificador: `LabDBreplica`
4. Clique em **Create**

> Parabéns! Você iniciou a criação da réplica de leitura em outra região.

---

## Conclusão

* Criou uma instância Amazon RDS.
* Criou um Application Load Balancer.
* Criou listener HTTP para o ALB.
* Criou grupo de destino e registrou instâncias.
* Testou conectividade da aplicação com o banco.
* Revisou os metadados da instância RDS.

> Observação: O design deste lab é apenas para aprendizado e não é totalmente elástico ou altamente disponível. Você aprenderá sobre redundância e alta disponibilidade no próximo lab.

---

## Encerramento do Lab

1. No Console AWS, clique em **AWSLabsUser** → **Sign out**
2. Clique em **End Lab** e confirme.

---

Para mais informações: [AWS Training and Certification](https://aws.amazon.com/training/)
