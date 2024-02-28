class User:
    count = 0  # Атрибут класса

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self._ban = False
        self.add_one()

    def greet(self):
        print(f'Привет, {self.get_fullname()}!')

    def get_fullname(self):
        return f'{self.name} {self.surname}'

    @staticmethod
    def function(age):
        return age > 18

    @classmethod
    def add_one(cls):
        cls.count += 1

    @property
    def ban(self):
        return self._ban

    def __str__(self):
        return self.get_fullname()


user_1 = User('John', 'Smith')
user_2 = User('Slava', 'Morozow')

print(user_1.function(20))


class User:

    count = 0 # Атрибут класса

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self._ban = False
        self.add_one()

    def greet(self):
        print(f'Привет, {self.get_fullname()}!')

    def get_fullname(self):
        return f'{self.name} {self.surname}'

    @classmethod
    def add_one(cls):
        cls.count += 1

    @property
    def ban(self):
        return self._ban

    def __str__(self):
        return self.get_fullname()


# [count, __init__ (дополнили), greet (переписали) , get_fullname, add_one, ban, __str__]
class PremiumUser(User):

    def __init__(self, name, surname, desс):
        super().__init__(name, surname)
        self.desс = desс

    def greet(self):
        print(f'***Привет, {self.get_fullname()}!***')


pr_user = PremiumUser('Mike', 'Smith', 'Всем привет!')
pr_user.greet()
pr_user.get_fullname()
print(pr_user.desс)
ghffghfg