'''nhap 12 so nguyen duong la tien dien 12 thang,dua ra man hinh
a,tong tien dien ca nam va tien dien trung binh
b,thang co nhieu dien hon tien dien trung binh'''
a = [float(i) for i in input('Nhập tiền điện của 12 tháng: ').split()]

def tong_tien_dien(a):
    tong = sum(a)
    return tong

def tien_dien_trung_binh(a):
    return tong_tien_dien(a) / len(a)

def thang_nhieu_dien(a):
    tb = tien_dien_trung_binh(a)
    thang_nhieu = []
    for i in range(len(a)):
        if a[i] > tb:
            thang_nhieu.append(i + 1)  # Tháng bắt đầu từ 1, nên cộng thêm 1 vào chỉ số
    return thang_nhieu

print("Tổng tiền điện cả năm:", tong_tien_dien(a))
print("Tiền điện trung bình:", tien_dien_trung_binh(a))
print("Các tháng có tiền điện cao hơn tiền điện trung bình:", thang_nhieu_dien(a))
