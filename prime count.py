num=int(input("enter the number: "))
num>1
for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
else:
        print("prime")    

        print('------')

start=int(input("enter the number: "))
end=int(input("enter the number:" ))
count=0
for i in range(start,end+1):
     if num>1:
          for num in range(2,num):
               if num%i==0:
                    break
          else:
               print(num, "is prime")
               count=count+1   
print("total primes:",count)         