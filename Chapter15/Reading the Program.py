def getBASIC():
   b = []
   while True:
         c = input()
         b.append(c)
         if c.endswith("END")==True:
            break
   return b
