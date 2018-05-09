from cc_validation import card_has_errors, print_bank, date_has_error, cvv_has_error

while True:
    cc_number = input("Enter cc number in format \'XXXX XXXX XXXX XXXX\': \n")
    if card_has_errors(cc_number):
        continue
    break

print_bank(cc_number)

while True:
    cc_date_str = input("Enter cc expiration date in format \"mm/yy\":")   # экранирование специальных символов
    if date_has_error(cc_date_str):
        continue
    break

while True:
    cvv_code = input("Enter CVV code: ")
    if cvv_has_error(cvv_code):
        continue
    break

print("ha-ha-ha, I will use your credit card")









