"""
Tarefa 2: fazer upload de um objeto no Amazon S3
Nesta tarefa, você conclui o script create-object.py que faz o upload do arquivo notes.csv
do seu disco local para o bucket criado na tarefa anterior. 
Esse arquivo contém notas de exemplo que você usa no desenvolvimento da sua aplicação. 
Você adiciona os metadados personalizados antes de fazer o upload do objeto para rastrear 
os arquivos de teste em seu bucket.

O arquivo create-object.py é processado na seguinte ordem pela função principal:

- Leia o arquivo config.ini e use as configurações para todos os valores estáticos.
- uploadObject faz upload de um arquivo no Amazon S3.
"""

import boto3, botocore, configparser

def main(s3Client):
    """
    Na função main() (principal), o script lê as variáveis do arquivo de configuração.
    Analise cada variável para ver o que está sendo atribuído. 
    Observe que o arquivo de configuração tem informações sobre o arquivo e as informações a serem atribuídas como metadados.
    A função uploadObject é passada para todas as variáveis que você coletou do arquivo .ini 
    para ser usada ao fazer upload do arquivo. O parâmetro de metadados espera que um objeto de 
    dicionário que você está criando seja passado para ele da configuração.
    """
    
    print('\nStart of create object script\n')
    ## Initialize variables for object creation

    print('Reading configuration file for bucket name...')
    config = readConfig()
    bucket_name = config['bucket_name']
    source_file_name = config["object_name"] + config['source_file_extension']
    key_name = config['key_name']+ config['source_file_extension']
    contentType = config['source_content_type']
    metaData_key = config['metaData_key']
    metaData_value = config['metaData_value']

    #### Create object in the s3 bucket
    print('Creating Object...')
    print(uploadObject(s3Client, bucket_name, source_file_name, key_name, contentType, {metaData_key: metaData_value}))
    
    print('\nEnd of create object script\n')

def uploadObject(s3Client, bucket, name, key, contentType, metadata={}):

    ## Start TODO 5: create a object by transferring the file to the S3 bucket, 
    ## set the contentType of the file and add any metadata passed to this function.
    
    response = s3Client.upload_file(
        Bucket=bucket, 
        Key=key,
        Filename=name,
        ExtraArgs={
            'ContentType': contentType,
            'Metadata': metadata
            }
    )    
    ## End TODO 5
    return "Finished creating object\n"
    
def readConfig():
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    return config['S3']

# Create an S3 client to interact with the service and pass 
# it to the main function that will create the buckets
client = boto3.client('s3')
try:
    main(client)
except botocore.exceptions.ClientError as err:
    print(err.response['Error']['Message'])
except botocore.exceptions.ParamValidationError as error:
    print(error)