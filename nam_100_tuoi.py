'''Tạo chương trình yêu cầu người dùng nhập tên và tuổi của họ. Chương trình in ra màn hình
chuỗi (s) thông báo năm mà người đó tròn 100 tuổi.
 Gợi ý: import module datetime, sử dụng datetime.now().year của class datetime để lấy
năm hiện tại như sau: datetime.datetime.now().year'''
import datetime as dt
a=input('nhap ten: ')
age=float(input('tuoi:'))
datetimenow=dt.datetime.now().year
year=100-age
datetimeto100=datetimenow+year
print(a)
print(datetimeto100)
