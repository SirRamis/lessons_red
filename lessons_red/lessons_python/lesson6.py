class Cats:
    breed = 'Persian'
    name = 'Vasya'
    age = 2

    def jump(self):
        return "Кошка прыгает"

# print(Cats.name)
# print(Cats.breed)
# print(Cats.age)
# print(Cats.jump(899))

class Animal:

    def __init__(self, bread, age):
        self.bread = bread
        self.age = age

class Cat(Animal):
    pass

cat1 = Cat("Parish", 10)

print(cat1.age)
print(cat1.bread)