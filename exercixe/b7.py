'''nhap tt ban phim vd 4 5 6 7 8  tra ve a[i-1] < a[i] > a[i+1]'''
a=[int(i) for i in input('nhap a').split(',')]
b=0
for i in range(len(a)):
    if a[i-1] < a[i] > a[i+1] :
        b+=1
print(b)
        