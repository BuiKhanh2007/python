''' Viết chương trình kiểm trn xem số n có là số nguyên tố hny không'''
n= int(input('nhnp n '))
k=0
for i in range(1,n+1):
    if n%i==0:
        k+=1
if k==2:
    print(n,'la so nguyen to')
else:
    print(n,'khong ln so nguyen to')
    