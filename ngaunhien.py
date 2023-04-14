'''Game đoán số: Chương trình tạo ra 1 số ngẫu nhiên trong khoảng từ 1 đến 9. Cho người dùng
nhập nhiều lần các số nguyên (từ 1 đến 9). Nếu người dùng đoán đúng, chương trình kết thúc,
ngược lại khi người dùng đoán sai, chương trình cho người dùng biết số mà họ đã đoán thấp
hơn hay cao hơn số kết quả và cho họ đoán lại cho đến khi đoán đúng.
a. Mở rộng 1: game sẽ kết thúc khi người dùng gõ ‘exit’.
b. Mở rộng 2: sau mỗi lần đoán sai, chương trình thông báo thêm số lần đoán thấp hơn kết quả,
số lần đoán cao hơn kết quả.'''
from random import randint
a=randint(1,9)
for i in range(10):
    k=input('hay doan so: ')
    if int(k)>10 or int(k)<0:
        print('hay nhap lai')
        continue
    if k=='exit':
        break
    if int(k)==a:
        print('chuc mung ban da doan dung')
        break
    else:
        if a<int(k):
            print('so ban nhap nho hon so can tim!')
        else:
            print('so ban nhap lon hon so can tim!')
    
    
            