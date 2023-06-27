#caculator
import re 
def tong():
	a = [float(i) for i in input('Nhập Giá Trị Cách Nhau Bởi Dấu Cách: ').split()]
	print(sum(a))
def tinhtoanbinhthuong():
	a = input('Nhập Phép Tính: ')
	re.split(r'+-*/',a)
	for i in a()
