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


