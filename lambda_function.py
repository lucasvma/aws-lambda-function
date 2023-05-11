import boto3
from log import log
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    s3_client = boto3.client('s3')

    record = event['Records'][0]

    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']

    try:
        get_object_result = s3_client.get_object(Bucket=bucket, Key=key)

        print('get_object_result {}', get_object_result)

        mega_byte = 1024 * 1024

        if get_object_result['ContentLength'] > 1 * mega_byte:
            log('Objeto muito grande')

            return 'Objeto muito grande'

        log('Objeto de tamanho OK')

        return 'Objeto de tamanho OK'
    except ClientError as e:
        print(f'Error retrievent S3 object: {e}')
        return None
