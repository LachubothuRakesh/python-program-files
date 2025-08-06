num=int(input("enter the number: "))
sum=0
a=num
while num>0:
    lastdigit=num%10
    sum=sum+lastdigit*lastdigit*lastdigit
    num=num//10
print(sum)  
if sum==a:
    print("armstrong")
else:
    print("not")    