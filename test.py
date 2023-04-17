def is_prime(num):
    """Kiểm tra xem một số có phải là số nguyên tố hay không."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input('Nhập n: '))
primes = []
for i in range(n):
    if is_prime(i):
        primes.append(i)
print(primes)
