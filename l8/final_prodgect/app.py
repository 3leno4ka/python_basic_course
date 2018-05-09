from utils import *
import csv

def generate_dict():
    return {"Name": get_full_name(), "Phone": get_phone(), "Exp_date": get_exp_date(), "Card": get_cc()}
def correct_holder(holder):
    if phone_has_errors(holder.get('Phone')) == False and card_has_errors(holder.get('Card')) == False:
        return True
    else:
        return False

card_holders = []
card_holders_correct = []
card_holders_errors = []

for i in range(0, 100):
    card_holders.append(generate_dict())

for i in card_holders:
    if correct_holder(i) == True:
        card_holders_correct.append(i)
    else:
        card_holders_errors.append(i)

print(card_holders_errors)

with open('card_holders.csv', 'w', newline='') as csv_file:
    csv_file_writer = csv.DictWriter(csv_file, fieldnames=['Name', 'Phone', 'Exp_date', 'Card'])
    csv_file_writer.writeheader()
    for row in card_holders_correct:
        csv_file_writer.writerow({'Name': row.get('Name'),
                                  'Phone': row.get('Phone'),
                                  'Exp_date': row.get('Exp_date'),
                                  'Card': row.get('Card')})

with open('card_holders_errors.csv', 'w', newline='') as csv_file:
    csv_file_writer = csv.DictWriter(csv_file, fieldnames=['Name', 'Phone', 'Exp_date', 'Card'])
    csv_file_writer.writeheader()
    for row in card_holders_errors:
        csv_file_writer.writerow({'Name': row.get('Name'),
                                  'Phone': row.get('Phone'),
                                  'Exp_date': row.get('Exp_date'),
                                  'Card': row.get('Card')})
