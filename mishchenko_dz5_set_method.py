# Задача  set methods
s1 = set('SET')
print(s1)

# add
s1 = set('SET')
s1.add('A')
print(s1)

# clear
s1 = set('SET')
s1.clear()
print(s1)

# copy
s1 = set('SET')
s2 = {}
s2 = s1.copy()
print(s2)

# difference
s1 = {1, 2, 3}
s2 = {1, 5, 3}
dfs = s1.difference(s2)
print(dfs)

# difference.update
s1 = {1, 2, 3}
s2 = {4, 5, 6, 7, 8, 9}
s3 = {6, 4, 2, 9}
s1.difference_update(s2, s3)
print(s1)

# discard
s1 = {1, 2, 3, 5, 7, 15, 21, 325}
s1.discard(21)
print(s1)

# intersection
s1 = {1, 2, 3, 9, 12, 123123, 544, 655, 21}
s2 = {4, 10, 13, 9, 123123, 6}
i_sec = s1.intersection(s2)
print(i_sec)

# intersection_update
s1 = {1, 2, 3}
s2 = {4, 5, 3}
s1.intersection_update(s2)
print(s1)

# isdisjoint
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.isdisjoint(s2))

# issubset
s1 = {1, 2, 3}
s2 = {1, 2, 3}
print(s1.issubset(s2))

# issuperset(iterable)
s1 = {1, 2, 3}
s2 = {2}
spisok = [1, 3]
print(s1.issuperset(s2), s1.issuperset(spisok))

# pop
s1 = {4, 5, 12, 13, 41}
print(s1.pop())

# remove
s1 = {21, 22, 23}
s1.remove(22)
print(s1)

# symmetric_difference
s1 = {'Apple', 'Pear', 'Melon'}
s2 = {'Banana', 'Plum', 'Pear'}
print(s1.symmetric_difference(s2))

# symmetric_difference.update
s1 = {'Apple', 'Pear', 'Melon'}
s2 = {'Banana', 'Plum', 'Pear', 'Apple'}
s1.symmetric_difference_update(s2)
print(s1)

# union
s1 = {1, 2, 3}
s2 = {4, 5, 6}
un = s1.union(s2)
print(un)

# update
s1 = {1, 2, 3}
s1.update([4,5])
print(s1)