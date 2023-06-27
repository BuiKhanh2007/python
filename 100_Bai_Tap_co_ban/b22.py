'''cho a,a1,a2,a3,an là dãy số hạnh phúc nếu nó thỏa mãn:
là dãy số giảm dần với mỗi ai hoặc là số nguyên tố hoặc ước 
 của 1 trong các số từ a1 đến ai-1
lập trình dãy số hạnh phúc dài nhất bắt đầu từ n<=10000 
với n là số nguyên dương cho trước
10 					10_7_5_3_2_1
45 				45_43_41_37_31_29_27_19_17_13_11_9_7_3_2_1
81
100   					'''
def daysohanhphuc(n):
    khanh = ''
    if 0 < n <= 10000 and n == int(n):
        for i in range(n, 0, -1):
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                khanh += '_' + str(i)
    return khanh[1:]  # Bỏ đi ký tự '_' đầu tiên
print(daysohanhphuc(5))
