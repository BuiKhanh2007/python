'''Viết chương trình tính số Fibonacci thứ n,
với n nhập vào từ bàn phím.'''
# find fibonacci number
n = int(input("Enter a number: "))
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(n))