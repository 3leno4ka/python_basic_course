# my_file = open()
# csv look in python.doc
# import os - указать путь к текст.файлу

my_text = ('Hi,\n'
           '\n'
           'I am a Python developer and I want to work a cool team.\n'
           'I would like to get a chance to work in your company.\n'
           'My work experience isn\'t big enough, but I am an open minded person and ready to work hard.\n'
           '\n'
           'Best regards,'
           '\n'
           '{name} {surname}')



# text_file = open('my_text_file.txt', 'w')
# text_file.write(my_text)

name = input('Enter your name: ')
surname = input('Enter your surname: ')

my_text = my_text.format(name=name, surname=surname)
print(my_text)

with open('my_text_file', 'w') as f:
    f.write(my_text)

with open('my_text_file', 'r') as f_read:
    result = 0
    for line in f_read:
        result += line.lower().count("work")
        print(result)

