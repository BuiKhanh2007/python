def khanh(arr):
    n=len(arr)
    for i in range(n):
        for k in range(n,n-i-1):
            if arr[k]>arr[k+1]:
                arr[k],arr[k+1]=arr[k+1],arr[k]
khanhs=[]
while True:
    a=input('nhap a: ')
    if a=='over':
        break
    else:
        khanhs.append(float(a))
print(khanh(khanhs))