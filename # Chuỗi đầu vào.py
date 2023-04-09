import sympy as sp
file=open('vd3')
file.read();
print(file)
a= input('nhap: ')
x=sp.Symbol('x y')
khanh=sp.sympify(a)
nghiem=sp.solve(khanh)
print(nghiem)
file.close()