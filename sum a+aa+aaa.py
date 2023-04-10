'''
Cho nhập số nguyên dương a có giá trị từ 1 đến 9. In ra tổng của a+aa+aaa.
Ví dụ: a=5  in ra 5 + 55 + 555 = 615
 Gợi ý: sử dụng phép nối chuỗi các số nguyên (vd: với a=5: "%s%s" % (a,a) => 55)
và hàm int (đổi kiểu dữ liệu từ chuỗi sang số nguyên).
'''
a=float(input('nhap a'))
if a<0 or a>9:
    print('loi')
else:
    a=int(a)
    c= int('%s'%(a)) + int('%s%s'%(a,a)) + int('%s%s%s'%(a,a,a))
    print(f'{a} + {a}{a} + {a}{a}{a} = {c}')