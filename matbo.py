'''Phú Ông có đàn bò gồm n con, các con bò mang số hiệu từ 1 đến n. Bờm được Phú Ông giao
nhiệm vụ, hàng ngày, thả bò ra và chiều tối lùa bò về chuồng. Hàng ngày, khi bò về chuồng,
Bờm sẽ tính tổng các số hiệu của các con bò (S), nếu tổng S này đúng là bò về đủ. Một hôm,
do mải chơi nên Bờm đã để lạc mất 1 con bò. Để đăng tin tìm kiếm, Bờm cần xác định số hiệu
của con bò bị lạc.
Viết chương trình cho nhập 2 số nguyên n và S (với n và S được nhập đảm bảo bài
toán luôn có nghiệm), giúp Bờm xác định số hiệu của con bò bị lạc bằng 2 cách:
a. Có sử dụng lệnh lặp.
b. Không sử dụng lệnh lặp.
Ví dụ với n=5 và S=12, Bờm xác định ngay con bò bị lạc có mã số là 3.'''
def find_lost_cow_without_loop(n, s):
    # Sử dụng công thức tính tổng của dãy số từ 1 đến n: n*(n+1)//2
    # Trừ tổng s hiện tại, ta sẽ thu được số hiệu của con bò bị lạc
    lost_cow = n * (n + 1) // 2 - s

    return lost_cow

# Nhập dữ liệu đầu vào
n = int(input("Nhập số lượng bò: "))
s = int(input("Nhập tổng số hiệu của các con bò: "))

# Gọi hàm và in kết quả
lost_cow = find_lost_cow_without_loop(n, s)
print("Số hiệu của con bò bị lạc là:", lost_cow)