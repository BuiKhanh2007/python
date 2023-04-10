import math as Q
def khanh(n):
    k=1
    if n==0:
        return k
    elif n<0:
        raise ValueError('nhap lai di')
    else:
        for i in range(1,n+1):
            k=i*k
        return k
while True:
    try:
        n=int(input('nhap n: '))
        khanh(n)
        d=int(input('nhap d: '))
        khanh(d)
        b=int(input('nhap b: '))
        khanh(b)
        S=khanh(n)+khanh(d)+khanh(b)
        print(S)
        break
    except Exception as e:
        print(e)