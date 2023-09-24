import json

data = {
     'name' : 'John Doe',
     'age' : 30,
     'occupation' : 'Sostware Engineer'

}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)