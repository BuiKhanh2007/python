a=int(input("khanh"))
khanh=1
while a/khanh>1:
  if a % khanh != 0 :
    khanh += 1
  a=a/khanh
print(khanh)