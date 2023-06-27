''' Viết chương trình Python tính trung bình cộng
 của cả danh sách, trung bình cộng các phần tử dương 
 trong danh sách.'''
a=[1,2,-4,3,-5,-1]
khanh=0
for i in a:
	if i>0:
		khanh+=i
print(khanh)
