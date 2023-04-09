import time as tm
c=0
while True:
    for i in range(3):
        a = input('Nhập số nguyên: ')
        if not a.isdigit():
            print('Vui lòng nhập lại số nguyên.')
        else:
            print(int(a))
            break
    else:
        c+=1
        if c==1:
            print('nhap qua 3 lan')
            tm.sleep(3)
            c=0
