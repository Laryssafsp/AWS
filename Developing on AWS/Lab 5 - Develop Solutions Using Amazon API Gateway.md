# Lab 5 - Develop Solutions Using Amazon API Gateway
In this lab, you will create an Amazon API Gateway resource for your application.

**Diagrama:** Descrição da imagem: o diagrama anterior mostra várias funções do AWS Lambda configuradas para funcionarem com o Amazon Polly e uma tabela chamada Notes, tudo acessado por um Amazon API Gateway.


# Laboratório 5: Desenvolver Soluções usando o Amazon API Gateway

## Visão Geral
Agora que o back-end principal já está configurado (armazenamento, banco de dados e processamento com Lambda), precisamos de uma forma para que os usuários acessem as funções do **AWS Lambda** pela Internet.

Neste laboratório você irá:
- Criar uma API REST no **Amazon API Gateway**
- Conectar essa API a funções Lambda
- Configurar CORS
- Usar modelos de mapeamento para validação e transformação
- Implantar a API em um estágio e validar o endpoint

---

## Objetivos
- Criar recursos da API RESTful e configurar o CORS.
- Integrar métodos de API a funções Lambda para processar dados.
- Configurar modelos de mapeamento para transformar dados de entrada/saída.
- Criar modelo de solicitação para validar dados.
- Implantar a API e testar via endpoint.

---

## Tarefa 1: Criar API REST e Recurso

### Passos principais:
1. Criar API REST regional chamada **PollyNotesAPI**.
2. Criar recurso `/notes` com CORS habilitado.

**Explicação:**  
- **API REST** no API Gateway é um conjunto de recursos e métodos que podem ser integrados a Lambdas ou outros serviços.  
- O **CORS** permite que aplicações em domínios diferentes acessem a API.  

---

## Tarefa 2: Configurar Método GET e Modelos de Mapeamento

### 2.1 Configurar GET → Lambda list-function
- Criar método **GET** em `/notes`
- Integrar com função Lambda `list-function`
- Testar retorno de notas (Status 200, JSON com itens do DynamoDB)

### 2.2 Atualizar Solicitação de Integração
Adicionar mapeamento para enviar `UserId` fixo:

```json
{"UserId":"student"}
```

### 2.3 Limitar dados de resposta (Resposta de Integração)
Exemplo de modelo de resposta em **Velocity Template Language (VTL):**

```vtl
#set($inputRoot = $input.path('$'))
[
    #foreach($elem in $inputRoot)
    {
        "NoteId" : "$elem.NoteId",
        "Note" : "$elem.Note"
    } 
    #if($foreach.hasNext),#end
    #end
]
```

**Explicação:**  
- **Solicitação de integração**: transforma entrada antes de ir ao backend.  
- **Resposta de integração**: transforma saída antes de retornar ao cliente.  
- Usando VTL conseguimos manipular JSON de entrada/saída.  

---

## Tarefa 3: Configurar Método POST com Validação

### 3.1 Criar método POST → Lambda createUpdate-function
Exemplo de corpo de requisição para teste:

```json
{
    "Note": "This is your new note added using the POST method",
    "NoteId": 3,
    "UserId": "student"
}
```

### 3.2 Criar modelo de validação (NoteModel)
Exemplo de esquema JSON:

```json
{
    "title": "Note",
    "type": "object",
    "properties": {
        "UserId": {"type": "string"},
        "NoteId": {"type": "integer"},
        "Note": {"type": "string"}
    },
    "required": ["UserId", "NoteId", "Note"]
}
```

### 3.3 Testar Validador
Exemplo inválido (erro 400):
```json
{
    "Note": "This is invalid",
    "UserId": "student",
    "id": 3
}
```

Exemplo válido (sucesso):
```json
{
    "Note": "This is your updated note using the Model validation",
    "UserId": "student",
    "NoteId": 3
}
```

**Explicação:**  
- O **modelo de validação** garante que apenas dados no formato correto sejam enviados ao Lambda.  
- Reduz erros e melhora segurança.  

---

## Tarefa 4: Configurar CORS e Implantar API

### 4.1 Habilitar CORS
- Ativar CORS em `/notes`
- Métodos permitidos: **GET, POST, OPTIONS**
- Incluir cabeçalhos de resposta para 4XX e 5XX

### 4.2 Implantar API
- Criar estágio **Prod**
- Implantar API
- Copiar **Invoke URL** e testar `/notes`

### Saída esperada (JSON):
```json
[
    {
        "NoteId" : "1",
        "Note" : "DynamoDB is NoSQL"
    },
    {
        "NoteId" : "2",
        "Note" : "A DynamoDB table is schemaless"
    },
    {
        "NoteId" : "3",
        "Note" : "This is your updated note using the Model validation"
    }
]
```

---

## Conclusão
- Criamos API REST com recurso `/notes`.
- Configuramos GET e POST para funções Lambda.
- Usamos modelos de mapeamento para transformar entrada/saída.
- Validamos payloads com modelo JSON.
- Implantamos API com CORS ativado.

---

## Resumo das Ferramentas

| Ferramenta              | Função no Lab |
|--------------------------|---------------|
| **Amazon API Gateway**   | Criação da API REST, métodos, CORS |
| **AWS Lambda**           | Backend da aplicação (list-function, createUpdate-function) |
| **Amazon DynamoDB**      | Armazena as notas da aplicação |
| **Velocity Template Language (VTL)** | Usada para transformação de entrada/saída nos modelos de mapeamento |
| **CORS**                 | Permite que diferentes origens (front-end em S3, API no API Gateway) se comuniquem |
| **Validação de Modelos** | Garante integridade dos dados enviados pelo cliente |

---

## Recursos Adicionais
- [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
- [Velocity Template Language (VTL)](https://velocity.apache.org/engine/1.7/user-guide.html)
- [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/CORS)
