def one():
    x = ['one', 'two']

    def inner():
        print(x)
        print(id(x))
        return inner()


o = one()
print(o)  # Я не понял почему у меня None выбивает?? должен принтиться список


def phone_number(numbers):
    return [f'+044{number}' for number in numbers]


def show_number(numbers):
    for number in numbers:
        print(number)


show_number(phone_number([838372893]))
