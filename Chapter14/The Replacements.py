def replace(list, X, Y):
  for i in range(list.count(X)):
   list.insert(list.index(X), Y)
   list.remove(X)
