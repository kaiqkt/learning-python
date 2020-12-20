import json

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25
    },
    'Pessoa 2': {
        'nome': 'Luiz',
        'idade': 25
    },
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)

with open('abc.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)

for k, v in d1_json.items():
    print(k)
    for k, v in v.items():
        print(k, v)