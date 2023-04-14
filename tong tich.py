def tinh_tong_tich_chu_so(n):
    tong = 0
    tich = 1
    for chu_so in str(n):
        so = int(chu_so)
        tong += so
        tich *= so
    return tong, tich

# Nhập số nguyên dương n từ người dùng
n = int(input("Nhập số nguyên dương n: "))

# Gọi hàm để tính tổng và tích các chữ số của n
tong, tich = tinh_tong_tich_chu_so(n)

# In kết quả ra màn hình
print("Tổng các chữ số của", n, "là:", tong)
print("Tích các chữ số của", n, "là:", tich)

