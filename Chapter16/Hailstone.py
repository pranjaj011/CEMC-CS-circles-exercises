def hailstone(n):
   print(n)
   if n == 1:
      return n
   elif n%2 == 0:
      hailstone(int(n/2))
   elif n%2 != 0:
      hailstone(int(3*n)+1)
