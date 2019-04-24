def lowerChar(char):
   if ord(char) < 97 and ord(char)>=65:
      return(chr(ord(char)+32))
   else:
      return(char)
