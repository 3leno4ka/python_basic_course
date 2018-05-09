import re
CURRENT_YEAR = 18
CURRENT_MONTH = 4

CC_REGEX = re.compile(r'^([\d]{4} ){3}[\d]{4}')


def card_has_errors(cc_number):
    if re.match(CC_REGEX, cc_number):
        return False
    return True


def print_bank(cc_number):
    cc_number_list = cc_number.split(" ")
    if cc_number_list[0] == '5167':
        print("You use PrivatBank credit card!")
    elif cc_number_list[0] == '5375':
        print("You use MonoBank credit card!")
    else:
        print("You use credit card from the unknown bank")


def date_has_error(cc_date_str):
    cc_date = cc_date_str.split("/")   # метод "split()"-разбиение текста с заданным разделителем на элементы списка!
    try:
        cc_date_mm = int(cc_date[0])
        cc_date_yy = int(cc_date[1])
    except ValueError:
        print("Date error! Must be a number")
    if cc_date_yy < CURRENT_YEAR or cc_date_yy > 99:
        print("Please, check year!")
        return True
    if cc_date_mm < 1 or cc_date_mm > 12:
        print("Please, check month!")
        return True
    if cc_date_yy == CURRENT_YEAR and cc_date_mm < CURRENT_MONTH:
        print("Your cc already expired!")
        return True
    return False


def cvv_has_error(cvv_code):
    try:
        int(cvv_code)
    except ValueError:
        print("Bad CVV code! Please, try again")
    if len(str(cvv_code)) < 3:
        print("CVV code is too short! Please, try again")
        return True
    return False
