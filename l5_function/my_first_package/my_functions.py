def my_func(name, surname, age):
    if age < 25:
        print(f'Hello, {name} {surname}. You are young enough.')
    if age >= 25:
        print(f'Hello, {name} {surname}. You are old.')


def year_of_birth(age):
    print(f'{2018 - age}')
