'''Viết chương trình giải phương trình bậc hai
ax2+bx+c=0 với a, b, c
là số nguyên và được nhập vào từ bàn phím.'''
a,b,c=map(float,input('nhap a,b,c').split())
delta = b**2-4*a*c
if delta < 0:
    print('pt vo jnghiem')
else:
    x1=(-b+delta**0.5)/2*a
    x2=(-b-delta**0.5)/2*a
    print('pt co nghiem',x1,x2)