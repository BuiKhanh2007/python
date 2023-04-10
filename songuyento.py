def songuyento():
    while True:
        try:
            c=[1,]
            a=int(input('nhap so nguyen to: '))
            if a>0:
                for i in range(1,a+1):
                    if i%a==0:
                        c.append(i)
                print('cac so nguyen to',c)
                break 
            elif a==0:
                print('khongla so nguyen to')
            else:
                print(a,'khong la so duong')
        except Exception as e:
            print('loi:  ',e)
songuyento()