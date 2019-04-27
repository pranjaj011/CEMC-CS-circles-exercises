import math
L = float(input())
A = float(input())
cosA= L*math.cos(A)
for X in range (0, 10):
   T= 0+X 
   a = L*math.cos(A*(math.cos(T*(math.sqrt(9.8/L)))))-cosA
   print(a)
