def persistence(n):
    if n < 10:
        return 0
    count = 1
    n = str(n)
    for i in n:
        count*=int(i)
    return 1 + persistence(count)
