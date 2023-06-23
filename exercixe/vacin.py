n,m = input('Nhập n và m: ').split()
m=int(m)
n=int(n)
pa,pb=input('Nhập pa va pb: ').split()
pa,pb=int(pa),int(pb)
tong_vacin_1_ngay = pa+pb
vacin_hien_co=m
ngay=0
while vacin_hien_co<n:
    vacin_hien_co+=tong_vacin_1_ngay
    ngay+=1
print(ngay)