'''Định nghĩa một class có ít nhất 2 method:

getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.
printString: in chuỗi vừa nhập sang chữ hoa.
Thêm vào các hàm kiểm tra đơn giản để kiểm tra method của class.

Ví dụ: Chuỗi nhập vào là quantrimang.com thì đầu ra phải là: QUANTRIMANG.COM

Gợi ý:

Sử dụng __init__ để xây dựng các tham số.'''
class InputOutString(object):
   def __init__(self):
       self.s = ""

   def getString(self):
       self.s = input("Nhập chuỗi:")
# Code by Quantrimang.com
   def printString(self):
       print (self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()