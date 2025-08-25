In this lab, students will develop a portion of the application using Amazon S3 to store files and configure a static website.

# 🧪 Resumo do Funcionamento do Laboratório 2 (S3 com Python e AWS CLI)

🎯 **Objetivo Principal**  
Desenvolver uma aplicação que utiliza o **Amazon S3** como serviço de **armazenamento** (CSV, JSON, MP3) e **hospedagem de site estático**, interagindo programaticamente via **Python (Boto3)** e **AWS CLI**.  
O laboratório foca em criar buckets, fazer upload/download de objetos, processar dados e configurar hospedagem de site.

---

## ✅ Etapas e Funcionamento

### 🔹 1. Criar Bucket no Amazon S3 (`create-bucket.py`)
- Configuração inicial no **config.ini** → `bucket_name=notes-bucket-123456789`.  
- Script estruturado em funções:  
  - `verifyBucketName` → verifica se o nome é válido.  
  - `createBucket` → cria bucket com `LocationConstraint`.  
  - `verifyBucket` → confirma existência com waiter.  

**Trechos de código principais:**  
```python
# TODO 1 - Criar cliente S3
client = boto3.client('s3')

# TODO 2 - Verificar nome do bucket
s3Client.head_bucket(Bucket=bucket)

# TODO 3 - Criar bucket
if current_region == 'us-east-1':
    response = s3Client.create_bucket(Bucket=name)
else:
    response = s3Client.create_bucket(
        Bucket=name,
        CreateBucketConfiguration={'LocationConstraint': current_region}
    )

# TODO 4 - Esperar criação
waiter = s3Client.get_waiter('bucket_exists')
waiter.wait(Bucket=bucket)
```

✅ Resultado: Bucket criado com sucesso.

---

### 🔹 2. Upload de Objeto no Bucket (`create-object.py`)
- Upload do arquivo **notes.csv** com metadados.  

**Trecho de código correto:**  
```python
# TODO 5 - Upload do arquivo CSV
response = s3Client.upload_file(
    Bucket=bucket, 
    Key=key,
    Filename=name,
    ExtraArgs={
        'ContentType': contentType,
        'Metadata': metadata
    }
)
```

✅ Resultado: Arquivo `notes.csv` criado no bucket com metadados.

---

### 🔹 3. Processar Dados: Converter CSV → JSON (`convert-csv-to-json.py`)
- Baixar `notes.csv` do bucket.  
- Converter em JSON.  
- Fazer upload do novo objeto no bucket.  

**Trechos de código principais:**  
```python
# TODO 6 - Download objeto em memória
s3Client.download_fileobj(
    Bucket=bucket, 
    Key=key, 
    Fileobj=bytes_buffer
)

# TODO 7 - Upload objeto convertido em JSON
s3Client.put_object(
    Bucket=bucket, 
    Key=key,
    Body=data,
    ContentType=contentType,
    Metadata=metadata
)
```

✅ Resultado: JSON gerado e armazenado no bucket.

---

### 🔹 4. Configurar Website Estático no S3 (via CLI)
- Definir variável com bucket:  
```bash
mybucket=NOTES_BUCKET_NAME
```

- Permitir acesso público:  
```bash
aws s3api put-public-access-block --bucket $mybucket  --public-access-block-configuration "BlockPublicPolicy=false,RestrictPublicBuckets=false"
```

- Upload dos arquivos HTML:  
```bash
aws s3 sync ~/environment/html/. s3://$mybucket/
```

- Ativar hospedagem de site:  
```bash
aws s3api put-bucket-website --bucket $mybucket  --website-configuration file://~/environment/website.json
```

- Aplicar política de acesso público:  
```bash
sed -i "s/\[BUCKET\]/$mybucket/g" ~/environment/policy.json
aws s3api put-bucket-policy --bucket $mybucket --policy file://~/environment/policy.json
```

- Obter URL do site:  
```bash
printf "\nhttp://$mybucket.s3-website-$region.amazonaws.com\n\n"
```

✅ Resultado: Site estático hospedado e acessível via navegador.

---

### 🔹 5. Desafio Opcional (Python) – `create-s3-website.py`
- Automação da configuração de website com Python.  
- **TODOs principais:**  
  - Upload de arquivos HTML.  
  - Ativar hospedagem de site.  
  - Aplicar política de acesso.  

---

## 🧠 Como tudo funciona junto

| Componente         | Função                                                                 |
|--------------------|------------------------------------------------------------------------|
| **Boto3 (Python)** | Criar bucket, fazer upload/download e manipular objetos no S3.         |
| **Waiters**        | Garantir que o bucket foi realmente criado antes do uso.               |
| **AWS CLI**        | Configurar hospedagem do site e aplicar política de acesso.            |
| **S3**             | Armazenar CSV, JSON, metadados e hospedar website estático.            |

---

## 🚀 Resultado Final
- Bucket criado e validado com **waiters**.  
- Arquivo CSV carregado com metadados.  
- Conversão CSV → JSON implementada e testada.  
- Site estático hospedado com sucesso no **Amazon S3**.  
- Opção extra: automação de hospedagem via **Python (Boto3)**.  

👉 Ambiente pronto para **armazenamento, processamento de dados e web hosting no S3**.

