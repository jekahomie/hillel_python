# Task 1. 5 points
# сложить словари в один.
# использовать for и dict methods.
first = {1: 10, 2: 20}

second = {3: 30, 4: 40}

third = {5: 50, 6: 60}

fourth = {7: 70, 8: 80}

fifth = {9: 90, 10: 100}
six = {}
for key, value in first.items():
    six[key] = value
    for key, value in second.items():
        six[key] = value
        for key, value in third.items():
            six[key] = value
            for key, value in fourth.items():
                six[key] = value
                for key, value in fifth.items():
                    six[key] = value

print(six)  # я знаю что заморочился , можно было через | сделать. Но оставлю как есть
# Надеюсь баллы не снимете =)

# Task 2.10 points
# 1. Создать словарь с ключами от 11 до 20 включительно. Значения = квадраты ключей
a = {1: 1, 2: 4, 3: 9,
     4: 16, 5: 25, 6:
         36, 7: 49, 8: 64,
     9: 81, 10: 100, 11: 121,
     12: 144, 13: 169, 14: 196, 15: 225}
print(sum(a.values()))

# Task 3.5 points
# отсортировать словарь по ключам
names = {1: 'Alex', 2: 'Fred', 4: 'Oleg', 3: 'John', 6: 'David', 5: 'Yannick'}
print(sorted(names.keys()))

# Task 4.15 points
a = {'id1':

    {

        'name': 'Ruslan',

        'class': 1,

        'subjects': {'Math', 'Algorithms', 'English'}

    },

    'id2':

        {

            'name': 'Mark',

            'class': 2,

            'subjects': {'Geometry', 'Java', 'Cooking'}

        },

    'id3':

        {

            'name': 'Ruslan',

            'class': 1,

            'subjects': {'Math', 'Algorithms', 'English'}

        }

}
b = []
res = dict()
for key, val in a.items():
    if val not in b:
        b.append(val)
        res[key] = val
print(res)

# Task 5. 10
# Вернуть уникальные из dictionary
a = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
     {"VIII": "S007"}]
s = set()
for dic in a:
    for val in dic.values():
        s.add(val)
print(s)

# Task 6.15
#  Посчитать общее количество наименований в списке. И только в списках.
shedule = {'monday':
               ['clean house', 'drive car', 'meet with freands'],
           'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}


def get_all_elements_in_list_in_lists():
    count = 0
    for element in shedule:
        count += len(element)
        return count


print(get_all_elements_in_list_in_lists())
#dict python.org https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Task 7.10 points
# 11/11 have screenshot ;)

# Task 8.25 points
# Понял и закрепил что такое Хеширование.