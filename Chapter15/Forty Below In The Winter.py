conversion = input()
if conversion.endswith("F"):
   conversion = conversion.replace("F", "")
   conversion = float(conversion)
   c = (conversion-32)*(5/9)
   print(str(c)+"C")
elif conversion.endswith("C"):
   conversion = conversion.replace("C", "")
   conversion = float(conversion)
   c = (conversion*(9/5))+32
   print(str(c)+"F")
