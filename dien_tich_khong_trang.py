'''Cho hình vuông ngoại tiếp hình tròn
như hình minh họa.Viết chương trình cho
nhập bán kính hình tròn (r) là 1 số thực có
giá trị lớn hơn 0, tính phần diện tích có
màu đậm trong hình.'''
from math import pi
r=float(input('nhap ban kinh: '))
if r>0:
    dien_tich_hinh_vuong=(r*2)**2
    dien_tich_hinh_tron=pi*r**2
    ket_qua=dien_tich_hinh_vuong-dien_tich_hinh_tron
    print(f'ket qua: {ket_qua}')