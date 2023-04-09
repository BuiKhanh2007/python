import math
import time as tm
#Viết chương trình lấy một list các con số (Ví dụ: a = [2, 4, 6, 8, 10]) và tạo một list mới chỉ gồm các phần tử đầu tiên và cuối cùng của list đã cho. Lưu ý: Viết code này bên trong một hàm.
def list_ends(arr):
    return [arr[0], arr[-1]]
 
 #: Tạo một chương trình hỏi người dùng một con số và in ra tất cả ước số của con số đó.
def uocso(): #tu lam 
    n=int(input('nhap n: '))
    uocso=[]
    for i in range(1,n+1):
        if n%i==0:
            uocso.append(i)
    print(uocso)
def dapan_uocso():
    try:
        number = int(input("Please choose a number to divide: "))
    except ValueError:
        print("We only accept integers.")
        exit(0)

    if number == 0:
        print("All non-zero integers are divisors of 0")
        exit(0)

    # Accept both negative and positive number
    # Disivors can be negative or postive as well
    divisors = []
    for i in range(1, abs(number) + 1):
        if number % i == 0:
            divisors.extend([i, -1 * i])

    print(divisors)
def khanh():
    #Viết một chương trình in ra tất cả các phần tử có giá trị nhỏ hơn 5. Ngoài ra, bạn có thể làm thêm các yêu cầu sau:
    #Thay vì in từng phần tử một, hãy in ra một list mới có tất cả các phần tử nhỏ hơn 5 từ list a ban đầu.
    #Khi hỏi thêm người dùng một con số khác (số X), chương trình có thể trả lại một list mới có chứa các phần tử nhỏ hơn X từ list a ban đầu
    a=0
def chuvi_dientich():
    #Viết chương trình Python nhập vào ba số a,b,c bất kì. Kiểm tra xem 3 số đó có thể  là độ dài ba cạnh tam giác hay không, nếu  không  thì in  ra màn  hình  ‘ Không tạo thành tam giác’. Ngược lại, tính chu vi và diện tích tam giác đó.
    a=float(input('nhap a: '))
    b=float(input('nhap b: '))
    c=float(input('nhap c: '))
    if a+b>c and a+c>b and b+c>a:
        p=(a+b+c)/2
        dientich=math.sqrt(p*(p-a)*(p-b)*(p-c))
        print('chuvi:',p*2,'dien tich:',dientich)
    else:
        print('khong tao thanh tam giac')
def solonnhat():
    #Viết chương trình Python tìm giá trị lớn nhất trong 3 số a, b, c bất kì nhập từ bàn phím
    a=float(input('nhap a: '))
    b=float(input('nhap b: '))
    c=float(input('nhap c: '))
    solonnhat= max(a,b,c)
    print((solonnhat))
    print(type(solonnhat))
def sonhonhat():
    #Viết chương trình Python tìm giá trị nhỏ nhất trong 4 số a, b, c, d bất kì nhập từ bàn phím
    a=float(input('nhap a: '))
    b=float(input('nhap b: '))
    c=float(input('nhap c: '))
    d=float(input('nhap d: '))
    so_nho_nhat= min(a,b,c,d)
    print((so_nho_nhat))
def bang_cuu_chuong():
    # Viết chương trình Python in bảng cửu chương từ bảng 2 đến bảng 9
    for i in range(2, 10):
        for a in range(1, 11):
            c = i * a
            print('%i nhan %i bang %i' % (i, a, c), end="   ")
        print("\n") # thêm dòng trống sau khi hoàn thành mỗi bảng cửu chương
def tong_1_phangiaithua():
    # Viết chương trình Python tính S=1+1/2!+1/3!+…+1/n!
    n = int(input('Nhap n: '))
    S = 1 # bắt đầu với 1, tương ứng với i = 1
    giaithua = 1 # bắt đầu với 1!, tương ứng với i = 1
    for i in range(2, n+1):
        giaithua *= i
        S += 1/giaithua
    print("Tong cua day so la: ", S)
    n=int(input("nhap n :"))
def giaithua():
    n=int(input('nhap n: '))
    hangso=1
    if n==0 or n==1:
        return hangso
    elif n<0:
        print('khong hop le')
    else:
        for i in range(2,n):
            hangso=hangso *i
        return(hangso)
def chanle():
    a=int(input('nhap 1-9'))
    for i in range(0,a):
        if i%2!=0:
            print(i,end=' ')
def sogiochuan():
    gio_vuot_chuan = int(input('cccc'))
    so_gio_lam=float(input('time'))
    gio_tieu_chuan=44
    gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
    print(gio_vuot_chuan)
def sochan10002000():
    for i in range(1000,2001):
        if i%2==0:
            print(i)
def chiahet7():
    k=[]
    #Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.
    for i in range(2000,3201):
        if i%7==0 and i%5!=0:
            k.append(i)
            print(',',k)
            '''
    def chiahet7():
    k = []
    # Tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, trong đoạn từ 2000 đến 3200 (bao gồm cả 2000 và 3200).
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            k.append(i)

    # In chuỗi kết quả, các số được cách nhau bằng dấu phẩy
    print(','.join(map(str, k)))
    '''
def giaithua():
    #Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
    c=int(input('nhap i:'))
    a=1
    for i in range(1,c+1):
        a*=i
    print(a)
    '''
    n = int(input("Nhập số cần tính giai thừa:"))
    def fact(n):
        if n==0:
        return 1
        else:
        return n*fact(n-1)
        print(fact(n))
        n = int(input("Nhập số cần tính giai thừa:")) def fact(n): if n==0: return 1 else: return n*fact(n-1) print(fact(n))
        n = int(input("Nhập số cần tính giai thừa:")) 
        def fact(n):
            if n==0:
                return 1
            else:
                return n*fact(n-1)
        print(fact(n))
    '''
def tinhtuoi():
    #Tạo một chương trình yêu cầu người dùng nhập tên và tuổi của họ. Gửi lại họ một tin nhắn cho biết năm họ sẽ tròn 100 tuổi.
    ten=input('nhap ten: ')
    tuoi=int(input('nhap tuoi cua ban: '))
    namtron100=100-tuoi
    print('chao',ten,'bansong',namtron100)
def sapxep():
    #Tạo một chương trình hỏi người dùng một con số và in ra tất cả ước số của con số đó.
    a=int(input('nhap a'))
    c=[]
    for i in range(0,a):
        if i%2==00:
            c.append(i)
    print(c)
def lessthanten():
    '''
     Lấy một list, ví dụ như sau:
a = [1, 1, 2, 3, 5, 9, 12, 23, 35, 56, 88]
Viết một chương trình in ra tất cả các phần tử có giá trị nhỏ hơn 5. Ngoài ra, bạn có thể làm thêm các yêu cầu sau:

Thay vì in từng phần tử một, hãy in ra một list mới có tất cả các phần tử nhỏ hơn 5 từ list a ban đầu.
Khi hỏi thêm người dùng một con số khác (số X), chương trình có thể trả lại một list mới có chứa các phần tử nhỏ hơn X từ list a ban đầu
    '''
    a=[]
    for g in range(0,6):
        s=(input('nhap s: '))
        if s.isdigit():
            s=float(s)
            a.append(s)
    print(a)
    def gtnho5():
        c=[i for i in a if i<5]
        print(c)
    gtnho5()
    k=float(input('nhap k: '))
    def nhapthemX():
        c=[i for i in a if i<5]
        b=[z for z in c if z<k]
        print(b)
def nhapsai3lan():
    #nhap sai3 lan se khoa 3s
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



