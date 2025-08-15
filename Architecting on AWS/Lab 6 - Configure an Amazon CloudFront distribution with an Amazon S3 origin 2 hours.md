## Lab 6 - Configure an Amazon CloudFront distribution with an Amazon S3 origin
This lab provides you with an overview of creating Amazon S3 buckets and adding them as an origin to Amazon CloudFront distributions

# Laboratório 6 – Proteger Bucket com CloudFront e Controle de Acesso de Origem

## Resumo

Neste laboratório, você irá proteger um bucket do Amazon S3 para que os objetos sejam acessíveis apenas através de uma distribuição do Amazon CloudFront. Será configurado um **Origin Access Control (OAC)**, comportamentos de cache específicos e, opcionalmente, replicação entre regiões.

Objetivos:

* Atualizar a política de bucket S3 para permitir acesso apenas pelo CloudFront.
* Ativar bloqueio de acesso público.
* Criar uma origem no CloudFront vinculada ao bucket.
* Configurar comportamento de cache para tipos de arquivos específicos.
* Testar acesso direto ao bucket e via CloudFront.
* Opcional: replicação entre regiões.

---

## Tarefa 5.1 – Atualizar a política do bucket (LabBucket)

**Objetivo:** Permitir leitura apenas da distribuição do CloudFront.

**Passos:**

1. Acesse **S3 → LabBucket → Permissões → Política do bucket → Editar**.
2. Copie o ARN do bucket (`arn:aws:s3:::LabBucket`) para uso posterior.
3. Cole o JSON abaixo, substituindo:

   * `RESOURCE_ARN` → ARN do bucket + `/*`
   * `CLOUDFRONT_DISTRIBUTION_ARN` → ARN da distribuição CloudFront

```json
{
    "Version": "2012-10-17",
    "Statement": {
        "Sid": "AllowCloudFrontServicePrincipalReadOnly",
        "Effect": "Allow",
        "Principal": {
            "Service": "cloudfront.amazonaws.com"
        },
        "Action": [
            "s3:GetObject",
            "s3:GetObjectVersion"
        ],
        "Resource": "RESOURCE_ARN",
        "Condition": {
            "StringEquals": {
                "AWS:SourceArn": "CLOUDFRONT_DISTRIBUTION_ARN"
            }
        }
    }
}
```

4. Salve as alterações.

---

## Tarefa 5.2 – Ativar bloqueio de acesso público

**Objetivo:** Garantir que o bucket não seja acessível publicamente.

**Passos:**

1. Na guia **Permissões → Bloquear acesso público → Editar**.
2. Selecione **Bloquear todo o acesso público**.
3. Confirme digitando `confirm` e salve.

---

## Tarefa 5.3 – Criar nova origem com OAC

**Objetivo:** Adicionar LabBucket como origem do CloudFront.

**Passos:**

1. Acesse **CloudFront → Distribuições → \[ID da Distribuição] → Origens → Create origin**.
2. Selecione LabBucket como **Origin domain**.
3. Nome: `My Amazon S3 Origin`
4. Em **Origin access**, selecione **Origin access control settings → Create new OAC**.
5. Salve a origem.

---

## Tarefa 5.4 – Criar comportamento para a origem S3

**Objetivo:** Configurar padrões de cache e tipos de arquivos que podem ser acessados.

**Passos:**

1. Guia **Comportamentos → Create behavior**.
2. Path pattern: `CachedObjects/*.png`
3. Origin: `My Amazon S3 Origin`
4. Cache Policy: `CachingOptimized`
5. Salve o comportamento.

---

## Tarefa 6 – Testar acesso direto e via CloudFront

1. Teste acesso direto: abra URL do objeto no S3 → deve retornar **Acesso negado**.
2. Teste via CloudFront: abra URL da distribuição + `/CachedObjects/logo.png` → objeto carregado com sucesso.

---

## Tarefa opcional 8 – Replicação entre regiões

**Resumo:** Configura o bucket LabBucket para replicar automaticamente objetos para outro bucket em outra região.

**Passos principais:**

1. Ativar versionamento em LabBucket.
2. Criar bucket de destino (DestinationBucket) em outra região e ativar versionamento.
3. Criar política pública de leitura no DestinationBucket (para fins de teste).
4. Criar regra de replicação no LabBucket apontando para DestinationBucket.
5. Testar upload de novo objeto e verificar replicação (`Status` deve mudar de `PENDING` para `REPLICA`).

**Exemplo JSON para política pública no DestinationBucket:**

```json
{
    "Version": "2012-10-17",
    "Id": "Policy1621958846486",
    "Statement": [
        {
            "Sid": "OriginalPublicReadPolicy",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::DestinationBucket/*"
        }
    ]
}
```

---

## Conclusão

* Bucket S3 protegido, acessível apenas via CloudFront.
* OAC configurado para controlar o acesso.
* Comportamento de cache definido para tipos de arquivos específicos.
* Replicação opcional entre regiões configurada e testada.
* Políticas de acesso aplicadas corretamente.

---

## Anexos

* **ARN do LabBucket**: `arn:aws:s3:::LabBucket`
* **ARN da distribuição CloudFront**: `arn:aws:cloudfront::123456789:distribution/EVTAORMSUBNP5`
* **Nome do DestinationBucket**: `DestinationBucket`
* **Policy JSON para CloudFront**: incluído nas tarefas 5.1 e 8.3
