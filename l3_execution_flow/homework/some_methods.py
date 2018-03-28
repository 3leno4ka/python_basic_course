my_str = input("Enter some text: ")
if not my_str == "":
    print("ok")
else:
    print("Text can't be empty")

my_int = input("Enter some number: ")

try:
    int(my_int)
except ValueError:
    print("Not a number!")

my_float = input("Enter some float: ")


try:
    float(my_float)
except ValueError:
    print("Not a float!")


x = 15
y = 54
if x == y or x < y and x == 10 + 5:
    print("It's True")
if x <= y:
    print("Yes")






