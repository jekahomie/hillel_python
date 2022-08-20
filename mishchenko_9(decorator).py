# Замыкания
def strip_string(strip_chars=''):
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip


strip1 = strip_string()
strip2 = strip_string(' !?.,')
print(strip1('   Hello python !?.,'))
print(strip2('   Hello python !?.,'))

# Декоратор
def funk_dec(func):
    def wrapper(*args, **kwargs):
        print('------- Что-то делаем перед вызовом функции')
        res = func(*args, **kwargs)
        print('--------Что-то делаем после вызова функции')
        return res
    return wrapper


def some_func(title, tag):
    print(f'title= {title}, tag = {tag}')
    return f'<{tag}>{title}</{tag}>'

some_func = funk_dec(some_func)
res = some_func('python Навсегда', 'h1')
print(res)

# Задание с номером телефона
# Task 2
def say_name(number):
    def say_goodbye():
        print('+044', number )

    say_goodbye()

say_name('838372893')

# OR
# Task 2
def phone_num(number):
    def c_code():
        print('Your phone number is:', c_num ,number )

    return c_code()

c_num = ('+044')
f = phone_num('838372893')
