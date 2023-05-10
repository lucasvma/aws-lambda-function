import json
from log import log

def lambda_handler(event, context):

    log('Log de execução. event: ' + json.dumps(event))

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
