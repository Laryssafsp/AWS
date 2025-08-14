# Laboratório 1: Introduction to AWS Identity and Access Management

© 2025 Amazon Web Services, Inc. ou suas afiliadas. Todos os direitos reservados.  
Este trabalho não pode ser reproduzido ou redistribuído, no todo ou em parte, sem a permissão prévia por escrito da Amazon Web Services, Inc.  
É proibido copiar, emprestar ou vender para fins comerciais. Todas as marcas comerciais pertencem a seus proprietários.

> **Observação:** não inclua nenhuma informação pessoal, de identificação ou confidencial no ambiente do laboratório.  
> As informações inseridas podem estar visíveis para outras pessoas.

Correções, feedback ou dúvidas? Entre em contato com **AWS Training and Certification**.

---

## Visão Geral do Laboratório

Este laboratório provisiona os seguintes recursos do IAM para exploração:

- **Usuários:** `user-1`, `user-2`, `user-3`
- **Grupos e políticas:**
  - **Suporte do S3:** acesso *Read-Only* ao Amazon S3
  - **Suporte do EC2:** acesso *Read-Only* ao Amazon EC2
  - **Administrador do EC2:** acesso para *View*, *Start* e *Stop* de instâncias EC2

---

## Recursos do IAM

Durante o laboratório, mensagens de erro podem aparecer se ações além das previstas forem tentadas.  
O IAM limita o acesso apenas aos serviços autorizados.  
Esses erros **não** afetam a conclusão do laboratório.

---

## Objetivos

Ao final do laboratório, você será capaz de:

1. Explorar usuários e grupos do IAM
2. Inspecionar políticas aplicadas a grupos
3. Adicionar usuários a grupos e explorar permissões
4. Localizar e usar o **URL de login** do IAM
5. Testar políticas e acesso a serviços

---

## Pré-requisitos

- Notebook com Wi-Fi e **Windows, macOS ou Linux** (tablets não suportados)
- Acesso administrativo (Windows)
- Navegador: **Chrome**, **Firefox** ou **Edge**

---

## Lista de Ícones

- 💻 **Saída esperada:** exemplo para validação de comandos/arquivos  
- ℹ️ **Observação:** dicas ou orientações  
- ✅ **Tarefa concluída:** resumo da etapa finalizada

---

## Início do Laboratório

1. Clique em **Start Lab**
2. Aguarde a provisão dos serviços
3. Clique em **Open Console** para abrir o AWS Management Console

> **Importante:** não altere a **Região** a menos que seja instruído.

---

## Erros Comuns de Login

### Erro: "You must first log out..."
- Clique no link **click here**
- Feche a guia aberta
- Volte ao início e clique **Open Console** novamente

### Erro: Start Lab não inicia
- Desative bloqueador de pop-ups ou scripts
- Adicione o domínio do laboratório à lista de permissões
- Atualize a página e tente novamente

---

## Tarefa 1: Explorar os Recursos do IAM

### Tarefa 1.1: Explorar Usuários, Grupos e Políticas
1. No Console da AWS, procure por **IAM**
2. Vá em **Usuários** → selecione `user-1`
3. Veja as abas **Permissões**, **Grupos** e **Credenciais de Segurança**
4. Vá em **Grupos de usuários**:
   - **EC2-Support** → política `AmazonEC2ReadOnlyAccess`
   - **S3-Support** → política `AmazonS3ReadOnlyAccess`
   - **EC2-Admin** → política em linha `EC2-Admin-Policy`

**Estrutura de uma política IAM:**
- **Effect:** *Allow* ou *Deny*
- **Action:** API calls permitidas
- **Resource:** escopo dos recursos permitidos

---

### Tarefa 1.2: Gerenciar Usuários e Grupos

**Cenário de Negócio:**
| Usuário | Grupo       | Permissões |
|---------|------------|------------|
| user-1  | S3-Support | Somente leitura no Amazon S3 |
| user-2  | EC2-Support| Somente leitura no Amazon EC2 |
| user-3  | EC2-Admin  | Visualizar, iniciar e parar instâncias EC2 |

**Passos para adicionar usuários a grupos:**
1. Vá em **Grupos de usuários**
2. Selecione o grupo desejado
3. Aba **Usuários** → **Adicionar usuários**
4. Selecione o usuário → **Adicionar usuários**
5. Confirmar inclusão

✅ **Tarefa concluída:** usuários adicionados aos grupos corretos.

---

## Tarefa 2: Usar o URL de Login do IAM

### Tarefa 2.1: Localizar o URL
- No painel do IAM, localize o **URL de login** no formato:
https://123456789012.signin.aws.amazon.com/console

- Copie e salve para logins futuros.

---

### Tarefa 2.2: Testar Logins com Diferentes Usuários

**Login user-1 (S3-Support):**
- Acesso ao S3: permitido listar buckets e conteúdos
- Acesso ao EC2: **erro de permissão**

**Login user-2 (EC2-Support):**
- EC2: visualizar instâncias (somente leitura)
- Tentativa de parar instância → **erro de permissão**
- S3: sem acesso

**Login user-3 (EC2-Admin):**
- EC2: pode visualizar e parar instâncias
- Teste realizado com sucesso

✅ **Tarefa concluída:** nível de acesso testado com cada usuário.

---

## Conclusão

Você concluiu com sucesso:
- Exploração de usuários e grupos do IAM
- Inspeção de políticas aplicadas
- Inclusão de usuários em grupos
- Uso do URL de login do IAM
- Teste de permissões

---

## Finalizar Laboratório

1. Retorne ao Console da AWS
2. Clique no nome do usuário (AWSLabsUser) → **Sign Out**
3. Clique em **End Lab** e confirme
