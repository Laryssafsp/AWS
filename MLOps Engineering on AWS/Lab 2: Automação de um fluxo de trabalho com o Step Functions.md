# 🧪 Resumo do Funcionamento do Laboratório 2 (Automação de Fluxo de ML com Step Functions)

[GITHUB](https://github.com/aws/amazon-sagemaker-examples/blob/09f6fad6de75a4520f6f71d661f4b7a8139ce736/sagemaker-pipelines/tabular/abalone_build_train_deploy/sagemaker-pipelines-preprocess-train-evaluate-batch-transform.ipynb)

🎯 **Objetivo Principal**  
Transformar um **fluxo de Machine Learning (ML)** em um processo **automático e repetível** usando **AWS Step Functions**, integrando com SageMaker, CodeCommit, CodeBuild e CodePipeline.  
O fluxo gerencia desde o treino até o registro e retraining do modelo.

---

## ✅ Etapas e Funcionamento

### 🔹 1. Editar o Fluxo de Trabalho no Step Functions
- Fluxo inicial: **Treinar → Criar modelo → Criar configuração de endpoint → Criar endpoint**.  
- Novas etapas adicionadas com **Workflow Studio**:  
  - **Test if endpoint is in service** (função Lambda `EndpointWaitLambda`).  
  - **Test model** (função Lambda `ModelTestLambda`).  
- Executar o pipeline **TrainDeployModelPipeline** para validar a nova definição.

---

### 🔹 2. Registrar o Modelo no SageMaker Model Registry
- Nova etapa inserida no fluxo: **Register a model version** (Lambda `ModelRegistryLambda`).  
- Novo fluxo:  
  **Treinar → Criar modelo → Registrar versão → Criar config de endpoint → Criar endpoint → Testar endpoint → Testar modelo**.  
- Modelo registrado aparece no **SageMaker Studio → Model Registry**.  
- Aprovação manual para produção realizada no console.

---

### 🔹 3. Retraining Automático com Novos Dados
- Upload de dados adicionais no **S3** (`v1.0-retrain/`).  
- Evento do S3 dispara a **TrainingStateMachine** automaticamente.  
- Novo modelo treinado é registrado no **Model Registry**.

---

### 🔹 4. Atualizar Código do Modelo no CodeCommit
- Repositório `ModelCode` contém:  
  - `model_random.py` (modelo antigo).  
  - `model.py` (novo modelo aprimorado).  
- Alteração feita no `app.py` para usar `model.py`.  
- Commit dispara o **CodePipeline**, que gera nova imagem no **ECR** e treina o modelo atualizado.

---

### 🔹 5. Novo Treinamento com Dataset Atualizado
- Upload de nova versão de dados (`v1.1/`) no **S3**.  
- Step Functions dispara o fluxo novamente.  
- Nova versão registrada no **Model Registry**.  
- Resultado final: **4 versões do modelo** no grupo `abalone-model-group`.

---

## 🧠 Como tudo funciona junto

| Componente | Função |
|------------|--------|
| **Step Functions** | Orquestra o fluxo de ML (treino, registro, deploy e testes). |
| **Lambda Functions** | Executam checagens (endpoint ativo, teste de modelo, registro). |
| **S3** | Armazena datasets e artefatos de modelos. |
| **CodeCommit** | Versionamento do código de treino do modelo. |
| **CodeBuild** | Cria imagens Docker e prepara artefatos. |
| **ECR** | Repositório para imagens Docker. |
| **CodePipeline** | Automatiza build → treino → deploy. |
| **SageMaker** | Treina, hospeda endpoints e gerencia versões. |
| **Model Registry** | Registro central de modelos e metadados. |

---

## 🚀 Resultado Final
- Workflow expandido com **testes e registro de modelo**.  
- Modelos versionados no **SageMaker Model Registry**.  
- Retraining automático via **upload no S3**.  
- Atualização de código gerenciada via **CodeCommit + CodePipeline**.  
- Ambiente completo para **ML automatizado, seguro e escalável**.
