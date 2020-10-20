import requests
import json
import jsonpath

# VALIDACIÓN DE SCHEMA = https://python-jsonschema.readthedocs.io/en/stable/

# API URL
url = "https://reqres.in/api/users"

# Read json file
file = open('C:\\Users\\CocoNads\\Documents\\Environments\\my_env\\Files\\CreateUser.json','r')
json_input = file.read()
request_json = json.loads(json_input)

# Make POST request with json input body

response = requests.post(url,request_json)

assert response.status_code == 201
# print(response.headers)
# print(response.headers.get('Content-Length'))

response_json = json.loads(response.text)
id = jsonpath.jsonpath(response_json,'id')
print(id[0])