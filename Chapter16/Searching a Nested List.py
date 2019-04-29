def nestedListContains(NL, target):
   if isinstance(NL, int):
      if NL == target:
         return True
      else: return NL
      
   for x in NL:
      if nestedListContains(x, target) == True:
         return True
   return False
