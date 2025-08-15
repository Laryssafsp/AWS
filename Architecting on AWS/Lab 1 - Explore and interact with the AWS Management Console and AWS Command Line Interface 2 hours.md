# 🧪 Lab 1: Exploring and Interacting with the AWS Management Console and AWS CLI

## 📌 Objetivos
- Explorar e interagir com o **AWS Management Console**.
- Criar recursos usando o **AWS Management Console**.
- Explorar e interagir com o **AWS CLI**.
- Criar recursos usando o **AWS CLI**.

---

## ⚙️ Task 1: Explorar e configurar o AWS Management Console

### 1.1 Escolher uma AWS Region
1. No console, clique no seletor de **Region** (topo direito) e escolha a desejada.
2. Configurar a **default Region**:
   - ⚙️ Ícone de engrenagem → *See all user settings* → Edit → selecionar região → Save settings → Go to new default Region.
3. Verifique se a região corresponde ao **LabRegion**.

### 1.2 Buscar serviços
- Use a barra de **Search** para procurar serviços, documentação e AWS Marketplace.
- Exemplo: digitar `cloud` e clicar no serviço desejado.

### 1.3 Adicionar e remover favoritos
- **Adicionar:** Services → All Services → clicar na estrela ao lado do serviço.
- **Remover:** Services → Favorites → desmarcar estrela.

### 1.4 Abrir console de um serviço
- Services → Favorites / Recently Visited / All Services → escolher serviço.
- Retornar à home: clicar no logo da AWS.

### 1.5 Criar e usar widgets do dashboard
- **Adicionar:** + Add widgets → arrastar para a página.
- **Reorganizar:** arrastar pelo título.
- **Redimensionar:** arrastar canto inferior direito.
- **Remover:** clicar nos três pontos → Remove widget.

---

## 🗂 Task 2: Criar bucket S3 via Console
1. Services → Storage → S3 → Buckets → Create bucket.
2. Nome do bucket: `labbucket-NUMBER` (único globalmente).
3. Região: LabRegion.
4. Manter demais configurações padrão → Create bucket.
5. Mensagem de sucesso: *Successfully created bucket “labbucket-xxxxx”*.

---

## 📤 Task 3: Upload de objeto no S3 via Console
1. Baixar arquivo **HappyFace.jpg**.
2. Abrir bucket criado → Upload → Add files → selecionar arquivo → Upload.
3. Mensagem de sucesso: *Upload succeeded*.

---

## 💻 Task 4: Criar bucket S3 e upload via AWS CLI

### 4.1 Conectar ao Command Host
1. EC2 → Instances → selecionar **Command Host** → Connect → Session Manager → Connect.
2. Terminal do EC2 será aberto em nova aba.

### 4.2 Comandos S3 no CLI
```bash
# Listar buckets existentes
aws s3 ls

# Criar bucket
aws s3 mb s3://labclibucket-NUMBER

# Verificar bucket criado
aws s3 ls

# Copiar arquivo para bucket
aws s3 cp /home/ssm-user/HappyFace.jpg s3://labclibucket-NUMBER

# Listar objetos do bucket
aws s3 ls s3://labclibucket-NUMBER
```

✅ Conclusão

- Console explorado e personalizado.
- Bucket S3 criado e arquivo enviado via Console.
- Bucket S3 criado e arquivo enviado via CLI.
- Experiência com gerenciamento de recursos AWS tanto via Console quanto CLI.

🔚 Finalizar Lab

1. AWS Management Console → usuário AWSLabsUser → Sign out.
2. End Lab → Confirm.
