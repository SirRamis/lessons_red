# # class Persons:
# #     def __init__(self,my_name, your_name):
# #         self.my_name = my_name
# #         self.your_name = your_name
# #
# #     def greet(self):
# #         return f'Hello {your_name}, my name is {my_name}'
# # person1 = Persons('Al','Ram')
# # print(person1.your_name)
# #
# # class Person:
# #     def __init__(self, first_name, last_name, age):
# #         self.first_name = first_name
# #         self.last_name = last_name
# #         self.age = age
# #     def prin(self):
# #         print(f'{self.first_name}')
# #
# #     def prin2(self):
# #         print(f'{self.last_name}')
# # per = Person('sdf','sdfas',45)
# # print(list(per))
# # gender = {
# #     'm': 'Дорогой',
# #     'f': 'Дорогая'
# # }
# #
# # a = [
# #     ['Ramis','Sirazetdinov', 123, 'm'],
# #     ['Amina','Nuriahmet',22, 'f'],
# #     ['Ilgiz','Kadirov', 55, 'm']
# #     ]
# # for name, lname, balance, g in a:
# #     text = f"{gender[g]} {name} {lname}, баланс вашего счета составляет {balance} руб."
# #     print(text)
# # print(type(a))
# # print(type(gender))
#
# tumb = ["ножницы", "карандаш", "яблоко", "книга"]
#
# for obj in tumb:
#     print(obj)
#
#
# tumb = ["ножницы", "карандаш", "яблоко", "книга"]
#
# # получаем итератор для итерируемого объекта
# it = iter(tumb)
#
# try:
#     while True:
#         next_val = next(it)
#         print("Очередное значение:", next_val)
# except StopIteration:
#     # явно напечатаем сообщение об окончании итерации,
#     # хотя цикл for этого не делает и ошибка просто подавляется
#     print("Итерация закончена")
# print("Программа завершена")
def sum_num(s):
    a = 0
    for i in s:
        if i.isdigit():
            a += int(i)
    print(a)

sum_num('5747fhdhhdfh')

def get_body_mass_index(m,r):
    b = r / 100
    a = m / (b ** 2)
    if a < 18.5:
        print('Недостаточная масса тела')
    elif 18.5 <= a <= 25:
        print('Норма')
    elif a > 25:
        print('Избыточная масса тела')
    print(a)
get_body_mass_index(77,175)

def check_password(x):
    a = "!@#$%*"
    b = []  # zifri
    c = []  # spez znaki
    d = []  # zaglavnii
    for i in x:
        if i.isdigit():
            b += i
    print(b)

    for k in x:
        if k in a:
            c += k
    print(c)

    for y in x:
        if y.isupper():
            d.append(y)
    print(d)

    if len(b) >= 10:
        return True
    print(len(b))

check_password('d24hsf!gsdgfQWE1@457#$')
