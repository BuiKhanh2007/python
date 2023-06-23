'''Viết chương trình hỏi người dùng một số
tự nhiên n và in ra tất cả ước số của con số đó.'''
a=int(input('nhap '))
for i in range(1,a+1):
    if a%i==0:
        print(i,end=',')