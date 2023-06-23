def calculate_fence_length(m, n):
    # Tính tổng độ dài các cạnh nằm ở biên của khu đất
    fence_length = 2 * (m + n)

    # Tính độ dài của hàng rào đi qua các hàng và cột bên trong
    fence_length += (m - 1) * n + (n - 1) * m

    return fence_length


# Đọc dữ liệu từ file FENCES.INP
with open('FENCES.INP', 'r') as file:
    data = file.readline().split()
    m = int(data[0])
    n = int(data[1])

# Tính tổng độ dài cần rào
total_fence_length = calculate_fence_length(m, n)

# Ghi kết quả vào file FENCES.OUT
with open('FENCES.OUT', 'w') as file:
    file.write(str(total_fence_length))
