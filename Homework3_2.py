# Создать по 3 варинта всех уже изученных объектов в Пайтоне.
# line1st - strings
'hello'.capitalize()
'hello'.title()
'hello'.count()

# Numbers
int = 15
float = 15.5
int = round(10 / 3, 2)

# line 2 - Cписки
# Standart type of lists
list1 = [1, 5, 10]
list2 = ['dog', 'cat', 'cow']
list3 = ['beer', 'wine', 'whiskey']

# Вариант реверса текста в списке
list = [10, 20, 30, 40, 50]
list.reverse()

# Вариант сортировки имён по алфавиту в списке
names = ['Adam', 'Fred', 'Gregory', 'Eleonora', 'Xan', 'Robert', 'Ad']
names.sort()
print(names)

# line 3 - Словари
# Стандартный вид словаря
MyVehicle = {'type': 'car', 'size': 'standard', 'brand': 'BMW'
, 'model': '5-series', 'class': 'luxury'}
print(MyVehicle)

# Вид словаря с примером емейл адресов
email = {'Bob': 'bob@gmail.com',
         'Marta': 'marta@icloud.com',
         'David': 'david777@boss.net'}
print(email)

# Метод get()
bbq = {
    'meat': 13,
    'drinks': 5,
    'snacks': 2
}
print(bbq.get('drinks'))

# 4 Кортежи
# Стандартный вид
tuple = ["tom", "boss", "job", "cjhendriks"]
print(tuple)

# Кортеж с применением len()
tuple = ["tom", "boss", "job", "cjhendriks"]
print(len(tuple))

# Кортежи с применением sorted()
tuple = ["Adam", "Paradise", "Ewa", "Apple"]
print(sorted(tuple))

# Срез кортежа
tuplefloat = (1.0, 1.5, 2.0, 4.0, 8.0, 16.0)
print(tuplefloat[0:4])

# Применение функций max() & min()
# min()
a = [1, 2, 43, 58, 173]
print(min(a))

# max()
a = [1, 2, 43, 58, 173]
print(max(a))

# Применение min() max() в двух списках
a = [1, 2, 43, 58, 173]
b = [4, 8, 175, 819]
c = min(a, b)
print(c)

# Применение min() max() в списке из имён
a = ['Adam', 'Bob', 'Jack', 'Patrick', 'Vincent']
print(max(a))

# Применение операторов принадлежности in
a = "b" in "abc"
print(a)

# Применение in в списке
a = 123 in [1, 4, 18, 58, 923, 666, 777]
print(a)

# Применение in в словаре
data = {'Age': 30, 'Name': 'Fred', 'Surname': 'Nord'}
if 'Age' in data:
    print(f"He is {data['Age']} years old")

# Применение if
coffe = input("what`s your favourite coffe,sir ?:")

if coffe == 'latte':
    print("Very good choice !")

# Применение if + else
coffe = input("what`s your favourite coffe,sir ?:")

if coffe == 'latte':
    print("Very good choice !")
else:
    print("No way !")

# Применение if + elif + else
coffe = input("what`s your favourite coffe,sir ?:")

if coffe == 'latte':
    print("Very good choice !")
elif coffe == 'Americano':
    print('Not bad , dude!')
else:
    print("No way !")

# Дополнительная задача на повторение
try:
    age = str(input("How old are you? :"))
except:
    print("Ошибка, введено не целое число")

if age == str(16):
    print('You should to visit Netherlands')

elif str(17) <= age < str(21):
    print('You should to visit Thailand')

elif str(16) > age:
    print('You`re young , stay at home :)')
else:
    print('Everywhere,friend...Everywhere')

# Задача 2 на 25 баллов
user_name = input('What`s your name? :')
if user_name == 'admin':
    print('Welcome back , Lord')
elif user_name == 'Женя':
    print('Рекомендую посмотреть Tenet')
elif user_name == 'Guido':
    print('Thank you so much!')

age = int(input('How old are you? :'))
gender = str(input('Gender? :'))

if 14 >= age >= 10 and gender == str('man'):
    print('Обязательно к просмотру : Starwars , Mandolorian')
elif 32 >= age >= 22 and gender == str('female'):
    print('Transformers')
if age > 32 and gender == str('man'):
    print('Mando')
elif 12 < age < 16:
    print('Insurgent')
if age < 11:
    print('TMNT')

# Задание номер 3 для закрепления материала
# Питон не хотел воспринимать символы из лмс
string = ('тутпитоннехотелвосприниматьсимволыиззаданиявлмс')
print(string[0::5])

# фильтр мата
from better_profanity import profanity

if __name__ == "__main__":
    text = "...sh1t...hello_cat_fuck,,,,123"

    censored_text = profanity.censor(text)
    print(censored_text)
