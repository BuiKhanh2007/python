n=int(input('nhap sochiec banh: '))
k=int(input('nhap so chiec banh chien 1 luc: '))
nmax,kmax=10**6,10**6
time=3
chienbanh=True
def chienbanh(n,k):
    if n%k==0:
        tong= n/k * 2 * time
        return tong
    else:
        nguyen = n//k
        du = n%k
        tong=nguyen*time*2+du*3*2
        return tong
print(chienbanh(n,k))