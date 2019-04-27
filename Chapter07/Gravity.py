import math
v = float(input())
h= float(11000)
g =float(9.80/2)
t= (v - math.sqrt(v**2-(4*-g*h)))/(2*-g)
if t >= 0:
   print(t)
if t< 0:
   print("wrong")
