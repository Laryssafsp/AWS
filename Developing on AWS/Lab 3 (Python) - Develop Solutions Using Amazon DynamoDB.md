# Laboratório 3: Python e Amazon DynamoDB

## Visão Geral
Este laboratório demonstra como usar o **AWS SDK para Python (Boto3)** para interagir com o **Amazon DynamoDB**.  
Você aprenderá a criar tabelas, inserir itens, consultar, atualizar e excluir dados usando código Python.

---

## Objetivos
- Criar e configurar uma tabela no DynamoDB usando Python.  
- Inserir e consultar itens.  
- Atualizar atributos.  
- Excluir itens.  
- Usar o Boto3 para manipular dados.  

---

## Ambiente do Laboratório
O **DynamoDB** é um banco de dados NoSQL totalmente gerenciado.  
- **Chave primária**: `year` (Partition Key) + `title` (Sort Key).  
- Os dados representam filmes com título, ano de lançamento e informações adicionais (classificação, elenco, etc).  

---

## Tarefa 1: Criar Tabela DynamoDB

### Código
```python
import boto3

# Conectar ao DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Criar tabela
table = dynamodb.create_table(
    TableName='Movies',
    KeySchema=[
        {'AttributeName': 'year', 'KeyType': 'HASH'},  # Partition key
        {'AttributeName': 'title', 'KeyType': 'RANGE'} # Sort key
    ],
    AttributeDefinitions=[
        {'AttributeName': 'year', 'AttributeType': 'N'},
        {'AttributeName': 'title', 'AttributeType': 'S'}
    ],
    ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
)

# Esperar a tabela ser criada
table.meta.client.get_waiter('table_exists').wait(TableName='Movies')
print("Tabela criada com sucesso:", table.table_status)
```

### Saída esperada
```
Tabela criada com sucesso: ACTIVE
```

---

## Tarefa 2: Inserir Itens

### Inserir um filme
```python
table = dynamodb.Table('Movies')

table.put_item(
   Item={
        'year': 2015,
        'title': "The Big New Movie",
        'info': {
            'plot': "Nothing happens at all.",
            'rating': 0
        }
    }
)
```

### Saída esperada
```
{'ResponseMetadata': {'HTTPStatusCode': 200, ...}}
```

---

## Tarefa 3: Ler Itens

### Obter um item específico
```python
response = table.get_item(
    Key={
        'year': 2015,
        'title': "The Big New Movie"
    }
)
item = response['Item']
print(item)
```

### Saída esperada
```json
{'year': 2015, 'title': 'The Big New Movie', 'info': {'plot': 'Nothing happens at all.', 'rating': 0}}
```

---

## Tarefa 4: Atualizar Itens

### Atualizar atributo `rating`
```python
table.update_item(
    Key={'year': 2015, 'title': "The Big New Movie"},
    UpdateExpression="set info.rating = :r",
    ExpressionAttributeValues={':r': 5},
    ReturnValues="UPDATED_NEW"
)
```

### Saída esperada
```json
{'Attributes': {'info': {'rating': 5}}}
```

---

## Tarefa 5: Excluir Itens

### Excluir um item
```python
table.delete_item(
    Key={
        'year': 2015,
        'title': "The Big New Movie"
    }
)
```

### Saída esperada
```
{'ResponseMetadata': {'HTTPStatusCode': 200, ...}}
```

---

## Conclusão
Você utilizou o **Boto3** para:  
- Criar uma tabela no DynamoDB.  
- Inserir e consultar itens.  
- Atualizar atributos específicos.  
- Excluir itens.  

Esse fluxo é a base para construir aplicações que usam o DynamoDB como banco de dados NoSQL.  

---

## Resumo das Ferramentas

| Ferramenta / Serviço      | Função no Lab |
|----------------------------|---------------|
| **Amazon DynamoDB**        | Banco NoSQL escalável para armazenar filmes |
| **Boto3 (AWS SDK Python)** | Biblioteca usada para interagir com o DynamoDB |
| **PutItem**                | Insere novos itens |
| **GetItem**                | Lê item específico por chave |
| **UpdateItem**             | Atualiza atributos de um item |
| **DeleteItem**             | Remove itens da tabela |

---

## Recursos Adicionais
- [Boto3 DynamoDB Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html)  
- [Amazon DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)  
