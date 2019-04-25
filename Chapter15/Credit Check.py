def check(S):
   credit_List = S.split()
   b = 0
   c = " "
   a = 0
   if len(S) != 19:
      return False
   for x in range(len(S)):
      if S[x].isalpha() == True: 
         return False
   if c in S[4] and c in S[9] and c in S[14]:
      S = S.replace(" ", "")
      for i in range (4):
           if credit_List[i].isdigit():
              for x in range(len(S)):
                  b=int(S[x])
                  a=a+b
      if a == 0:
         return False
      elif (a%10) == 0:
         return True
      else: return False
   else: return False
