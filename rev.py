num=int(input("enter the number: "))
rev=0
temp=num
while num>0:
    lastdigit=num%10
    rev=rev*10+lastdigit
    num=num//10
print(rev)    
if rev==temp:
    print("palnidrom")
else:
    print("not palindrom")    

   