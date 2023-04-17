'''(Theo Wikipedia) Lucky Number (số may mắn) là số được định nghĩa theo quá trình
sau: bắt đầu với số nguyên dương x và tính tổng bình phương y các chữ số của x, sau đó tiếp
tục tính tổng bình phương các chữ số của y. Quá trình này lặp đi lặp lại cho đến khi thu được
kết quả là 1 thì dừng (tổng bình phương các chữ số của số 1 chính là 1) hoặc quá trình sẽ kéo
dài vô tận. Số mà quá trình tính này kết thúc bằng 1 gọi là số may mắn. Số có quá trình tính
kéo dài vô tận là số không may mắn hay còn gọi là sad number (số đen đủi)
- Ví dụ: 7 là số may mắn vì
72 = 49
42 + 92 = 97
92 + 72 = 130
12 + 32 + 02 = 10
12 + 02 = 1
- Minh họa những số may mắn dưới 500 là: 1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79,
82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 203, 208, 219, 226,'''
def sum_of_squares(n):
    """Hàm tính tổng bình phương các chữ số của một số nguyên dương n."""
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit ** 2
        n //= 10
    return sum


def is_lucky_number(n):
    """Hàm kiểm tra xem một số nguyên dương n có phải là số may mắn."""
    visited = set()  # Dùng set để lưu các số đã được kiểm tra
    while n != 1 and n not in visited:
        visited.add(n)
        n = sum_of_squares(n)
    return n == 1


# In ra các số may mắn từ 1 đến 500
start = 1
end = 500
print("Các số may mắn từ", start, "đến", end, "là:")
for i in range(start, end + 1):
    if is_lucky_number(i):
        print(i)
