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