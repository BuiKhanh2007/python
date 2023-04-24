
#code em tao trong chu nhat :)))
#ai muon lay nguon thi ok nha

from tkinter import *

#tao cua so
root = Tk()
root.geometry('300x200')
root.title('make by khanh')
#tao label
label=Label(root,text='Tinh tong cua 2 so\nDay la lan dau tien minh tao cai nay :))')
label.pack(side='top')
label=Label(root,text='nhap so thu nhat: ')
label.place(y=40)
label1=Label(root,text='nhap so thu hai: ')
label1.place(y=65)
#tao entry
entry=Entry(root,font=('Times New Roman',10))
entry.place(x=120,y=40)

entry1=Entry(root,font=('Times New Roman',10))
entry1.place(x=120,y=65)

def tonghaiso():
    label3=Label(root,text=f'ket qua la:' + str(float(entry.get()) +  float(entry1.get())),bg='yellow')
    label3.place(x=135,y=95)

#tao nutbam
button=Button(root,text='ket qua',height=1,width=4,bg='green',command=tonghaiso)
button.place(x=20,y=90)
root.mainloop()