'''Viết một chương trình có thể tính giai thừa của một số cho trước
. Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy.
Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

a = 8
result = factorial(a)
print(result, end=',')
