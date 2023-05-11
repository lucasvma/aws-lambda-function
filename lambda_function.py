import boto3
from log import log


def lambda_handler(event, context):
    s3 = boto3.client('s3')

    record = event['Records'][0]

    bucket = record.s3.bucket.name
    key = record.s3.object.key

    get_object_result = s3.get_object(Bucket=bucket, Key=key)

    mega_byte = 1024 * 1024

    if get_object_result['ContentLength'] > 1 * mega_byte:
        log('Objeto muito grande')

        return 'Objeto muito grande'

    log('Objeto de tamanho OK')

    return 'Objeto de tamanho OK'
