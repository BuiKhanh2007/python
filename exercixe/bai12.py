def vonva(x,y,k):
  minn = min(x,y)
  count=0
  for j in range(1,minn+1):
    if x%j==0 and y%j==0:
      count+=1
    if count == k :
      return j
  return -1
x = int(input())
y = int(input())
k = int(input())
print(vonva(x,y,k))
