# 🧪 Resumo do Funcionamento do Laboratório 3 (Integração com S3 e DynamoDB)

## 🎯 Objetivo Principal
Personalizar a aplicação **Employee Directory** para incluir **imagens de funcionários** (via Amazon S3) e **dados estruturados** (via Amazon DynamoDB).

---

## ✅ Etapas e Funcionamento

### 🔹 1. Visão Geral da Aplicação
- Aplicação hospedada em uma **sub-rede pública**.
- Inicialmente, **não acessa S3 nem DynamoDB**.
- Usa o perfil IAM: `EmployeeDirectoryAppRole`.
- Acessa-se pela URL: `PublicWebApplicationURL`.

> Mensagem esperada ao abrir a aplicação:
> ```
> S3: Employee Images bucket not found.
> DynamoDB: ‘Employees’ table not found.
> ```

---

### 🔹 2. Criação do Bucket Amazon S3
- Acessa o serviço **S3** no console.
- Cria um bucket com nome: `employee-photo-bucket-<INICIAIS>-<NÚMERO>`.
- Região: mesma do laboratório.
- Bloqueio de acesso público: **Ativado**.

> ✅ **Saída esperada:** Bucket criado com sucesso.

---

### 🔹 3. Criação da Política de Bucket
- Edita a política do bucket em **Permissões → Política do bucket**.
- Define permissão de leitura e escrita para a role `EmployeeDirectoryAppRole`.

> Substituir:
> - `INSERT-BUCKET-NAME` → nome do bucket.  
> - `INSERT-ACCOUNT-NUMBER` → ID da conta AWS.

> ✅ **Saída esperada:** Política aplicada com sucesso.

---

### 🔹 4. Configuração da Aplicação para usar o S3
- Acessa a aplicação → **Administration → Configuration**.
- Ativa:
  - `S3 Access Enabled`: **Sim**  
  - `S3 Bucket`: nome do bucket criado.
- Salva as alterações.

> ✅ **Saída esperada:** Bucket associado corretamente à aplicação.

---

### 🔹 5. Upload de Imagens para o S3
- Baixa e extrai arquivos do `PhotosZipURL`.
- Faz upload das imagens `.png` no bucket S3.
- Imagens aparecem na aplicação em **Employees → Images**.

> ✅ **Tarefa concluída:** Upload de imagens realizado com sucesso.

---

### 🔹 6. Criação da Tabela DynamoDB
- Acessa o serviço **DynamoDB** no console.
- Cria a tabela:
  - Nome: `Employees`
  - Chave de partição: `id` (tipo: String)

> ✅ **Saída esperada:** Tabela criada com sucesso.

---

### 🔹 7. Teste da Aplicação via Interface Web
- Em **Employees → Management → New Employee**:
  - Preenche `Name`, `Location`, `Email`
  - Seleciona uma foto
  - Clica em **Adicionar**

> ✅ **Saída esperada:** Novo registro criado na aplicação.

---

### 🔹 8. Gerenciamento de Itens no DynamoDB
- Acessa a tabela `Employees` → **Explorar itens da tabela**.
- Edita atributos como `location`, `email` ou `photo` (sem alterar o `id`).
- Confirma atualização refletida na aplicação.

> ✅ **Tarefa concluída:** Itens existentes gerenciados com sucesso.

---

### 🔹 9. Criação Manual de Itens via Console
- Em **Itens retornados → Criar item**:
  - Adiciona `id`, `name`, `location`, `email`, `photo`.
- Confirma criação e verifica na aplicação.

> ✅ **Tarefa concluída:** Itens adicionados com sucesso e refletidos na aplicação.

---

## 🧠 Como tudo funciona junto

| Componente                  | Função no sistema                                                     |
|-----------------------------|------------------------------------------------------------------------|
| **Amazon S3**               | Armazena as fotos dos funcionários.                                   |
| **Bucket Policy**           | Concede permissões de acesso à aplicação para acessar os arquivos.    |
| **Amazon DynamoDB**         | Armazena os dados estruturados dos funcionários.                      |
| **IAM Role**                | Controla o acesso seguro da aplicação aos recursos AWS.               |
| **Interface Web**           | Permite cadastrar, visualizar e gerenciar os funcionários.            |

---

## 🚀 Resultado Final

- A aplicação acessa corretamente os dados do **bucket S3** e da **tabela DynamoDB**.
- Imagens são carregadas e exibidas na interface.
- Novos funcionários podem ser criados e gerenciados via web.
- Todos os dados são persistidos nos serviços AWS com segurança e escalabilidade.
