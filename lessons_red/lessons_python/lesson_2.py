# '''
# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
#
# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным. Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”
#
# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным. Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600). Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)
#
# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно. Текст и количество повторений нужно ввести с помощью input()
#
# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str), производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}
# '''
#
#        #1
def zdorovie():
    if z <= 0:
        return False
    return True
z = 0
print(zdorovie())

       #2
def chetnoe():
    if i % 2 == 0:
        return 'Четное'
    return 'Нечетное'
i = 21
print(chetnoe())

      3
def visokisny():
a = 200
if a % 4 == 0 or a % 400 == 0 and a % 400 != 0:
    print(a)


         #4
def text():
    t = input()
    x = int(input())
    for _ in range(x):
        #return text()
        print(t)
text()
       #5
# def colculator():
#     return

num1 = int(input())
num2 = int(input())
operator = input()

if operator == '+':
    result = num1 + num2
    print(f'{num1} {operator} {num2} = {result}')
if operator == '-':
    result = num1 - num2
    print(f'{num1} {operator} {num2} = {result}')
if operator == '*':
    result = num1 * num2
    print(f'{num1} {operator} {num2} = {result}')
if operator == '/':
    result = num1 / num2
    print(f'{num1} {operator} {num2} = {result}')
