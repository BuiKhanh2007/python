'''Viết chương trình yêu cầu người dùng nhập vào một chuỗi 
và in ra màn hình thông báo chuỗi đó có phải là chuỗi palindrome hay không.
 (Chuỗi Palindrome là một chuỗi 
mà đọc xuôi và ngược đều như nhau, ví dụ ABCDCBA.)'''
a=input()
b=a[::-1]
a=a.upper()
if a==b:
	print('is Palindrome ')
else:
	print('not Palindrome')