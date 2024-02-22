# '''
# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
#
# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
#
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
#
# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке (my_list)
# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
#
# 	'''
#
#         #1
# def square(a):
#     p = a * 4
#     s = a * a
#     d = a * (2 ** 0.5)
#     return p, s, d
#
#         #2
# q, w, e = square(5)
# print(q, w, e)
#
# def print_arguments(**kwargs):
#     for arg, value in kwargs.items():
#         print(f"{arg}: {value}")
#         #return f"{arg}:{value}"
#
# print_arguments(name="Alice", age=30, city="New York", country="USA")
#
# #a = print_arguments(name='ramis', age=39)
# #print(a)

        #3
my_list = [20, -3, 15, 2, -1, -21]
new_list = []
for i in my_list:
    if i > 0:
        new_list.append(i)
print(new_list)

res = lambda x: [new_list.append(item) for item in my_list if item > 0]
rew = list(filter(lambda x: x > 0, my_list))
print(rew)


# def decorator(func):
#
#     def wrapper(*args, **kwargs): # (4, 5)
#         print('Делаем что-то до')
#         result = func(*args, **kwargs) # add
#         print('Делаем что-то после')
#         return result
#
#     return wrapper
#
# @decorator
# def add(a):
#     return a
#
# print(add(1))
#
# def decorator(func):
#     return lambda x:
#     def wrapper(*args, **kwargs): # (4, 5)
#         print('Делаем что-то до')
#         result = func(*args, **kwargs) # add
#         print('Делаем что-то после')
#         return result
#
#     return wrapper
#
# @decorator
# def add(a):
#     return a
#
# print(add(1))
#
# Aleksandr Matveev 21:37
# def decorator(func):
#
#     def wrapper(*args, **kwargs): # (4, 5)
#         print('Делаем что-то до')
#         result = func(*args, **kwargs) # add
#         print('Делаем что-то после')
#         return result
#
#     return wrapper
#
# @decorator
# def add(a):
#     return a
#
# print(add(1))
#
# # add_new = decorator(add)
# # result = add_new(4)
# # print(result)
