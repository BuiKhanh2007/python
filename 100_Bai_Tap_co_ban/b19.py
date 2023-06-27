'''Viết chương trình Python đếm số lượng 
các số hạng dương và tổng của các số hạng dương.'''
a=[4,5,-6,2,655,2,6,3]
khanh=0
soluong=0
for i in a:
	if i > 0:
		soluong+=1
		khanh+=i
print(soluong,khanh)