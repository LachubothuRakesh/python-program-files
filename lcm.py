num1=int(input("enter the first number: "))
num2=int(input("enter the first number: "))
if num1>num2:
    greater=num1
else:
    greater=num2
while True:
    if greater%num1==0 and greater%num2==0:
        print("lcm is:",greater)
        break
    greater=greater+1        



