class print_initials():

    def __init__(self, name, surname, middlename):
        self.name = name
        self.surname = surname
        self.middlename = middlename

    def print_all(self):
        print()

def print_initials(name, surname, middlename):
    print(name.capitalize())

print_initials('rbt','rtg','rtg')