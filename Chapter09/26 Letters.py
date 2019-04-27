letter = input()
a = int(ord(letter))
if a>=ord('A') and a<=ord('Z'):
   a = (a-64)
   print(a)
else:
   print("invalid")
