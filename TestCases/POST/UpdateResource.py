import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users"

# Read json file
file = open('C:\\Users\\CocoNads\\Documents\\Environments\\my_env\\Files\\UpdateUser.json','r')
json_input = file.read()
request_json = json.loads(json_input)

# Make POST request with json input body

response = requests.put(url,request_json)

assert response.status_code == 200
# print(response.headers)
# print(response.headers.get('Content-Length'))

response_json = json.loads(response.text)
# id = jsonpath.jsonpath(response_json,'id')
print(response_json)