import csv

with open("stage3_test.csv", 'r') as a:
    reader = csv.reader(a, delimiter=',')

    with open('itp.csv', 'w') as b:
        writer = csv.writer(b)
        for row in reader:
            writer.writerow([row[0], row[2], row[4]])