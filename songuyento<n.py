'''Cho nhập số nguyên dương n. Liệt kê các số nguyên tố <n.'''
c=[]
n = int(input('Nhập n: '))
def check(sumn):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for k in range(2,n-1):
    check()