import csv

with open('images.csv', 'w') as f1:
    with open('stage3_test.csv', 'r') as f2:
        reader = csv.DictReader(f1, delimiter=',')
        headers = reader.fieldnames
        for row in reader:
            if len(row['Images'].split(',')) > 3:
                writer.writerow(row)

