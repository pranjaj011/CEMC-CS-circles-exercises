def isPalindrome(S):
   a = len(S)
   for i in range(a//2):
      if S[i] != S[-1-i]:
         return(False)
         print(a//2)
   return(True)
