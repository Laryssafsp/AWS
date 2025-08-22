# Laboratório 1: Configurar o Ambiente de Desenvolvimento (Python)

## Visão Geral
Neste laboratório, você configurará um ambiente de desenvolvimento em nuvem para trabalhar com a AWS. O objetivo é garantir que o **IDE (VS Code)**, a **AWS CLI** e as permissões do **IAM** estejam prontos para o desenvolvimento de aplicações que utilizam serviços da AWS.

## Objetivos
- Conectar-se ao ambiente de desenvolvimento (VS Code em uma instância EC2).
- Verificar instalação do **Python** e **AWS CLI**.
- Configurar região e formato da AWS CLI.
- Validar permissões do **IAM**.
- Anexar políticas de IAM para excluir buckets do **Amazon S3**.

---

## Tarefa 0: Conectar ao Ambiente
1. Acesse o **LabWorkspaceURL**.
2. Faça login com a senha fornecida.
3. O **VS Code** será aberto em uma instância do Amazon EC2.
4. Utilize o **terminal bash** para executar os comandos.

---

## Tarefa 1: Verificar Ambiente

### 1.1 Verificar Python
```bash
python3 --version
```
Saída esperada (exemplo):
```
Python 3.11.16
```

### 1.2 Verificar AWS CLI
```bash
aws --version
```
Saída esperada (exemplo):
```
aws-cli/2.17.18 Python/3.9.20 Linux/6.1
```

### 1.3 Configurar Região
```bash
aws configure
```
Exemplo:
```
AWS Access Key ID [None]:
AWS Secret Access Key [None]:
Default region name [None]: ap-northeast-1
Default output format [None]: yaml
```

### 1.4 Verificar Credenciais em Uso
```bash
aws sts get-caller-identity
```
Exemplo de saída:
```
Account: '012345678901'
Arn: arn:aws:sts::012345678901:assumed-role/notes-application-role/i-047954185d0aa81f3
```

---

## Tarefa 2: Usar Extensão AWS no VS Code
1. Abra a extensão AWS (ícone lateral).
2. Confirme que aparece **Connected with ec2:instance**.
3. Configure a região correta.
4. Explore os serviços disponíveis pelo **AWS Explorer**.

---

## Tarefa 3: Verificar Permissões IAM

### 3.1 Listar Buckets S3
```bash
aws s3 ls
```

### 3.2 Definir Variável do Bucket e Tentar Excluir
```bash
bucketToDelete=$(aws s3api list-buckets --output text --query 'Buckets[?contains(Name, `deletemebucket`)==`true`] | [0].Name')
aws s3 rb s3://$bucketToDelete
```
Saída esperada:
```
An error occurred (AccessDenied) when calling the DeleteBucket operation: Access Denied
```

### 3.3 Debug da Operação
```bash
aws s3 rb s3://$bucketToDelete --debug
```
Mostra detalhes de autenticação e erro `403 AccessDenied`.

---

## Tarefa 4: Corrigir Permissões IAM

### 4.1 Obter ARN da Política
```bash
policyArn=$(aws iam list-policies --output text --query 'Policies[?PolicyName == `S3-Delete-Bucket-Policy`].Arn')
```

### 4.2 Analisar Política
```bash
aws iam get-policy-version --policy-arn $policyArn --version-id v1
```

### 4.3 Anexar Política à Função
```bash
aws iam attach-role-policy --policy-arn $policyArn --role-name notes-application-role
```

### 4.4 Confirmar e Excluir Bucket
```bash
aws iam list-attached-role-policies --role-name notes-application-role
aws s3 rb s3://$bucketToDelete
aws s3 ls
```

---

## Conclusão
Você configurou o ambiente de desenvolvimento, validou permissões do IAM e anexou políticas para excluir buckets do Amazon S3.

---

## Recursos Adicionais
- [AWS CLI Reference - STS](https://docs.aws.amazon.com/cli/latest/reference/sts/index.html)
- [AWS CLI Reference - S3](https://docs.aws.amazon.com/cli/latest/reference/s3/index.html)
- [AWS CLI Reference - IAM](https://docs.aws.amazon.com/cli/latest/reference/iam/index.html)
