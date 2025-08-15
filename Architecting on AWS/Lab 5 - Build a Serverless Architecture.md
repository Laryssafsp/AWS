**In this lab, you will use AWS managed services to build a serverless architecture.**

# 🧪 Resumo do Funcionamento do Laboratório 5 (Arquitetura Serverless)

## 🎯 Objetivo Principal
Implementar uma arquitetura *serverless* e orientada a eventos para processar imagens automaticamente, substituindo instâncias EC2 por funções AWS Lambda, usando Amazon S3, SNS, SQS e CloudWatch.

---

## ✅ Etapas e Funcionamento

### 🔹 1. Criação do Tópico SNS
- Criado um *Standard Topic* no Amazon SNS (`resize-image-topic-XXXX`).
- Ponto central de distribuição de notificações para filas SQS.

### 🔹 2. Criação das Filas SQS e Associação ao SNS
- Criadas duas filas *Standard*:
  - `thumbnail-queue` → processa imagens em miniatura (128×128).
  - `mobile-queue` → processa imagens para versão mobile (640×320).
- Ambas inscritas no tópico SNS para receber eventos de upload no S3.
- Publicação de mensagem no SNS para validar recebimento nas filas.

### 🔹 3. Configuração de Evento no S3
- Ajustada *Access Policy* do SNS para permitir publicação a partir do S3.
- Criada notificação no bucket S3 (`ingest/`) para enviar eventos ao SNS quando arquivos `.jpg` forem adicionados.

### 🔹 4. Criação das Funções Lambda
- **`CreateThumbnail`**
  - Dispara ao receber mensagem da `thumbnail-queue`.
  - Baixa imagem do S3, redimensiona para 128×128 e salva em `thumbnail/`.
- **`CreateMobileImage`**
  - Dispara ao receber mensagem da `mobile-queue`.
  - Baixa imagem do S3, redimensiona para 640×320 e salva em `mobile/`.

### 🔹 5. Teste de Funcionamento
1. Upload de imagem `.jpg` no diretório `ingest/` do bucket S3.
2. Evento aciona SNS → distribui para as filas SQS → dispara as Lambdas.
3. Funções processam e salvam imagens redimensionadas em pastas específicas no S3.
4. Logs e métricas monitorados pelo Amazon CloudWatch.

---

## 🧠 Como tudo funciona junto

| Componente        | Função no Sistema |
|-------------------|-------------------|
| Amazon S3         | Armazena imagens originais e processadas; gera eventos de upload. |
| Amazon SNS        | Recebe notificações do S3 e as distribui para as filas SQS. |
| Amazon SQS        | Mantém mensagens para as Lambdas processarem. |
| AWS Lambda        | Processa imagens em diferentes formatos sem necessidade de servidores. |
| Amazon CloudWatch | Monitora execução das funções e registra logs. |

---

## 🚀 Resultado Final
- Processamento de imagens totalmente *serverless* e orientado a eventos.
- Redução de custo substituindo EC2 por AWS Lambda.
- Imagens processadas armazenadas no mesmo bucket S3 em pastas distintas (`thumbnail/` e `mobile/`).
- Fácil monitoramento via CloudWatch.



---
### CreateThumbnailZIPLocation 
```python
import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus
from PIL import Image
import PIL.Image
import json

s3_client = boto3.client("s3")
s3 = boto3.resource("s3")


def resize_image(image_path, resized_path):
    with Image.open(image_path) as image:
        image.thumbnail((128, 128))
        image.save(resized_path)


def handler(event, context):
    for record in event["Records"]:
        payload = record["body"]
        sqs_message = json.loads(payload)
        bucket_name = json.loads(sqs_message["Message"])["Records"][0]["s3"]["bucket"][
            "name"
        ]
        print(bucket_name)
        key = json.loads(sqs_message["Message"])["Records"][0]["s3"]["object"]["key"]
        print(key)

        download_path = "/tmp/{}{}".format(uuid.uuid4(), key.split("/")[-1])
        upload_path = "/tmp/resized-{}".format(key.split("/")[-1])

        s3_client.download_file(bucket_name, key, download_path)
        resize_image(download_path, upload_path)
        s3.meta.client.upload_file(
            upload_path, bucket_name, "thumbnail/Thumbnail-" + key.split("/")[-1]
        )

```

---
### CreateMobileImage

```python
import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus
from PIL import Image
import PIL.Image
import json

s3_client = boto3.client("s3")
s3 = boto3.resource("s3")


def resize_image(image_path, resized_path):
    with Image.open(image_path) as image:
        image.thumbnail((640, 320))
        image.save(resized_path)


def handler(event, context):
    for record in event["Records"]:
        payload = record["body"]
        sqs_message = json.loads(payload)
        bucket_name = json.loads(sqs_message["Message"])["Records"][0]["s3"]["bucket"][
            "name"
        ]
        print(bucket_name)
        key = json.loads(sqs_message["Message"])["Records"][0]["s3"]["object"]["key"]
        print(key)

        download_path = "/tmp/{}{}".format(uuid.uuid4(), key.split("/")[-1])
        upload_path = "/tmp/resized-{}".format(key.split("/")[-1])

        s3_client.download_file(bucket_name, key, download_path)
        resize_image(download_path, upload_path)
        s3.meta.client.upload_file(
            upload_path, bucket_name, "mobile/MobileImage-" + key.split("/")[-1]
        )

```

