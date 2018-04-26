import random, csv, re
companies = ('tesla', 'acura', 'micro')
emails_ly = []
emails_ny = []
for i in range(50):
    company = random.choice(companies)
    emails_ly.append(f'{company}{random.randint(1,11)}@{company}.com')
    company = random.choice(companies)
    emails_ny.append(f'{company}{random.randint(1,30)}@{company}.com')

emails_set_ly = set(emails_ly)
print(f'all:{len(emails_ly)}, set:{len(emails_set_ly)}')
emails_set_ny = set(emails_ny)
print(f'all:{len(emails_ny)}, set:{len(emails_set_ny)}')

second_comers = set.intersection(emails_set_ly, emails_set_ny)

with open('second_comers.csv', 'w', newline='') as csv_file:
    csv_file_writer = csv.DictWriter(csv_file, fieldnames=['Email', 'Name'])
    csv_file_writer.writeheader()
    for row in second_comers:
        csv_file_writer.writerow({'Email': row, 'Name': row.split('@')[0]})
