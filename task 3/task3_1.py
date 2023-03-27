import json

dictionary = {}
for line in open('wikidata_1000.json', 'r'):
    line = json.loads(line)
    key = line["label"]['value']
    try:
        value = line["description"]['value']
    except:
        value = 'None'
    dictionary[key] = value

with open('result1.json', 'w') as j:
    json.dump(dictionary, j, sort_keys=False, ensure_ascii=False, indent=4, separators=(',', ':'))