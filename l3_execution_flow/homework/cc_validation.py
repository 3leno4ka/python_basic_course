try:
    cc_number = int(input("Enter cc number: "))
    if len(str(cc_number)) != 16:
        print(f'Cc number must contain 16 digits, but received {len(str(cc_number))}!')
        exit()
except ValueError:
    print("Cc number must contain only numbers!")

cc_date_str = input("Enter cc expiration date in format \"mm/yy\":")
cc_date = cc_date_str.split("/")   # метод "split()"-разбиение текста с заданным разделителем на элементы списка!

try:
    cc_date_mm = int(cc_date[0])
    cc_date_yy = int(cc_date[1])
    if cc_date_mm < 1 or cc_date_mm > 12:
        print("Please, check month!")
        exit()
    if cc_date_yy < 0 or cc_date_yy > 99:
        print("Please, check year!")
        exit()

except ValueError:
    print("Date error!")

try:
    cvv_code = int(input("Enter CVV code: "))
    if len(str(cvv_code)) < 3:
        print("CVV code is too short!")
        exit()
except ValueError:
    print("Bad CVV code!")

print("ha-ha-ha, i will use your credit card")









