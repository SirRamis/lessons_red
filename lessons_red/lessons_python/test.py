def check_password(x):
    """

    :param x:
    :return:
    """
    a = "!@#$%*"
    b = []  # zifri
    c = []  # spez znaki
    d = []  # zaglavnii
    #for i in x:
    if x.isdigit():
       print('ew')

    for k in x:
        if k in a:
            c += k
    print(c)

    for y in x:
        if y.isupper():
            d.append(y)
    print(d)

    if len(b) >= 10:
        return True
    print(len(b))

check_password('d24hsf!gsdgfQWE1@457#$')