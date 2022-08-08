from datetime import datetime


# Task1. 5 points
#
# Написать функцию которая будет принимать 3 аргумента (int) и находить максимум из них '''
def max_num(a: int, b: int, c: int) -> int:
    return max(a, b, c)


num1: int = int(input('1st num: '))  # 1st int
num2: int = int(input('2nd num: '))  # 2nd int
num3: int = int(input('3rd num: '))  # 3rd int
print(max_num(num1, num2, num3))  # print max


# Task2. 10 points
#
# Написать функцию которая будет принимать 2 аргумента (int) и находить максимум из них.
#
# Затем используя функцию1 (вызвать ее) написать функцию2
# которая будет принимать 3 аргумента и находить максимум с помощью функции1.
def mn(a: int, b: int) -> int:
    return max(a, b)


def max_f(a: int, b: int, c: int) -> int:
    max_2: int = mn(a, b)
    return max(max_2, c)


num1: int = int(input('1st num: '))  # 1st int
num2: int = int(input('2nd num: '))  # 2nd int
num3: int = int(input('3rd num: '))  # 3rd int
print(max_f(num1, num2, num3))

# Task 3. 10 points Lambda function. с помощью Анонимной функции остортировать список кортежей по цифре.

ex_list: list = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
ex_list.sort(key=lambda x: x[1])
print(ex_list)

# Task 4
# python package datetime


actual = datetime.now()  # var = actual
year = lambda x: x.year  # var = year
month = lambda x: x.month  # var = month
day = lambda x: x.day  # var = day
print('current year is : ', year(actual))
print('current month is :', month(actual))
print('current day is :', day(actual))

# https://docs.python.org/3.9/library/datetime.html?highlight=datetime#module-datetime
