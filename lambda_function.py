import boto3
import json
from log import log

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    record = event.Records[0]

    Bucket = record.s3.bucket.name
    Key = record.s3.object.key

    getObjectResult = s3.get_object(Bucket, Key)

    mega_byte = 1024 * 1024

    if (getObjectResult.ContentLength > 1 * mega_byte):
        log('Objeto muito grande')
        
        return 'Objeto muito grande'

    log('Objeto de tamanho OK')

    return 'Objeto de tamanho OK'
