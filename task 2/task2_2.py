import csv

with open("stage3_test.csv", 'r') as a:
    reader = csv.reader(a, delimiter=',')
    headers = next(reader, None)
    with open('cost.csv', 'w') as b:

        writer = csv.writer(b, delimiter=',')
        if headers:
            writer.writerow(headers)
        for row in reader:

            if 10000 < float(row[-1]) <= 50000:
                writer.writerow(row)