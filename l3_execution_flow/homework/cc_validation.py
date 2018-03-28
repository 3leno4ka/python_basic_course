try:
    cc_number = int(input("Enter cc number: "))
    cc_number_str = str(cc_number)
    if len(cc_number_str) != 16:
        print(f'Cc number must contain 16 digits, but received {len(cc_number_str)}!')
        exit()
    # проверка номера кредитной карты по алгоритму Луна!
    cc_sum = 0
    even = False
    for digit in cc_number_str:
        dig = int(digit)
        if even:
            cc_sum += dig
        else:
            cc_sum += dig*2 if dig*2 < 10 else dig*2-9
        even = not even
    if (cc_sum % 10) != 0:
        print("Your cc number is incorrect! Please, try again")
        exit()

except ValueError:
    print("Cc number must contain only numbers!")

cc_date_str = input("Enter cc expiration date in format \"mm/yy\":")   # экранирование специальных символов
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

print("ha-ha-ha, I will use your credit card")









