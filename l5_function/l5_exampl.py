
def hello_world():
    print("Hello, world")

    def print_my_name(name):
        if len(name) < 4:
            print(f'Hi, you have a short {name}!')
        print_my_name("Ivan")

    def my_sum(a, b, c=1):
        return c * (a + b)
    x = 10
    y = 20
    my_sum(x, y)

    print(my_sum)
    x = my_sum(5, 6)
    y = my_sum(5, 6, 2)





