num=int(input("enter the no.: "))
sum=0
for i in range(1,num):
   if num%i==0:
      sum=sum+i
print(sum)
if sum==sum:
   print("perfect")
else:
   print("not")   