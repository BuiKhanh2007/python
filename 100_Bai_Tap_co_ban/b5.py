''' Viết chương trình chấp nhận một chuỗi số,
phân tách bằng dấu phẩy từ giao diện điều khiển,
tạo ra một List  và một tuple chứa mọi số.'''
a=[int(i) for i in input('nhap a').split(',')]
print(a)
print(tuple(a))