# 🧪 Resumo do Funcionamento do Laboratório 1 (AWS IAM)

---

## 🎯 Objetivo Principal
Explorar usuários, grupos e políticas do AWS Identity and Access Management (IAM), adicionando usuários aos grupos corretos e testando suas permissões nos serviços Amazon S3 e Amazon EC2.

---

## ✅ Etapas e Funcionamento

### 🔹 1. Exploração Inicial do IAM
- Acessar o painel IAM no AWS Management Console.
- Visualizar os **três usuários**: `user-1`, `user-2`, `user-3`.
- Conferir os **três grupos** existentes: `S3-Support`, `EC2-Support`, `EC2-Admin`.
- Identificar as **políticas associadas**:
  - `AmazonS3ReadOnlyAccess` (S3-Support)
  - `AmazonEC2ReadOnlyAccess` (EC2-Support)
  - `EC2-Admin-Policy` (permissões em linha para visualizar, iniciar e parar instâncias).

---

### 🔹 2. Gerenciamento de Usuários e Grupos
Adicionar usuários aos grupos de acordo com o cenário de negócio:

| Usuário  | Grupo       | Permissões                                    |
|----------|-------------|-----------------------------------------------|
| user-1   | S3-Support  | Acesso somente leitura ao Amazon S3           |
| user-2   | EC2-Support | Acesso somente leitura ao Amazon EC2          |
| user-3   | EC2-Admin   | Visualizar, iniciar e interromper instâncias EC2 |

**Passos:**
1. No IAM, abrir **Grupos de usuários**.
2. Selecionar o grupo.
3. Na aba **Usuários**, clicar **Adicionar usuários**.
4. Marcar o usuário e confirmar.

---

### 🔹 3. Localização e Uso do URL de Login do IAM
- No painel do IAM, copiar o **URL de login** no formato: https://<ID_DA_CONTA>.signin.aws.amazon.com/console
- - Usar o link em **janela privada** para testar logins como cada usuário.

---

### 🔹 4. Teste de Permissões

**User-1 (S3-Support)**
- Pode listar buckets e visualizar objetos no S3.
- Ao tentar acessar EC2, recebe **erro de permissão**.

**User-2 (EC2-Support)**
- Pode visualizar instâncias EC2.
- Ao tentar parar uma instância, recebe **erro de permissão**.
- No S3, não enxerga nenhum bucket.

**User-3 (EC2-Admin)**
- Pode visualizar, iniciar e parar instâncias EC2.
- Teste de parar instância realizado com sucesso.

---

## 🧠 Como tudo funciona junto

| Componente          | Função no sistema                                                       |
|---------------------|-------------------------------------------------------------------------|
| **IAM Usuários**    | Identidades individuais com credenciais próprias.                       |
| **IAM Grupos**      | Conjunto de usuários que compartilham as mesmas permissões.              |
| **Políticas IAM**   | Definem o que usuários e grupos podem fazer na AWS.                      |
| **Amazon S3**       | Serviço de armazenamento de objetos, testado com acesso somente leitura. |
| **Amazon EC2**      | Serviço de computação, testado com diferentes níveis de acesso.          |
| **CloudWatch/ELB/AS**| Serviços incluídos em permissões de leitura para suporte EC2.            |

---

## 🚀 Resultado Final
- Usuários atribuídos corretamente aos grupos.
- Permissões funcionam conforme esperado:
- **S3-Support** → acesso somente ao S3
- **EC2-Support** → acesso somente ao EC2 (leitura)
- **EC2-Admin** → controle administrativo básico do EC2
- Ambiente pronto para uso seguro e controlado.

