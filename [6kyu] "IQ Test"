def iq_test(numbers):
    numbers = map(int, numbers.split(' '))
    eo = []
    for n in numbers:
        if n % 2 == 0:
            eo.append('e')
        else:
            eo.append('o')
    if eo.count('e') > 1:
        return (eo.index('o')+1)
    else:
        return (eo.index('e')+1)
