## Lab 4 - Configure high availability in your Amazon VPC 2 hours
**This lab provides hands-on practice deploying redundant resources in a VPC such as NAT gateway, VPC routing, EC2 auto scaling groups, and Amazon Aurora DB clusters**

# Lab 4 – Configure High Availability in Your Amazon VPC

**Objetivo:** Aprender a criar sistemas altamente disponíveis e tolerantes a falhas na AWS, utilizando Auto Scaling, Load Balancer, Aurora Multi-AZ e NAT gateways redundantes.

---

## Pré-requisitos
- Notebook com Windows/macOS/Linux e navegador (Chrome, Firefox, Edge)
- Editor de texto simples

---

## Tarefa 1 – Inspecionar o ambiente existente

### Recursos provisionados:
- Amazon VPC com subnets públicas e privadas em duas AZs
- Internet Gateway
- NAT Gateway em uma subnet pública
- Application Load Balancer (ALB) em subnets públicas
- EC2 AppServer em subnet privada
- Aurora DB cluster em subnet privada

### Passos principais:
1. Acesse o console VPC e examine:
   - VPC e subnets
   - Route tables
   - Network ACLs
   - Security groups (Inventory-ALB, Inventory-App, Inventory-DB)
2. Verifique o EC2 AppServer:
   - Copie o **user data** para uso futuro.
3. Verifique o ALB e target group:
   - Inventory-App target group já contém o AppServer.
4. Abra a aplicação PHP de inventário no navegador:
   - URL do InventoryAppSettingsPage
   - Salve as configurações padrão
   - Adicione ou modifique itens do inventário
> **Observação:** Deixe a aba da aplicação aberta.

---

## Tarefa 2 – Criar um Launch Template
1. Console EC2 → Launch Templates → Create launch template
2. Configurações:
   - Nome: `Lab-launch-template`
   - AMI: Amazon Linux 2023
   - Instance type: `t3.micro`
   - Security group: `Inventory-App`
   - IAM profile: `Inventory-App-Role`
   - User data: colado do passo anterior
3. Criar template e salvar

---

## Tarefa 3 – Criar Auto Scaling Group
1. Console EC2 → Auto Scaling Groups → Create Auto Scaling group
2. Configurações:
   - Nome: `Inventory-ASG`
   - Launch template: `Lab-launch-template`
   - Subnets: Private Subnet 1 e 2
   - Attach to existing load balancer: Inventory-App | HTTP
   - Health check grace period: 300s
   - Desired/Min/Max capacity: 2
   - Enable group metrics
   - Tag: `Name=Inventory-App`
3. Criar Auto Scaling group
4. Verifique Activity, Instance management e Monitoring

---

## Tarefa 4 – Testar aplicação
1. Deregister AppServer original do target group Inventory-App
2. Confirme que apenas as instâncias Inventory-App permanecem
3. Acesse a aplicação via ALB:
   - DNS do load balancer
   - Refresh da página confirma balanceamento entre as duas instâncias

---

## Tarefa 5 – Testar alta disponibilidade (Application Tier)
1. EC2 → Instances → Terminate uma instância Inventory-App
2. Observe:
   - Requests redirecionados para a instância restante
   - Auto Scaling lança uma nova instância automaticamente
3. Refresh da aplicação confirma alta disponibilidade

---

## Tarefa 6 – Alta disponibilidade do banco de dados
### 6.1 Criar Aurora Replica
1. RDS → Databases → inventory-cluster → Add reader
2. Configurações:
   - DB identifier: `inventory-replica`
   - AZ diferente da primária
   - Disable Enhanced Monitoring
3. Após a criação, Aurora replica aumenta disponibilidade e permite failover

---

## Tarefa 7 – Alta disponibilidade do NAT Gateway
### 7.1 Criar NAT Gateway secundário
1. VPC → NAT gateways → Create NAT gateway
2. Configurações:
   - Subnet: Public Subnet 2
   - Allocate Elastic IP
3. Criado com sucesso

### 7.2 Criar nova Route Table
1. Route tables → Create route table
   - Nome: `Private Route Table 2`
   - VPC: Lab VPC
2. Edit routes → Add route:
   - Destination: `0.0.0.0/0`
   - Target: `my-nat-gateway`
3. Subnet associations → Associate Private Subnet 2

> NAT gateways agora são redundantes entre AZs

---

## Tarefa 8 – Force failover da Aurora
1. RDS → inventory-primary → Actions → Failover
2. Observe:
   - Replica promovida para Writer
   - Aplicação continua funcionando
> Confirma que o banco está altamente disponível

---

## Conclusão
- Criado EC2 Auto Scaling group com ALB multi-AZ
- Aurora DB cluster altamente disponível
- VPC configurada com NAT gateways redundantes
- Failover do banco de dados confirmado

---

## Fim do Lab
1. Console → AWSLabsUser → Sign out
2. End Lab
