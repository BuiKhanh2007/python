'''Cho nhập số nguyên n. In ra cách đọc của số n.
Ví dụ: Nhập n = -105. In ra màn hình: am mot khong nam.'''
n = input('Nhập n: ')

def kiemtra(k):
    """Hàm kiểm tra và in ra cách đọc của các chữ số."""
    if k == '0':
        print('khong', end=' ')
    elif k == '1':
        print('mot', end=' ')
    elif k == '2':
        print('hai', end=' ')
    elif k == '3':
        print('ba', end=' ')
    elif k == '4':
        print('bon', end=' ')
    elif k == '5':
        print('nam', end=' ')
    elif k == '6':
        print('sau', end=' ')
    elif k == '7':
        print('bay', end=' ')
    elif k == '8':
        print('tam', end=' ')
    elif k == '9':
        print('chin', end=' ')
    elif k == '-':
        print('am', end=' ')

# Lặp qua từng chữ số của số n để in ra cách đọc
print('Cách đọc của số', n, 'là:')
for i in n:
    kiemtra(i)
