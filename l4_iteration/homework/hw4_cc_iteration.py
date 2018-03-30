

while True:

    cc_number = input("Enter cc number in format \'XXXX XXXX XXXX XXXX\': \n")
    cc_number_list = cc_number.split(" ")
    if len(cc_number_list) != 4:
        print("Bad cc number format! Try again!")
        continue
    cc_number_str = ''
    quartets_are_good = True
    for quartet in cc_number_list:
        if len(quartet) != 4:
            print("Bad cc number format! Try again!")
            quartets_are_good = False
            break
        try:
            int(quartet)
        except ValueError:
            print("Bad cc number format! Try again now!")
            quartets_are_good = False
            break
        cc_number_str += quartet
    if not quartets_are_good:
        continue

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
        continue
    break
if cc_number_list[0] == '5167':
    print("You use PrivatBank credit card!")
elif cc_number_list[0] == '5375':
    print("You use MonoBank credit card!")
else:
    print("You use credit card from the unknown bank")
    

# except ValueError:
#     print("Cc number must contain only numbers!")

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









