import requests
import json
import os
from requests.auth import HTTPBasicAuth

url='localhost:8332'
username='barisser'
password='2bf763d2132a2ccf3ea38077f79196ebd600f4a29aa3b1afd96feec2e7d80beb3d9e13d02d56de0f'

def connect(method,body):
  node_url='http://'+url#+':'+node_port
  headers={'content-type':'application/json'}
  payload=json.dumps({'method':method,'params':body})
  result=requests.get(node_url,headers=headers,data=payload, verify=False, auth=HTTPBasicAuth(username, password))

  response=json.loads(result.content)
  return response['result']
