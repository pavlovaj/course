import collections
import json

with open('RomeoAndJuliet.json', 'r') as f:
    data = json.load(f)

d = collections.defaultdict(list)
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            for line in action["says"]:
                d[action["character"]].append(line)

print(d)