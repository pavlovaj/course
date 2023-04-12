import json

with open('RomeoAndJuliet.json', 'r') as f:
    data = json.load(f)

data1 = []
for act in data["acts"]:
    for scene in act["scenes"]:
        characters = set()
        for action in scene["action"]:
            characters.add(action["character"])
        data1.append(list(characters))

with open('result2.json', 'w') as g:
    for line in data:
        g.write(json.dumps(line, ensure_ascii=False, separators=(',', ':')))
        g.write("\n")
