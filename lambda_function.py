import json
from log import log

def lambda_handler(event, context):

    log('Event: ' + json.dumps(event))

    return {
        'statusCode': 200,
        'body': '<html><body>Dados da requisicao {}</body></hmtl>'.format(json.dumps(event)),
        'headers': {
            "content-type": "text/html"
        }
    }
