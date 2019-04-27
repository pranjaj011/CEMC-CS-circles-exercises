time = str(input())
D = int(input())
if D >0:
   H = int(time[0:2])
   M = int(time[3:5])
   FinalM = (M+D)%60
   FinalH = int(((H+(M/60)+(D/60))//1)%24)
   if FinalH<10:
      FinalH = "0"+str(FinalH)
   if FinalM < 10:
      FinalM = "0"+str(FinalM)
print(str(FinalH)+":"+str(FinalM))
