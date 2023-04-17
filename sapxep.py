def bubble_sort(arr):
    n = len(arr)

    # Duyệt qua từng phần tử trong mảng
    for i in range(n):
        # Sau mỗi lần duyệt, phần tử lớn nhất sẽ đổi chỗ về cuối mảng,
        # do đó ta chỉ cần duyệt đến (n - i - 1) vị trí cuối cùng
        for j in range(0, n - i - 1):
            # Nếu phần tử hiện tại lớn hơn phần tử đằng sau nó, hoán đổi chỗ
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Ví dụ về cách sử dụng thuật toán bubble sort
arr = []
for kha in range(10):
    a=float(input('nhap a'))
    arr.append(a)
    bubble_sort(arr)
print("Mảng gốc:", arr)

print("Mảng sau khi sắp xếp:", arr)

    
    
    
    
    
