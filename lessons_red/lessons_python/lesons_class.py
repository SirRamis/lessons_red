# # # class Persons:
# # #     def __init__(self,my_name, your_name):
# # #         self.my_name = my_name
# # #         self.your_name = your_name
# # #
# # #     def greet(self):
# # #         return f'Hello {your_name}, my name is {my_name}'
# # # person1 = Persons('Al','Ram')
# # # print(person1.your_name)
# # #
# # # class Person:
# # #     def __init__(self, first_name, last_name, age):
# # #         self.first_name = first_name
# # #         self.last_name = last_name
# # #         self.age = age
# # #     def prin(self):
# # #         print(f'{self.first_name}')
# # #
# # #     def prin2(self):
# # #         print(f'{self.last_name}')
# # # per = Person('sdf','sdfas',45)
# # # print(list(per))
# # # gender = {
# # #     'm': 'Дорогой',
# # #     'f': 'Дорогая'
# # # }
# # #
# # # a = [
# # #     ['Ramis','Sirazetdinov', 123, 'm'],
# # #     ['Amina','Nuriahmet',22, 'f'],
# # #     ['Ilgiz','Kadirov', 55, 'm']
# # #     ]
# # # for name, lname, balance, g in a:
# # #     text = f"{gender[g]} {name} {lname}, баланс вашего счета составляет {balance} руб."
# # #     print(text)
# # # print(type(a))
# # # print(type(gender))
# #
# # tumb = ["ножницы", "карандаш", "яблоко", "книга"]
# #
# # for obj in tumb:
# #     print(obj)
# #
# #
# # tumb = ["ножницы", "карандаш", "яблоко", "книга"]
# #
# # # получаем итератор для итерируемого объекта
# # it = iter(tumb)
# #
# # try:
# #     while True:
# #         next_val = next(it)
# #         print("Очередное значение:", next_val)
# # except StopIteration:
# #     # явно напечатаем сообщение об окончании итерации,
# #     # хотя цикл for этого не делает и ошибка просто подавляется
# #     print("Итерация закончена")
# # print("Программа завершена")
# def sum_num(s):
#     a = 0
#     for i in s:
#         if i.isdigit():
#             a += int(i)
#     print(a)
#
# sum_num('5747fhdhhdfh')
#
# def get_body_mass_index(m,r):
#     b = r / 100
#     a = m / (b ** 2)
#     if a < 18.5:
#         print('Недостаточная масса тела')
#     elif 18.5 <= a <= 25:
#         print('Норма')
#     elif a > 25:
#         print('Избыточная масса тела')
#     print(a)
# get_body_mass_index(77,175)
#
# def check_password(x):
#     a = "!@#$%*"
#     b = []  # zifri
#     c = []  # spez znaki
#     d = []  # zaglavnii
#     for i in x:
#         if i.isdigit():
#             b += i
#     print(b)
#
#     for k in x:
#         if k in a:
#             c += k
#     print(c)
#
#     for y in x:
#         if y.isupper():
#             d.append(y)
#     print(d)
#
#     # if len(x) >= 10 and b and c and d:
#     #     return True
#     # else:
#     #     return False
#
#     if len(x) >= 10 and b and c and d:
#         print("Perfect password")
#     else:
#         print("Easy peasy")
#
# check_password('d24hsf!gsdgfQWE1@457#$')
# def count_letters(slovo):
#     K = []
#     N = []
#     for i in slovo:
#         if i.islower():
#             K.append(i)
#     for k in slovo:
#         if k.isupper():
#             N.append(k)
#     print(f'Количество заглавных символов: {len(N)}')
#     print(f'Количество строчных символов: {len(K)}')
#
# count_letters('rkehvjhevvvbvERERG')
#
import turtle


def move(size):
    turtle.forward(size)
    turtle.left(90)


def draw_square(size):
    for i in range(4):
        move(size)
#draw_square(60)
move(30)
#
# # def draw_color_square(size, name_color):
# #     turtle.color(name_color)
# #     turtle.begin_fill()
# #     for i in range(4):
# #         move(size)
# #     turtle.end_fill()
# #
# #
# # turtle.speed(1)
# # turtle.goto(0, -150)
# # draw_color_square(50, 'red')
# # turtle.goto(0, 0)
# # draw_color_square(100, 'green')
# # turtle.goto(0, 150)
# # draw_color_square(150, 'blue')
#
# def is_between(a,b,c):
#     if c <= a <= b and c >= a >= b:
#         print("True")
#     else:
#         print("False")
# is_between(3,5,6)
#
# def count_letter(text, letter):
#    a = []
#    for i in text:
#        if i == letter:
#            a.append(i)
#    print(len(a))
# count_letter('gsgfrtbe', 'g')
#
# def print_initials(name, surname, middlename):
#     print(surname.capitalize())
#     print(surname[0].capitalize())
#     print(name.capitalize([0]))
# print_initials('fgsdf','sdfgfd','sdfgdf')