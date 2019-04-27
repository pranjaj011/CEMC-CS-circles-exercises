width = int(input())
for length in range (0, width+1):
   x = str(input())
   a = int(len(x))
   b = int((width-a)//2)
   if x == 'END':
      break
   x = ('.'*b)+x+('.'*b)
   c = len(x)
   if c <width:
      x = '.'+x
   print(x)
