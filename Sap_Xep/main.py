from tkinter import *
from data import PointSchool

root = Tk()
root.title("Get Point NamDinhEdu2023")
root.minsize(height=500, width=450)

Ten_Truong = {'HHA': 40, 'VVH': 46,'NK':12,'NH':14,'NQ':15,"THD":17,'ML':18,'TVL':19,'LTV':20,'HVT':21,'NDT':22,'NB':23,"TVT":24,'MT':25,'PVN':26,'DA':27
,'LNT':28,'DHL':29,"LTT":30,"NT":31,"ND":32,"TVB":33,'TN':35,"TNB":36,"LQD":37,'NT':38,"HHB":41,'HHC':42,'TL':43,"TQT":44,'AP':45,'GT':50,'GTB':51,
'GTC':52,'QL':53,'XT':55,'XTB':56,"XTC":57,'NTT':58,'NHA':60,'NHB':61,'NHC':62,'TNT':63,"NM":64,'QT':72,"TT":76}
TenTruong = StringVar()
ID = StringVar()
SBD = IntVar()
SBDEND = IntVar()

def CSVNOSORT():
	if TenTruong.get() not in Ten_Truong:
		a='Tên Trường Không Đúng!'
		a2=' Lưu Ý: Tên Trường Nhập Vào Là Viết Tắt Ví Dụ VVH(Vũ Văn Hiếu)'
		log(a)
		log(a2)	
	if entry.get() == "0":
		with open("Vu_Hieu.csv", "w") as file:
			for x in range(int(Ten_Truong[TenTruong.get()]*10000), int(int(Ten_Truong[TenTruong.get()]*10000)+int(1000))):
				new = PointSchool(
				url="https://namdinh.edu.vn/",
				sbd=str(x),
				).method()
				formatted_entries = [entry.replace(',', '.') for entry in new]
				file.write(','.join(formatted_entries) + '\n')
				log(formatted_entries)

	else:
		with open("diem_thi.csv", "w") as file:
			for x in range(int(Ten_Truong[TenTruong.get()]*10000), int(int(Ten_Truong[TenTruong.get()]*10000)+int(SBDEND.get()))):
				new = PointSchool(
				url="https://namdinh.edu.vn/",
				sbd=str(x),
				).method()
				formatted_entries = [entry.replace(',', '.') for entry in new]
				file.write(','.join(formatted_entries) + '\n')
				log(formatted_entries)
def TraSoBaoDanh():
	new = PointSchool(
				url="https://namdinh.edu.vn/",
				sbd=str(SBD.get()),
				).method()
	log(new)


Label(root, text="App Lấy Điểm Thi Tuyển Sinh Của Trường Học Tại Nam Định").grid(row=0, columnspan=1)
lsbox = Listbox(root, height=16, width=60)
lsbox.grid(row=1)

def log(message):
	lsbox.insert(END, message)  # Thêm log vào cuối danh sách
	lsbox.see(END)  # Cuộn đến cuối danh sách
	root.update()  # Cập nhật giao diện người dùng
log('Lấy Điểm Thi Tuyển Sinh Nam Định')
log('Hướng Dẫn ==>')
log('Phần SBD Các Bạn Có Thể Ghi Số Báo Danh Của Mình Để Tra ngay ')
log('Điểm lần lượt là Văn Toán Anh')
log('Tên Trường Và Số Học Sinh Là Phần Để Tạo File CSV(Excel)')
log('LƯU Ý!CHẠY CÁI CSV LÀ KHÔNG DỪNG LẠI ĐƯỢC :)))')
log("oke hết hướng dẫn")
Label(root, text="Nhập Tên Trường: ").place(x=30, y=360)
Entry(root, font="Arial", fg='red', textvariable=TenTruong).place(x=150, y=360)

Label(root, text="Nhập SBD: ").place(x=30, y=330)
Entry(root, font="Arial", fg='red', textvariable=SBD).place(x=150, y=330)

Label(root, text="Nhập Số Học Sinh(Nếu có thì tool chạy nhanh hơn): ").place(x=30, y=390)
entry = Entry(root, font="Arial", fg='red', textvariable=SBDEND)
entry.place(x=150, y=410)

button = Frame(root)
Button(button, text='Tạo File CSV: ', command=CSVNOSORT).pack(side="left")
Button(button, text='Tra Số Báo Danh ',command=TraSoBaoDanh).pack(side="left")
Button(button, text='Thoát :))', command=root.quit).pack(side="left")
button.place(x=30, y=450)

root.mainloop()
