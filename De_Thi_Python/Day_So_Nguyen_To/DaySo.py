'''cho a,a1,a2,a3,an là dãy số hạnh phúc nếu nó thỏa mãn:
là dãy số giảm dần với mỗi ai hoặc là số nguyên tố hoặc ước 
 của 1 trong các số từ a1 đến ai-1
lập trình dãy số hạnh phúc dài nhất bắt đầu từ n<=10000 
với n là số nguyên dương cho trước
10 					10_7_5_3_2_1
45 				45_43_41_37_31_29_27_19_17_13_11_9_7_3_2_1
81
100   					'''
import sys
def daysohanhphuc(n):
    khanh = ''
    if 0 < n <= 10000 and n == int(n):
        for i in range(n, -1, -1):
            check = True
            for j in range(2,int(i**0.5)+1):
                if i % j == 0:
                    check = False
                    break
            if check:
                khanh += '_' + str(i)
    return khanh[1:]

fi = open('khanh.txt')
fo = open('khanhout.txt','w')
sys.stdin = fi 
sys.stdout=fo
n=int(input())
result=daysohanhphuc(n)
sys.stdout.write(result)
fo.close()
