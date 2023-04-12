import collections
import csv

with open('result1.csv', 'w') as f:
    writer = csv.writer(f)
    with open('stage3_test.csv', 'r') as g:
        reader = csv.DictReader(g, delimiter=',')
        d = {}
        for row in reader:
            d[row["Id"]] = float(row["Price"])
        od = collections.OrderedDict(sorted(d.items(), key=lambda t: t[1]))
        for item in od:
            writer.writerow([item, od[item]])
with open('result2.csv', 'w') as q:
    writer = csv.writer(q)
    od1 = collections.OrderedDict(sorted(d.items(), key=lambda t: t[1], reverse=True))
    for item in od1:
        writer.writerow([item, od1[item]])