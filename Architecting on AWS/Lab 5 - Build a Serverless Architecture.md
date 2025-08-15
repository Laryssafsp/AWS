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
