import math
n=int(input())
for a in range(0,n):
  b = int(math.sqrt(a))
  if (b==0):
   continue
  if (b != math.sqrt(a)):
   continue
  if (b== math.sqrt(a)):
   print(b*b)
