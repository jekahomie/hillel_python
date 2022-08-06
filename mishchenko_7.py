# Task 1 begginer
# 5 lst.compr
# Standart

h_lst = [letter for letter in 'Hillel']
print(h_lst)

# Compr + append
h_letters = []
for letter in 'School':
    h_letters.append(letter)

print(h_letters)

# lambda
let = [list(map(lambda x: x, 'The Best'))]
print(let)

# Range
n_l = [x for x in range(20) if x % 2 == 0]
print(n_l)

# if else compr
obj = ['Even' if i % 2 == 0 else 'Odd' for i in range(10)]  # Перебираем чётные не чётные в ренже до 10
print(obj)

# DICT COMPR
sq_dict = dict()
for num in range(1, 11):
    sq_dict[num] = num * num
print(sq_dict)

# Регулируем цену по новому курсе использую .items и переменную usdtoeur
old = {'Bread': 1.32, 'Milk': 1.12, 'Potato': 0.67}
usdtoeur = 0.95
new = {item: value * usdtoeur for (item, value) in old.items()}
print(new)

# Проверяем возвраст на чётный/нечётный среди Dict
odict = {'Petya': 31, 'Vasya': 49, 'Toha': 40, 'Andr': 38}
edict = {k: v for (k, v) in odict.items() if v % 2 == 0}
print(edict)

# Проверяем возвраст на чётный/нечётный среди Dict И устанавливаем лимит до 40 лет
odict = {'Petya': 31, 'Vasya': 48, 'Toha': 40, 'Andr': 38}
edict = {k: v for (k, v) in odict.items() if v % 2 == 0 if v < 40}
print(edict)

# if-else для индексикации возраста
odict = {'Petya': 31, 'Vasya': 48, 'Toha': 40, 'Andr': 38}
sepdict = {k: ('old' if v > 40 else 'young')
           for (k, v) in odict.items()}
print(sepdict)

# SET COMPR
# range
a = {i for i in range(10)}
print(a)

# Even
aa = {i for i in range(10) if i % 2 == 0}
print(aa)

# math func
aaa = {i * i for i in range(5)}
print(aaa)

# unique
v1 = [10, '10', 10 , '30', '30', 81 , 82 , 84 ,81]
uniq = {int(v1) for v1 in v1}
print(uniq)

# matrix
matrix = []
for row_index in range(0, 3):
    row = []
    for col_index in range(0, 3):
        if col_index == row_index:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)
print(matrix) 