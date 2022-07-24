# Задача 1
a = input("Hello , enter your str here :")
if len(a) <= 2:
    print(f"Your %s too short !\n:"
          f"{a} <- this one :)")
print(a[0:2] + a[-2:])

# Задача 2
stroke = input("Enter your stroke:")  # запрос входной строки
result = {}  # вывод результата в словарь
for i in stroke:  # генерируем считывание символов
    result[i] = stroke.count(i)
print(result)

# Задача 3

grossary = ['bread', 'milk', 'kolbasa']  # Наш список
maxlen = max(grossary, key=len)  # Запрос по ключу длинны
print(f'The most long word:{maxlen}')  # Вывод по ключу

# Задача 4
name = str(input('Enter your name:'))
print(str.upper(name).format(), str.lower(name).format())

# Задача 5
list1 = ('red', 'white', 'black', 'red', 'green', 'black')
print(set(sorted(list1)))

# Задача 6
# Кортеж - нельзя изменить , так что удалить значение из него нельзя
# но есть альтернатива

kotedj = (1, 2, 3)  # Наши значения в кортеже
a, b, c = kotedj  # Присвоение индексов
print(a, b)  # Вывод значений по индексу

# Задача 7
kort = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
spisok = list(kort)
print(spisok)

# Задача 8

for i in range(-99, 99, 3):  # Задаём старт,стоп,шаг
    print(f'this number : {i} , is ''devided by the 3')  # Выводим результат через ф строку

# Задача 9
list1 = [1, 2, 3]
list2 = [4, 5, 3]
c = []
for x in list1:
    for i in list2:
        if x == i:
            c.append(x)
            break
print(c)