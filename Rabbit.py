'''
Ban đầu trong rừng có 1 cặp thỏ, biết rằng cứ sau 1 tháng thì số lượng thỏ trong rừng tăng
lên gấp đôi. Hỏi sau m tháng thì có bao nhiêu con thỏ (giả sử các con thỏ không chết).'''
m = int(input('Nhập số tháng: '))
tho = 2 ** m  # tính 2 mũ m
print(f'Sau {m} tháng, số lượng thỏ trong rừng là: {tho} con')
