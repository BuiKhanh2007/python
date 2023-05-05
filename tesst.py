khanh = [4,6,2]
for i in range(len(khanh)):
    for j in range(i+1, len(khanh)):
        if khanh[i] + khanh[j] == 6:
            print([i, j])
