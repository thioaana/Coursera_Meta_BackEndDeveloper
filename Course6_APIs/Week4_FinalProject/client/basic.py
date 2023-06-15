import requests

endpoint = "http://127.0.0.1:8000/api/menu-items/"
params = {'page':1}

get_response = requests.get(endpoint, params=params)

print(f"status-code : {get_response.status_code}\n")
print(get_response.headers)
print('\nData\n----')
for i in get_response.json()['results']:
    print(i)
