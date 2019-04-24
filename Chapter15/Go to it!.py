def findLine(prog, target):
   a =[]
   for i in range(len(prog)):
     a = (prog[i].split())
     if a[0] == target:
        return i
