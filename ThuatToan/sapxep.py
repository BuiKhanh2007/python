khanh=[]
for i in range(3):
    a=float(input(f'nhap {i}: '))
    khanh.append(a)
for i in range(len(khanh)):
    for j in range(i+1,len(khanh)):
        if khanh[i]<khanh[j]:
            khanh[i],khanh[j]=khanh[j],khanh[i]
print(khanh)