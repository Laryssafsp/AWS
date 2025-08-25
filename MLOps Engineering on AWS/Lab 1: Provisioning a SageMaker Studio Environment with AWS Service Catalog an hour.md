# Lab 1: Provisioning a SageMaker Studio Environment with AWS Service Catalog an hour
This lab provides you with a basic overview to setup Amazon SageMaker Studio using AWS Service Catalog and also gives an overview of SageMaker Studio UI navigation.

[Github](https://github.com/Laryssafsp/AWS/blob/main/MLOps%20Engineering%20on%20AWS/Lab_1_files/lab_1.ipynb)

# 🧪 Resumo do Funcionamento do Laboratório 1 (SageMaker Studio com Service Catalog)

## 🎯 Objetivo Principal
Provisionar um ambiente do **Amazon SageMaker Studio** utilizando o **AWS Service Catalog**, garantindo que os recursos sejam criados de forma padronizada e com os devidos controles de acesso.

---

## ✅ Etapas e Funcionamento

### 🔹 1. Acesso ao AWS Service Catalog
- Abrir o console da AWS e acessar o **Service Catalog**.
- Selecionar o portfólio que contém o produto **SageMaker Studio**.
- O portfólio foi configurado previamente pelo administrador com políticas de conformidade.

### 🔹 2. Provisionamento do Produto
- Escolher o produto **SageMaker Studio Domain** no catálogo.
- Preencher os parâmetros obrigatórios:
  - Nome do domínio do SageMaker Studio.
  - Sub-redes e VPC onde o domínio será provisionado.
  - Papéis do IAM para execução (execution role).

### 🔹 3. Configuração do Domínio SageMaker Studio
- O **Service Catalog** cria o domínio do SageMaker Studio com as configurações padronizadas.
- Permite o gerenciamento centralizado dos recursos provisionados.
- Garante que as permissões de rede, segurança e papéis IAM estejam corretos.

### 🔹 4. Criação do Usuário no SageMaker Studio
- Dentro do domínio, criar perfis de usuário (por exemplo, `student`).
- Cada usuário possui um **execution role** vinculado para executar notebooks e jobs de ML.

### 🔹 5. Acesso ao SageMaker Studio
- O usuário acessa o **SageMaker Studio** pelo console.
- O ambiente de desenvolvimento já está pronto para uso com notebooks Jupyter.
- O Service Catalog garante que o ambiente esteja conforme os padrões da organização.

---

## 🧠 Como tudo funciona junto

| Componente                | Função no Sistema                                                                 |
|----------------------------|----------------------------------------------------------------------------------|
| **AWS Service Catalog**    | Fornece produtos padronizados e com conformidade definidos pelo administrador.    |
| **SageMaker Studio**       | Ambiente integrado para desenvolvimento de ML.                                   |
| **IAM Roles**              | Controlam permissões de execução e acesso aos serviços da AWS.                   |
| **VPC/Subnets**            | Definem a rede onde o ambiente do SageMaker será provisionado.                   |
| **User Profiles**          | Permitem múltiplos usuários acessarem o mesmo domínio com diferentes permissões. |

---

## 🚀 Resultado Final
- O domínio do **SageMaker Studio** é criado de forma padronizada via **Service Catalog**.  
- Usuários podem acessar o ambiente com segurança e começar a desenvolver projetos de ML.  
- Administradores garantem conformidade e governança dos recursos provisionados.

- [AWS::SageMaker::Domain](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html)
- [AWS::SageMaker::UserProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html)
- [AWS::SageMaker::Space](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-space.html)
- [O que é o Amazon SageMaker?]([O que é o Amazon SageMaker?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html))
- [Amazon SageMaker Features](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis-features-alpha.html)
