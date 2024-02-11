def paperwork(n, m):
    # Happy Coding! ^_^
    if n <= 0 or m <= 0:
        return 0
    return n * m

def even_or_odd(number):
    number = int(input())
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
print(even_or_odd())