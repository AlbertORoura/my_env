import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users?page=2"

response = requests.get(url)
print(response.elapsed)
#print(response.content)
#print(response.headers)

# Parse response to Json format
json_response = json.loads(response.text)
#print(json_response)

# Fetch value using Json path
pages = jsonpath.jsonpath(json_response,'total_pages')
#print(pages[0])
assert response.elapsed <= 2
assert response.status_code == 200
assert pages[0] == 2