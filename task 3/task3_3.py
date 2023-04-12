import json

with open('RomeoAndJuliet.json', 'r') as f:
    data = json.load(f)

characters = {}
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            if action["character"] not in characters:
                characters[action["character"]] = 1
            else:
                characters[action["character"]] += 1

max_lines = 0
ch_name = ""
for character in characters:
    if characters[character] >= max_lines:
        max_lines = characters[character]
        ch_name = character
print(ch_name)