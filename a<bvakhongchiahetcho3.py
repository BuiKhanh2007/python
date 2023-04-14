'''Cho nhập 2 số nguyên a, b (a<b). In ra các số nằm trong khoảng từ a đến b và bỏ qua các số
chia chẵn cho 3 thuộc đoạn [a, b].
 Yêu cầu: thực hiện bằng 2 cách:
- Cách 1: dùng lệnh (statement) if.
- Cách 2: dùng lệnh continue.'''
a = int(input("a: "))
b = int(input("b: "))
z=[]
for i in range(a,b+1):
    if i%3==0:
        continue
    z.append(i)
print(z)
    