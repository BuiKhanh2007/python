'''Cho hình vuông nội tiếp hình tròn như
hình minh họa.Viết chương trình cho 
nhập bán kính hình tròn (r) là 1 số thực có giá trị lớn hơn 0, tính phần diện tích có
màu đậm trong hình.'''

from math import pi,sqrt
r=float(input('nhap ban kinh: '))
if r>0:
    dien_tich_hinhf_tron=pi * r**2
    canh=sqrt(r**2+r**2)
    dien_tich_hinh_vuong=canh**2
    ket_qua=dien_tich_hinhf_tron-dien_tich_hinh_vuong
    print(ket_qua)
else:print('loi')