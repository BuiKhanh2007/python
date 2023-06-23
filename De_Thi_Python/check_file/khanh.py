
run = True
while run:
    a=input("nhap ten tep ")
    if len(a)>3 and a[-3:]=='.py' and a.count('.')==1:
        print('This is python file!')
        break
    else:
        print('This is not python file!')