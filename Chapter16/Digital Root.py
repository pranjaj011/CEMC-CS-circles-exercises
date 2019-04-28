def digitalRoot(n):
   i = digitalSum(n)
   if n < 10:
      return n
   else:
      n = digitalRoot(i)
      return n
