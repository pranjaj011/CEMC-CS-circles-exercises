myList = []
counter = 0
b = 0
while True:
   a = input() #takes input 
   a = (a.lower())
   if a == "###": # stops the loop when met with ###
      break
   myList+=a.split() # all the words are in this list
if len(myList) == 1: # check if there is only one word
   print(myList[0])
for x in myList: # now check if there is more than one time that the same word appears
   a = myList.count(x)
   if a >1:
      b = x
      counter+=1
if counter > 1:
   print(b)      
