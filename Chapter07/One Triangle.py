n=int(input())
b = 0
for a in range(0,n):
   X=0
   b=n-b
   for x in range(0,b):
         X=(X*10)+1
   b=n-b+1
   print(X)
