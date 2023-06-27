def daysohanhphuc(n):
	khanh = ''
	if 0<n<=10000 and n == int(n):
		for i in range(n,0,-1):
			check=True
			for j in range(2,i):
				if i%j==0:
					check=False
					break
			if check:
				khanh+='_'+str(i)
	return khanh[1:]
print(daysohanhphuc(10))