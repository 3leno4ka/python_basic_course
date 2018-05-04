from l5_function.my_first_package import my_func, year_of_birth


def aa():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    age = int(input("Enter your age "))
    year_of_birth(age)
    my_func(name, surname, age)


aa()

