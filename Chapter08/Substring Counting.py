needle=str(input())
haystack = str(input())
a = 0
for b in range(0,len(haystack)-1):
   if haystack[b:len(needle)+b]== needle:
      a = a+1
print (a)
