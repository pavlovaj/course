import collections
import json

with open('RomeoAndJuliet.json', 'r') as f:
    data = json.load(f)
lines = list()
cnt = collections.Counter()
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            for line in action["says"]:
                for word in line.split(' '):
                    cnt[word] += 1

word_list = [word for line in cnt for word in line.split()]
c = list(word_list)
print(cnt.most_common(20), cnt.most_common()[-21::])