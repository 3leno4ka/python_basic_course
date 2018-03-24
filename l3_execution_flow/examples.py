# name is not None

name = input("Enter your name: \n")
age = int(input("Enter your age: \n"))
email = f'{name}{age}@itea.ua'

surname = 'Noob'
try:
    name/'sometext'
except:
    surname = 'Voronov'
print('\nDeveloping with Python...\n')

if surname == 'Noob':
    print('you made a mistake!')
else:
    print('Win')







