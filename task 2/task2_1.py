import csv

with open('new_table.csv', 'w', encoding='UTF-8') as a:
    fieldnames = ["Id", "Images", "Title", "Description", "Price"]
    writer = csv.DictWriter(a, fieldnames=fieldnames)
    writer.writeheader()
    with open('stage3_test.csv', 'r', encoding='UTF-8') as b:
        reader = csv.DictReader(b, delimiter=',')
        for row in reader:
            if len(row["Images"].split(',')) > 3:
                writer.writerow(row)
