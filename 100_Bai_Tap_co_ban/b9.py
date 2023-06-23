'''Viết một hàm nhận vào ba số thực và trả về số lớn nhất trong ba số.
Lưu ý, không sử dụng hàm max() của Python.'''
a, b, c = map(float,input('Nhập a, b, c: ').split())
maxx = a
if maxx<b:
    b=maxx
if maxx<c:
    c=maxx
print(maxx)
