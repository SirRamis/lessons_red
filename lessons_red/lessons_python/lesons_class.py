# class Persons:
#     def __init__(self,my_name, your_name):
#         self.my_name = my_name
#         self.your_name = your_name
#
#     def greet(self):
#         return f'Hello {your_name}, my name is {my_name}'
# person1 = Persons('Al','Ram')
# print(person1.your_name)
#
# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     def prin(self):
#         print(f'{self.first_name}')
#
#     def prin2(self):
#         print(f'{self.last_name}')
# per = Person('sdf','sdfas',45)
# print(list(per))
gender = {
    'm': 'Дорогой',
    'f': 'Дорогая'
}

a = [
    ['Ramis','Sirazetdinov', 123, 'm'],
    ['Amina','Nuriahmet',22, 'f'],
    ['Ilgiz','Kadirov', 55, 'm']
    ]
for name, lname, balance, g in a:
    text = f"{gender[g]} {name} {lname}, баланс вашего счета составляет {balance} руб."
    print(text)
print(type(a))
print(type(gender))