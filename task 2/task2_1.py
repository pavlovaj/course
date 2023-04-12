import csv

with open('images.csv', 'w') as a:
    with open('stage3_test.csv', 'r') as b:
        reader = csv.DictReader(b, delimiter=',')
        headers = reader.fieldnames
        for row in reader:
            if len(row['Images'].split(',')) > 3:
                print(row['Images'])
                writer = csv.DictWriter(a, fieldnames=headers)
                writer.writerow(row)