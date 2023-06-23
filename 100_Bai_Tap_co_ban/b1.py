'''In toàn bộ các số chẵn từ 1000 đến 2000.'''
a=[]
for i in range(1000,2001,2):
    a.append(str(i))
b=','.join(a)
print(b)