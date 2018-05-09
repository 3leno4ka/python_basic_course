import random, string

names = ('Elena', 'Boris', 'Petro', 'Ivan', 'Olga', 'Oleg', 'Irina', 'Sergiy', 'Nataliy', 'Svetlana')
surname = ('Gricko', 'Tarasenko', 'Shevchenko', 'Marchenko', 'Bondarenko', 'Omelchenko', 'Makagon', 'Konovalec', 'Ivanchenko', 'Korolenko')
middle_name = 'WERTYUIOPASDFGHJKLZXCVBNM'

def get_name():
    return random.choice(names)


def get_surname():
    return random.choice(surname)


def get_middle_name():
    return random.choice(middle_name)


def get_full_name():
    return f'{get_name()} {get_middle_name()}. {get_surname()}'


def get_number(qty, error_probability, additional_symbols):
    letters = string.ascii_letters + additional_symbols
    num = ''
    for i in range(0, qty):
        num += str(random.randint(0, 9)) if random.randint(0, error_probability * qty) != 1 else random.choice(letters)
    return num


def get_phone():
    return '+380'+get_number(9, 50, '[]-')


def get_cc():
    cc = get_number(16, 100, '- ')
    cc = cc[:4] + ' ' + cc[4:8] + ' ' + cc[8:12] + ' ' + cc[12:]
    return cc


def get_exp_date():
    month = random.randint(1,12)
    if month < 10:
        month = '0'+str(month)
    else:
        month = str(month)
    return f'{month}/{random.randint(19,30)}'

