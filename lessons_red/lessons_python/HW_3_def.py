def E1():
    my_list = ['a', 'b', [1, 2, 3], 'd']
    w = []
    for e in my_list:
        if isinstance(e, int):
            w.append(e)
        elif isinstance(e, list):
            for se in e:
                if isinstance(se, int):
                    w.append(se)
    print(w)

def E2():
    list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
    summ = []
    for i in list_1:
        if isinstance(i, int):
            summ.append(i)
    print(sum(summ))

    w = []
    for si in list_1:
        if isinstance(si, str) and 'a' in si:
            w.append(si)
    print(w)

def E3():
    list = ['cat', 'dog', 'horse', 'cow']
    print(tuple(list))