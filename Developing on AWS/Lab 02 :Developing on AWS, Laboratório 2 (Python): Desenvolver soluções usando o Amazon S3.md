# 🧪 Resumo do Funcionamento do Laboratório 2 (Amazon S3 com Python e AWS CLI)

🎯 **Objetivo Principal**  
Explorar o Amazon S3 criando e gerenciando buckets e objetos usando **AWS Management Console**, **AWS CLI** e **Python (boto3)**.

---

## ✅ Etapas e Passos Técnicos

### 🔹 1. Criar Bucket no Amazon S3
- No Console AWS → **Amazon S3 → Create bucket**  
- Nome sugerido: `lab2-bucket-<ID_UNICO>`  
- Região: mesma usada para os recursos do laboratório.  
- Desmarcar "Block all public access" (se solicitado).  
- Confirmar e criar.

📌 **Via CLI:**
```bash
aws s3 mb s3://lab2-bucket-<ID_UNICO> --region us-east-1
```

---

### 🔹 2. Fazer Upload de Objetos
- No Console → abrir bucket criado → **Upload → Add files**.  
- Selecionar arquivos de teste (`.txt`, `.csv`, etc.) → **Upload**.

📌 **Via CLI:**
```bash
aws s3 cp arquivo.txt s3://lab2-bucket-<ID_UNICO>/arquivo.txt
```

📌 **Via Python (boto3):**
```python
import boto3
s3 = boto3.client('s3')
s3.upload_file('arquivo.txt', 'lab2-bucket-<ID_UNICO>', 'arquivo.txt')
```

---

### 🔹 3. Listar Objetos do Bucket
📌 **Via CLI:**
```bash
aws s3 ls s3://lab2-bucket-<ID_UNICO>
```

📌 **Via Python:**
```python
response = s3.list_objects_v2(Bucket='lab2-bucket-<ID_UNICO>')
for obj in response.get('Contents', []):
    print(obj['Key'])
```

---

### 🔹 4. Baixar Objetos do Bucket
📌 **Via CLI:**
```bash
aws s3 cp s3://lab2-bucket-<ID_UNICO>/arquivo.txt arquivo_baixado.txt
```

📌 **Via Python:**
```python
s3.download_file('lab2-bucket-<ID_UNICO>', 'arquivo.txt', 'arquivo_baixado.txt')
```

---

### 🔹 5. Deletar Objetos
📌 **Via CLI:**
```bash
aws s3 rm s3://lab2-bucket-<ID_UNICO>/arquivo.txt
```

📌 **Via Python:**
```python
s3.delete_object(Bucket='lab2-bucket-<ID_UNICO>', Key='arquivo.txt')
```

---

### 🔹 6. Deletar Bucket
📌 **Via CLI:**
```bash
aws s3 rb s3://lab2-bucket-<ID_UNICO> --force
```

📌 **Via Python:**
```python
s3.delete_bucket(Bucket='lab2-bucket-<ID_UNICO>')
```

---

## 🧠 Como tudo funciona junto

| Componente | Função |
|------------|--------|
| **Amazon S3** | Armazena objetos (arquivos e metadados). |
| **AWS CLI** | Linha de comando para interagir com buckets e objetos. |
| **Python boto3** | SDK que permite automação e scripts para gerenciar o S3. |
| **Console AWS** | Interface gráfica para criação e teste manual. |

---

## 🚀 Resultado Final
- Bucket criado com sucesso.  
- Objetos adicionados, listados, baixados e removidos.  
- Todo processo validado via **Console**, **CLI** e **Python (boto3)**.  
- Ambiente pronto para uso de S3 em aplicações e automações.
