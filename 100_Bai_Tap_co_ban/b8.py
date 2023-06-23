'''Viết một chương trình nhập vào một danh sách các số và
tạo một danh sách mới chỉ gồm phần tử đầu tiên và cuối cùng của danh sách đó
. Viết chương trình sử dụng hàm.

Ví dụ, nhập vào danh sách [5, 10, 15, 20, 25] thì kết quả trả về là danh sách [5, 25]'''
def cc(n):
    return [n[0],n[-1]]
n= input('nhap n').split(',')
print(cc(n))