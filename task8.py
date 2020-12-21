import json
with open('data.json', 'w') as file:
    file.write('\n\n\n{"a":\n\n\n{"b"\n: 1}}')
with open('data.json', 'r') as file:
    dict = json.load(file)
    innerdict = dict['a']
    innerdict['b'] = 2
    print(dict)