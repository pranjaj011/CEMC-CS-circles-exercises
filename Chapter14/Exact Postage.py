def postalValidate(S):
  S = S.replace(" ", '')
  if S.isalpha() or S.isdigit() == True:
      return(False)
  else:
      if len(S) == 6:
         if (S[0].isalpha() and S[2].isalpha() and S[4].isalpha()) == False:
            return False
         elif (S[1].isdigit() and S[3].isdigit() and S[5].isdigit()) == False:
            return False
         else:
            return S.upper()
      else:
         return False
