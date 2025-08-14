# Laboratório 3: Configurar uma Aplicação Web para usar um Bucket Amazon S3 e Tabela DynamoDB

© 2025 Amazon Web Services, Inc. Todos os direitos reservados.

> **Observação:** Não inclua informações pessoais ou confidenciais no ambiente do laboratório.

---

## Visão Geral

Neste laboratório, você personalizará a aplicação de diretório de funcionários para incluir imagens e informações de funcionários usando Amazon S3 e Amazon DynamoDB.  

As etapas incluem:  
- Criar e configurar um bucket S3.  
- Fazer upload de objetos (imagens).  
- Configurar a aplicação para usar o bucket S3.  
- Criar uma tabela DynamoDB.  
- Testar a aplicação e gerenciar itens na tabela.

---

## Objetivos

Ao final deste laboratório, você será capaz de:

1. Criar um bucket do Amazon S3.  
2. Criar uma política de bucket S3.  
3. Modificar uma aplicação para usar um bucket do S3.  
4. Fazer upload de objetos no S3.  
5. Criar uma tabela do Amazon DynamoDB.  
6. Testar a aplicação usando a interface web.  
7. Gerenciar itens existentes do DynamoDB via Console AWS.  
8. Criar itens no DynamoDB via Console AWS.

---

## Pré-requisitos

- Notebook com Wi-Fi e Windows, macOS ou Linux.  
- Acesso de administrador.  
- Navegador atualizado (Chrome, Firefox ou Edge).  

> **Observação:** Tablets não são suportados para execução do laboratório.

---

## Lista de Ícones

- **Saída esperada:** Exemplo para verificar resultado de comandos ou arquivos.  
- **Observação:** Dica ou orientação importante.  
- **Atenção:** Informação importante que pode impactar o laboratório.  
- **Copiar e editar:** Comando ou script que deve ser copiado para edição.  
- **Tarefa concluída:** Resumo da conclusão de uma tarefa.

---

## Iniciar Laboratório

1. Selecione **Start Lab** no topo da página.  
2. Aguarde a provisão dos serviços AWS.  
3. Selecione **Open Console** para abrir o AWS Management Console.

> **Não altere a Região, a menos que instruam.**

---

## Tarefas do Laboratório

### Tarefa 1: Visão Geral da Aplicação Web

- A aplicação é executada na sub-rede pública 1.  
- Atualmente, não há acesso ao S3 nem à tabela DynamoDB.  
- A aplicação usa o perfil IAM `EmployeeDirectoryAppRole`.

Para acessar a aplicação:

1. Copie `PublicWebApplicationURL`.  
2. Cole em uma nova guia do navegador.  

> Mensagem inicial:
> ```
> S3: Employee Images bucket not found.
> DynamoDB: ‘Employees’ table not found.
> ```

---

### Tarefa 2: Criar um Bucket Amazon S3

1. No AWS Console, pesquise e abra **S3**.  
2. Clique em **Criar bucket** e configure:  
   - Nome do bucket: `employee-photo-bucket-<INITIALS>-<NUMBER>`  
   - Região: mesma do laboratório  
   - Bloquear todo acesso público: **Ativado**  
3. Clique em **Criar bucket**.  

> **Saída esperada:** Bucket criado com sucesso.

---

### Tarefa 3: Criar uma Política de Bucket S3

1. Acesse o bucket criado.  
2. Guia **Permissões** → **Política do bucket** → **Editar**.  
3. Cole a política abaixo, substituindo os espaços reservados:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3ReadAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::INSERT-ACCOUNT-NUMBER:role/EmployeeDirectoryAppRole"
      },
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::INSERT-BUCKET-NAME",
        "arn:aws:s3:::INSERT-BUCKET-NAME/*"
      ]
    }
  ]
}
```
## Tarefa 3: Criar uma Política de Bucket S3

- Substitua `INSERT-BUCKET-NAME` pelo nome do seu bucket.  
- Substitua `INSERT-ACCOUNT-NUMBER` pelo seu AWS Account ID.  
- Salve alterações.  

> **Saída esperada:** Política aplicada com sucesso.

---

## Tarefa 4: Modificar a Aplicação para usar o Bucket S3

1. Acesse a aplicação Employee Directory.  
2. Em **Administration → Configuration**, altere:  
   - **S3 Access Enabled:** Ativado  
   - **S3 Bucket:** Nome do bucket criado  
3. Clique em **Salvar**.  

> **Saída esperada:** Bucket associado corretamente à aplicação.

---

## Tarefa 5: Fazer Upload de Objetos para o S3

1. Baixe o arquivo `PhotosZipURL` e extraia localmente.  
2. No bucket S3, vá em **Objetos → Fazer upload → Adicionar arquivos**.  
3. Selecione todas as imagens `.png` e clique em **Fazer upload**.  
4. Na aplicação, em **Employees → Images**, as imagens devem aparecer.  

> **Tarefa concluída:** Upload de imagens realizado com sucesso.

---

## Tarefa 6: Criar Tabela Amazon DynamoDB

1. Pesquise e abra **DynamoDB** no console.  
2. Clique em **Criar tabela**:  
   - Nome: `Employees`  
   - Chave de partição: `id` (String)  
3. Clique em **Criar tabela**.  

> **Saída esperada:** Tabela criada com sucesso.

---

## Tarefa 7: Testar Aplicação via Interface Web

1. Atualize a página da aplicação.  
2. Em **Employees → Management → New Employee**, insira:  
   - `Name`, `Location`, `Email`  
   - Selecione uma `Photo`  
3. Clique em **Adicionar**.  

> **Saída esperada:** Novo registro criado na aplicação.

---

## Tarefa 8: Gerenciar Itens no DynamoDB via Console AWS

1. Abra a tabela `Employees` no DynamoDB.  
2. Clique em **Explorar itens da tabela**.  
3. Selecione um item e clique em **Editar** (não altere `id`).  
4. Atualize atributos como `location`, `email` ou `photo` e salve.  
5. Verifique na aplicação que as alterações aparecem.  

> **Tarefa concluída:** Itens existentes gerenciados com sucesso.

---

## Tarefa 9: Criar Itens no DynamoDB via Console AWS

1. Em **Itens retornados → Criar item**, use a visualização **Formulário**.  
2. Adicione atributos:  
   - `id` (único)  
   - `name`, `location`, `email`, `photo` (vazia)  
3. Clique em **Criar item**.  
4. Atualize a aplicação para verificar os novos itens.  

> **Tarefa concluída:** Itens adicionados com sucesso e refletidos na aplicação.

---

## Conclusão

Você concluiu com êxito:

- Criou um bucket Amazon S3.  
- Criou e aplicou uma política de bucket.  
- Configurou a aplicação para usar o bucket S3.  
- Fez upload de objetos no S3.  
- Criou uma tabela DynamoDB.  
- Testou a aplicação usando a interface web.  
- Gerenciou itens existentes e criou novos itens no DynamoDB.

