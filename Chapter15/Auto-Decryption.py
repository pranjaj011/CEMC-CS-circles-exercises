letterGoodness=[0.0817, 0.0149, 0.0278, 0.0425, 0.127,    #predefined in the program
                0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 
                0.0077, 0.0402, 0.0241, 0.0675, 0.0751, 
                0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 
                0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 
                0.0007]
message = input()
code = list(message)
value = 0
total = 0
for step in range(26): # step 26 back each time increasing
   value = 0
   for x in code: # looping thru the list
      if x == " ": # if space skip
         continue
      x = chr(ord(x)-step) # using the step
      x = letterGoodness[(ord(x)-65)] # relating it to the pre defined value
      value += x # storing it
   if total<value: # checking which step had the highest value
      total = value 
      S = step # storing what value is needed to get the highest "good"
result = ''
for x in code:
    if x == ' ': # add the space when needed by checking from the input
        result += x
    elif ord(x) - S not in range(65, 91): # using the step value to find the text, if it goes before 64 return to 90
        result += chr(ord(x) - S + 26)
    else:
        result += chr(ord(x) - S)
print(result)
