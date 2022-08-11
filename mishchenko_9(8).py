# Task 1 all
ip: str = '192.168.0.1'
print(all(ip))

i_p: str = '192.168.0.1'
print(all(ip.isdigit() for i in i_p.split('.')))

# Task 2 any
ad: list = [False, True, False]
print(any(ad))

ad2: str = '192.168.0.1'
print(any(ad2.isdigit() for x in ad2.split('.')))

# Task 3 isinstance
print(isinstance(1, int))
print(isinstance('1', str))
print(isinstance(1.25, float))
print(isinstance([1], list))
print(isinstance(True, bool))
a = 3
print(isinstance(a, object))
xxx = (1, 2, 3)
print(isinstance(xxx, tuple))
b = {}
print(isinstance(b, dict))
c = {'apple'}
print(isinstance(c, set))
d = frozenset([1])
print(isinstance(d, frozenset))


# Task 4 BOOK

# Task 5 Надеюсь я правильно понял задачу :D
def butterbroad(char):
    print(char)
    return


def kolabas(inside):
    print(inside)
    return


butterbroad('Дуже смачний \n'
            'а класс')
kolabas('')
print(type(kolabas))

# Task 6
# LOCAL / ENCLOSING / GLOBAL / Built-in-scope
# Что означает :
# в локальной области видимости ф-ции(local)
# в лок.областях видимости объемлющих ф-ций(enclosing)
# в глобальной области видимости (global)
# во встроенной области видимости (built-in)
