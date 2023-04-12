import csv

with open("stage3_test.csv", 'r') as f:
    reader = csv.reader(f, delimiter=',')

    with open('itp.csv', 'w') as f:
        writer = csv.writer(f)
        for row in reader:
            writer.writerow([row[0], row[2], row[4]])