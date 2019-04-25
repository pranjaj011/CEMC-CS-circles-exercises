def choose(n, k):
   first = 1
   second = 1
   third = 1
   for i in range (n):
      first = first* (n-i)
   for x in range (k):
      second = second*(k-x)
   for a in range (n-k):
      third *= (n-k) - a
   solution = first/(second*third)
   return solution
