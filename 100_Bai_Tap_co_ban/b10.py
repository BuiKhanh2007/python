'''Viết chương trình yêu cầu người dùng nhập vào một chuỗi
và in ra màn hình thông báo chuỗi đó có phải là chuỗi palindrome
hay không. (Chuỗi Palindrome là một chuỗi mà đọc xuôi và ngược đều
như nhau, ví dụ ABCDCBA.)

'''
a=input('nhap chuoi')
a.upper()
khanh=0
for i in range(len(a)):
    if a[i]!=a[-(i+1)]:
        khanh+=1
if khanh ==0:
    print('day la Palindrome')
else: print('day khong la Palindrome')
    