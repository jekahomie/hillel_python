# Задача 1.10 баллов
password = int(input('Enter your password: '))  # Запрос пароля
password_check = int(input('Enter your password 1 more time'))  # Повторная проверка
while password == password_check:  # Если повторная проверка = первой выводим :
    print('Welcome')
    break  # завершаем цикл провелки
else:  # если не равны принтим
    print('incorrect password')

# Задача 2.5 баллов
input_data = ['bear', 'milk', 'egg', 'egg', 'egg', 'egg']  # Входные данные
a = 'egg'  # Что нас не интересует
while a in input_data:  # если то , что не интересует , во входных данных
    input_data.remove(a)    # Ремувим
print(input_data)

# Задача 3.10 баллов
my_list = [11, 23, 65, 44, 76, 533]  # Входные данные
x = 0  # добавляем переменную для счётчика
for i in my_list:   # Перебираем список
    x += i % 2  # Если остаток от 2х - чётное
if x == 0:
    print('even')
else:   # Тут входные данные на нечётные
    print('odd')

# Задача 4.25 баллов

m_lists = dir(set)  # вызываем все методы сета
i = 0  # присваиваем переменную для перебора
while i != len(m_lists):
    if m_lists[i][0] == '_':  # значение которое нужно исключить из перебора
        m_lists.pop(i)  # попим его
    else:
        i += 1
print(m_lists)  # получаем +25 за успешное задание :)

# Задача 5.15 баллов
# на 100% не вышло , но успехи после 6 раз - есть )

# Задача 6.5 баллов
# в отдельном файле на Гитхабе,дабы не засорять тут

# Задача 7.25 баллов
frz: frozenset = frozenset([1, 2, 3, 'Adam', 'Hloe'])
counter: int= 0
for i in frz:
    counter += 1
    print(f'Total {counter} you have inside')

