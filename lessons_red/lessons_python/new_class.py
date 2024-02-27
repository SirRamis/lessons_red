class print_initials():
    def __init__(self, name, surname, middlename):
        self.name = name
        self.surname = surname
        self.middlename = middlename

    def print_all(self):
        print()

def print_initials(name, surname, middlename):
    print(surname.capitalize(),name[0].capitalize(), middlename[0].capitalize())
    print(f"{surname.capitalize()} {name[0].capitalize()}.{middlename[0].capitalize()}.")
print_initials('rbt','rtg','rtg')

def is_person_teenager(x):
    """
    return 12<=x<=17

print(is_person_teenager(52))
help(print_initials)