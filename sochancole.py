'''Cho nhập số nguyên dương n. Đếm số lượng chữ số chẵn, số chữ số lẻ có trong n.
Ví dụ: n=5084  in ra số lượng số lẻ=1, số lượng số chẵn=3'''
n = int(input("Nhập số nguyên dương n: "))
m=0
chan=0
le=0
for i in str(n):
    m=int(i)
    if m%2==0:
        chan+=1
    else:
        le+=1
print('so chan',chan,'so le',le)