def execute(prog):
  location = 0
  T =[]
  visited = [False]*len(prog)
  while True:
    if location==len(prog)-1: return "success"
    elif visited[location] == True: return "infinite loop"
    visited[location] = True
    T = (prog[location].split())
    location = findLine(prog, T[len(T)-1])
