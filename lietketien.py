'''Có 9 loại tiền 1, 2, 5, 10, 20, 50, 100, 200, 500. Cho nhập số tiền X. Chuyển số tiền X ra
các loại tiền sao cho số lượng là ít nhất. In ra số tờ tiền của mỗi loại, tổng số tờ tiền của tất
cả các loại.
Ví dụ với X=1234, sẽ in ra:
So tien 1234 duoc doi thanh:
Loai 500 gom 2 to
Loai 200 gom 1 to
Loai 100 gom 0 to
Loai 50 gom 0 to
Loai 20 gom 1 to
Loai 10 gom 1 to
Loai 5 gom 0 to
Loai 2 gom 2 to
Loai 1 gom 0 to
TỔNG CỘNG CÓ 7 TỜ'''
# Các mệnh giá của tiền
tien = [500, 200, 100, 50, 20, 10, 5, 2, 1]

# Nhập số tiền X từ người dùng
X = int(input("Nhập số tiền X: "))

# Khởi tạo biến đếm tổng số tờ tiền
tong_so_to_tien = 0

# Duyệt qua từng mệnh giá tiền
for loai_tien in tien:
    # Tính số tờ tiền của mỗi loại
    so_to_tien = X // loai_tien
    # Cập nhật số tiền còn lại sau khi đổi
    X = X % loai_tien
    # In ra kết quả
    print(f"Loại {loai_tien} gồm {so_to_tien} tờ")
    # Cộng dồn số tờ tiền vào tổng số tờ tiền
    tong_so_to_tien += so_to_tien

# In ra tổng số tờ tiền của tất cả các loại
print(f"TỔNG CỘNG CÓ {tong_so_to_tien} TỜ")

    