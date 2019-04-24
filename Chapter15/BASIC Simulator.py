def getBASIC():
   b = []
   while True:
         c = input()
         b.append(c)
         if c.endswith("END")==True:
            break
   return b
def findLine(prog, target):
   a =[]
   for i in range(len(prog)):
     a = (prog[i].split())
     if a[0] == target:
        return i
def execute(prog):
  location = 0
  visited = [False]*len(prog)
  while True:
    if location==len(prog)-1: return "success"
    elif visited[location] == True: return "infinite loop"
    visited[location] = True
    T = (prog[location].split())
    location = findLine(prog, T[len(T)-1])
print(execute(getBASIC()))
