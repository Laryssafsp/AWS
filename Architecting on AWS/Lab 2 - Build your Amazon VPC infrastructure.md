# Lab 2 - Build your Amazon VPC infrastructure 2 hoursPreloading
**This lab follows Compute Module, which focuses primarily on Amazon EC2, and Networking Part 1 Module, which focuses on Amazon VPCs, subnets, and routing.**

# Lab 2 – VPC com Subnets Públicas e Privadas

## Task 7: Conectar à instância pública via HTTP

1. No console, vá em **Instances** → selecione **Public Instance** → aba **Networking**.
2. Copie o **Public IPv4 DNS**.
3. Abra em navegador: a página Apache mostra **Instance ID** e **Availability Zone**.

---

## Task 8: Conectar à instância pública via Session Manager

1. Console → **Instances** → selecione **Public Instance** → **Connect** → **Session Manager** → **Connect**.
2. Teste conectividade:

```bash
cd ~
curl -I https://aws.amazon.com/training/
```

3. Saída esperada: HTTP/2 200 + headers do site AWS.

---

## Task 9: Criar NAT Gateway e configurar rota da subnet privada

1. Console → **VPC** → **NAT gateways** → **Create NAT gateway**:

   * Subnet: Public Subnet
   * Elastic IP: Allocate
   * Nome opcional: `Lab NGW`
2. Console → **Route tables** → **Create route table**:

   * Nome: `Private Route Table`
   * VPC: Lab VPC
3. Edit routes → Add route:

   * Destination: `0.0.0.0/0`
   * Target: NAT Gateway
4. Subnet associations → associar **Private Subnet**.

---

## Task 10: Criar security group para recursos privados

1. Console → **Security groups** → **Create security group**:

   * Nome: `Private SG`
   * VPC: Lab VPC
   * Inbound rule: HTTP → Source: Public SG
2. Salvar.

---

## Task 11: Launch EC2 na private subnet

### 11.1 Configuração inicial

* Nome: `Private Instance`

### 11.3 Seleção de AMI

* Amazon Linux 2023

### 11.4 Tipo de instância

* t3.micro

### 11.5 Key pair

* **Proceed without a key pair**

### 11.6 Network settings

* VPC: Lab VPC
* Subnet: Private Subnet
* Auto-assign public IP: Disable

### 11.7 Security group

* Selecionar **Private SG**

### 11.8 Armazenamento

* Default

### 11.9 IAM role

* Selecionar **EC2InstProfile**

### 11.10 User data (instala Apache e PHP)

```bash
#!/bin/bash
yum update -y
yum install -y httpd php8.1
systemctl enable httpd.service
systemctl start httpd
cd /var/www/html
wget https://us-west-2-tcprod.s3.amazonaws.com/courses/ILT-TF-200-ARCHIT/v7.9.11.prod-60bc4f16/lab-2-VPC/scripts/instanceData.zip
unzip instanceData.zip
```

### 11.11 Launch

* Revisar configuração e **Launch instance**
* Esperar instância **Running** e status checks 3/3

---

## Task 12: Conectar à instância privada via Session Manager

1. Console → **Instances** → selecione **Private Instance** → **Connect** → **Session Manager** → **Connect**.
2. Teste conectividade:

```bash
cd ~
curl -I https://aws.amazon.com/training/
```

3. Saída esperada: HTTP/2 200 + headers do site AWS.

---

### Optional Task 1: Testar conectividade privada-publica

1. Copiar **Private IPv4** da instância privada.
2. Conectar à instância pública via Session Manager.
3. Testar acesso ao web server privado:

```bash
curl PRIVATE_IP
ping PRIVATE_IP
```

4. Se ping falhar, ajustar **inbound rule** da Private SG:

   * Type: Custom ICMP - IPV4
   * Source: Public SG

---

### Optional Task 2: Recuperar metadata da instância

1. Conectar à instância pública via Session Manager.
2. Recuperar metadata:

```bash
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/
```

3. Recuperar public-hostname:

```bash
curl http://169.254.169.254/latest/meta-data/public-hostname -H "X-aws-ec2-metadata-token: $TOKEN"
```

---

## Conclusão

* Criou VPC com subnets públicas e privadas.
* Instâncias públicas e privadas lançadas e conectadas via Session Manager.
* NAT gateway configurado para permitir tráfego de instâncias privadas.
* Security groups configurados para isolamento seguro.
* Metadata da instância recuperada via CLI.

---

## Recursos adicionais

* [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
* [Subnets for Your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html)
* [Internet Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)
* [Route Tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)
* [Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
* [NAT Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)
