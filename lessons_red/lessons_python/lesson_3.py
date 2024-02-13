'''
3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

3.2 Дан список list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
   - получите сумму всех чисел,
   - распечатайте все строки, где есть буква 'a'

3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж

3.4. Напишите программу, которая определяет, какая семья больше. 
      1) Программа имеет два input() - например, family_1, family_2. 
      2) Членов семьи нужно перечислить через запятую. 
     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
    о вашем любимом фильме. 
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение

3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1] 

3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     - проверьте являются ли эти множества подмножествами друг друга
'''
        # 1.
"""Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3"""

my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2][0], my_list[2][1], my_list[2][2], sep=',')

my_list = ['a', 'b', [1, 2, 't', 3], 4, 'd']
w = []

for i in my_list:
    if isinstance(i, int):
        w.append(i)
    elif isinstance(i, list):
        for si in i:
            if isinstance(si, int):
                w.append(si)
print(w)
new = [x for x in my_list if isinstance(x, int)]
new_list = [x for sublist in my_list if isinstance(sublist, list) for x in sublist if isinstance(x, int)]
print(new)
print(new_list)

        # 2.
"""Дан список list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
   #  - получите сумму всех чисел,
   #  - распечатайте все строки, где есть буква 'a'
"""

list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
q = []
for i in list_1:
    if isinstance(i, int):
        q.append(i)
print(sum(q))

w = []
for y in list_1:
    if isinstance(y, str) and 'a' in y:
        w.append(y)
print(w)

l = []
for _ in list_1:
    if type(_) == int:
        l.append(_)
print(l)

        #3
"""Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж"""
my_list_2 = ['cat', 'dog', 'horse', 'cow']
print(tuple(my_list_2))
print(my_list_2)

        #4
'''Напишите программу, которая определяет, какая семья больше. 
      1) Программа имеет два input() - например, family_1, family_2. 
      2) Членов семьи нужно перечислить через запятую. 
     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
'''
# family_1 = input().split(',')
# family_2 = input().split(',')
#
# if len(family_1) > len(family_2):
#     print(family_1)
# elif len(family_2) > len(family_1):
#     print(family_2)
# else:
#     print('Equal')

    # 5
'''Создайте словарь film c ключами title, director, year, budget, main_actor, slogan.\n
 В значения можете передать информацию
    о вашем любимом фильме. 
     - распечатайте только ключи
     - распечатайте только значения
     - распечатайте пары ключ - значение
'''
my_film = {'title': 'Крестный отец',
           'director': 'Christopher Nolan',
           'year': 1960,
           'budget': '$160 million',
           'main_actor': 'Leonardo DiCaprio',
           'slogan': 'Your mind is the scene of the crime'}
print(my_film.keys())#ключи в словаре
print(my_film.values())#значение словаря
print(my_film.items())#ключ - значение
print("\nПары ключ - значение:")
for key, value in my_film.items():
    print(f"{key}: {value}")

        #6
    '''Найдите сумму всех значений в словаре'''
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
summm = sum(my_dictionary.values())
print(summm)


        #7
"""Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]"""
qw = [1, 2, 3, 4, 5, 3, 2, 1]
wq = set(qw)#множество
print(wq)


        #8
"""Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     - проверьте являются ли эти множества подмножествами друг друга"""

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

inter1 = set1.intersection(set2)#создает новое множество, содержащее только те элементы которые есть во всех
inter2 = set2.symmetric_difference(set1)#Значения, которые не встречаются в обоих множествах
print(inter2)
print(inter1)