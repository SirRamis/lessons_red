'''Использовано 87 % доступного пространства. … Когда свободное место закончится, вы не сможете создавать, редактировать и загружать файлы. Получите 100 ГБ за 139,00 ₽ 35,00 ₽/мес. на 3 месяца.
4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
     периметр квадрата, площадь квадрата и диагональ квадрата.

4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
     в формате аргумент: значение. Например:
	name: John
	last_name: Smith
	age: 35
	position: web developer

4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
     положительные числа

4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке (my_list)
4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
     Примените эти функции в качестве методов в другом файле.

	'''


def square(a):
    p = a * 4
    s = a * a
    d = a * (2 ** 0.5)
    return p, s, d


q, w, e = square(5)
print(q, w, e)

# a = int(input())  # Вводим значение стороны квадрата
# p = a * 4  # Вычисляем периметр квадрата
# s = a * a  # Вычисляем площадь квадрата
# d = a * (2 ** 0.5)  # Вычисляем диагональ квадрата
#
# print(s, p, d)  # Выводим результаты
import math

