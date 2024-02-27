class Person:
    def __init__(self, ase, fname, lname):
        self.ase = ase
        self.fname = fname
        self.lname = lname

person_1 = Person("tytyt", 'Ramis', 'Sir')
print(person_1.ase)
print(person_1.fname)
print(person_1.lname)

def check_logs(log) -> int:
    if len(log)== 0:
        return 0
    elif len(log) == 1:
        return 1
    count_day = 1
    for k in range(1,len(log)):
        if log[k-1] >= log[k]:
            count_day += 1
    return count_day
log = ['234','345','456','0 45','434','333']
print(check_logs(log))