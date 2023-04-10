def songuyento():
    while True:
        try:
            c=[]
            a=int(input('Nhập số nguyên tố: '))
            if a>1:
                for i in range(2,a+1):
                    is_prime = True
                    for j in range(2, int(i**0.5) + 1):
                        if i % j == 0:
                            is_prime = False
                            break
                    if is_prime:
                        c.append(i)
                print('Các số nguyên tố từ 1 đến',a,'là:',c)
                break 
            elif a==0:
                print('Không là số nguyên tố')
            else:
                print(a,'không là số nguyên tố')
        except Exception as e:
            print('Lỗi:',e)

songuyento()
