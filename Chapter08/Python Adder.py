S = input()
for position in range (0, len(S)):
   if S[position]== '+':
      str1= int(S[0:position])
      str2= int(S[position:len(S)])
      print(str1+str2)
