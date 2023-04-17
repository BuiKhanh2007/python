'''Cho nhập số nguyên dương n. Kiểm tra xem n có phải là số nguyên tố hay không'''
n = int(input('Nhập n: '))
is_prime = True  # Giả sử ban đầu n là số nguyên tố

if n <= 1:  # Xét trường hợp n <= 1
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):  # Chỉ cần xét từ 2 đến căn bậc hai của n
        if n % i == 0:
            is_prime = False  # Nếu n chia hết cho i thì không phải số nguyên tố
            break

if is_prime:
    print(f'{n} là số nguyên tố.')
else:
    print(f'{n} không phải số nguyên tố.')
