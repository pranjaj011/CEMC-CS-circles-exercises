import math
def choose(n, k):
   possibilities = (math.factorial(n)/(math.factorial(n-k)*math.factorial(k)))
   return possibilities
