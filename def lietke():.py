def lietke(n):
    i = 2
    c = []
    while n > 1:
        if n % i == 0:
            n = n // i
            c.append(i)
        else:
            i += 1
    if len(c) == 0:
        c.append(n)
    return c

n = int(input('Nhập n: '))
if n < 0:
    print('Không hợp lệ')
else:
    print(lietke(n))
