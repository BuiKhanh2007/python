'''
Bài 2. Viết một chương trình có thể tính giai thừa của một số cho trước.
 Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy.
  Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
  '''
khanh=1
n=int(input())
for i in range(1,n+1):
	khanh*=i
print(str(khanh))
