import json
import os

def log(message):
    print(os.environ['MINHA_VAR'])
    print(json.dumps(message))