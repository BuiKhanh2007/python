import sympy as sp

# Nhập giá trị của biến a từ người dùng
a = input('Nhập phương trình: ')

# Tạo biến ký tự c trong sympy
c = sp.Symbol('x','y','z')

# Biến đổi biểu thức thành dạng hợp lệ của Python
e = sp.Eq(sp.sympify(a), 0)

# Giải phương trình
gai = sp.solve(e, c)

# In ra kết quả
print(gai)
