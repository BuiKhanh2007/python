'''Viết chương trình cho người dùng nhập 1 chuỗi (S). Xuất ra vị trí của từng ký tự có trong
chuỗi
Ví dụ: S= “Sài Gòn”, xuất ra
Ký tự S xuất hiện tại vị trì 0
Ký tự à xuất hiện tại vị trí 1
Ký tự i xuất hiện tại vị trí 2
Ký tự
xuất hiện tại vị trí 3
Ký tự G xuất hiện tại vị trí 4
Ký tự ò xuất hiện tại vị trí 5
Ký tự n xuất hiện tại vị trí 6'''
a=input('nhap a: ')
for i in range(len(a)):
    print('Ký tự', a[i], 'xuất hiện tại vị trí', i)