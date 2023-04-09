lan=0
i=0
while True:
    try:
        n  = int(input('nhap n: '))
        while i <= n:
            if i % 2 == 0:
                print(i,end=' ')
            i += 1
        break
    except ValueError:
        print('nhap lai')
        lan=lan+1
        if lan==3:
            print('qua 3 lan')
            break