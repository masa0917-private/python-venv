import json

j = {
    "employee":[
        {"id": 111, "name": "Mike"},
        {"id": 222, "name": "Nancy"}
    ]
}

print(j)
print("#######")
a=json.dumps(j)
print("@@@@@@@@")
print(json.loads(a))

print(json.dumps(j))

with open('text.json', 'w') as f:
    json.dump(j, f)

print("#######")
with open('text.json', 'r') as f:
    print(json.load(f))