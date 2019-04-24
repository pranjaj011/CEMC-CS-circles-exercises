timbitsLeft = int(input()) # step 1: get the input
totalCost = 0              # step 2: initialize the total cost

if timbitsLeft >= 40:
  bigBoxes = int(timbitsLeft / 40)
  totalCost = totalCost + bigBoxes * 6.19    
  timbitsLeft = timbitsLeft - 40 * bigBoxes 

if timbitsLeft >= 20:                
    totalCost = totalCost + 3.39
    timbitsLeft = timbitsLeft - 20
if timbitsLeft >= 10:                
    totalCost = totalCost + 1.99
    timbitsLeft = timbitsLeft - 10

totalCost = totalCost + timbitsLeft * 0.20 
print(totalCost)                         
