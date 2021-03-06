import requests


payload = {'key1': 'value1', 'key2': 'value2'}

# GET
#r = requests.get('http://httpbin.org/get', params=payload)

# POST
# r = requests.post('http://httpbin.org/post', params=payload)

# PUT
#r = requests.put('http://httpbin.org/put', params=payload)

# DELETE
# r = requests.delete('http://httpbin.org/delete', params=payload)

r = requests.get('http://httpbin.org/get', params=payload, timeout=1)

print(r.status_code)
print(r.text)
print(r.json())