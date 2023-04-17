'''Cho nhập n. Tính tổng S (hoặc tích
******* CHƯƠNG TRÌNH TÍNH TỔNG TÍCH ********
P) trong các trường hợp sau. Yêu
0.- Nhập n
cầu thực hiện:
1.- Tính S = 1 + 2 + 3 + ... + n
- Tạo menu cho bài tập có dạng
2.- Tính S = 1 + 3 + 5 + ... + (2n+1)
như hình sau. Tùy vào chức
3.- Tính S = 1 + 1/2 + 1/3 + ... + 1/n
4.- Tính S = 1/2 + 1/3 + 1/4 + ... + 1/(n+1)
năng được chọn, chương trình
5.- Tính S = 1/2 + 1/4 + 1/6 + ... + 1/(2n)
sẽ gọi hàm thực hiện tính toán
6.- Tính S = (1) + (1+2) + (1+2+3) + ... + (1+2+3+... +n)
tương ứng.
7.- Tính P = 1 * 2 * 3 * ... * n
- Sử dụng lệnh for và hàm range()
8.- Tính P = (1) * (1+2) * (1+2+3) * ... * (1+2+3+... +n)
để thực hiện tính toán.
9.- Kết thúc chương trình
- Mở rộng: sử dụng lệnh while để Chọn chức năng cần thực hiện (0-9): _
thực hiện tính toán thay cho lệnh
for.'''
def bai6(n):
    tong = 0
    for i in range(1, n + 1):
        tong += i * (i + 1) // 2
    return tong

def bai7(n):
    tong = 1
    for i in range(1, n + 1):
        tong *= i
    return tong

def bai8(n):
    tong_2 = 0
    tong = 1
    for i in range(1, n + 1):
        tong_2 += i
        tong *= tong_2
    return tong

k = input('Nhập k (1 - 3): ')
n = int(input('Nhập n: '))
if k == '1':
    print('Tổng của dãy là:', bai6(n))
elif k == '2':
    print('Tích của dãy là:', bai7(n))
elif k == '3':
    print('Tích của dãy là:', bai8(n))
else:
    print('Nhập sai giá trị k!')


    