#Viết một chương trình tính giai thừa của một số nguyên dương n. Với n được nhập từ bàn phím.

#Định nghĩa giai thừa: giai thừa của 1 số là tích các số liên tiếp từ 1 đến số đó. Trường hợp đặc biệt, giai thừa của 0 và 1 là 1.

#Ví dụ, n = 8 thì kết quả đầu ra phải là 1*2*3*4*5*6*7*8 = 40320.
n=int(input("nhap n :"))
def giaithua():
    hangso=1
    if n==0 or n==1:
        return hangso
    elif n<0:
        print('khong hop le')
    else:
        for i in range(2,n):
            hangso=hangso *i
        return(hangso)
print(giaithua())