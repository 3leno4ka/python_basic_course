
low_digit_limit = 1
upper_digit_limit = 100
my_new_list = []
while True:
    favorite_num = input("Enter your favorite number: ")
    try:
        favorite_num = int(favorite_num)
        my_new_list.append(favorite_num)
        if favorite_num < low_digit_limit:
            print(f'Your input value is less than {low_digit_limit}')
        elif favorite_num > upper_digit_limit:
            print(f'Your input value is more than {upper_digit_limit}')
        else:
            break
    except ValueError:
        my_new_list.append(favorite_num)

print(my_new_list)
your_list = [favorite_num for favorite_num in my_new_list if type(favorite_num) == str]
print(your_list)




