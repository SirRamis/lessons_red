# def sum_it(a, b, c):
#     return a + b + c
#
#
# print(sum_it(5, 4, c=10))


def decorator(func):
    def wrapper(*args):
        print('эта функция')
        print(f'wrap func : {func.__name__}')
        print('wrap')
        print(func(*args))
        print('konex')
    return wrapper

@decorator
def my_wrapper(item):
    return f'{item} is wrapped'
my_wrapper('lalala')
def kwa(**kwargs):
    print(type(kwargs))
    print(kwargs)
kwa(name='ram', lname='smit',posit='sfsd')

res = lambda x, y: x*y
print(res(5,5))