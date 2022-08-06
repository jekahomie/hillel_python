# Def without return
def funk():
    pass


print(funk())


# funk if else
def display(number):
    if number == 2:
        pass
    else:
        print('number', number)


display(2)
display(3)


# def greet
def greet(name):
    print('hello ' + name)


greet('Admim')

# fstr
def hello(n1,age):
    print(f'I am {n1} ,and I am {age} years old ')
hello('Yevgen', 26)

# key=value
def f_lang(language='Python'):
    print(f'My favourite prog lang is {language}')
f_lang()