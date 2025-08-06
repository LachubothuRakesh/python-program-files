num=int(input("enter the year: "))
if num%4==0:
    print("this is leap year")
elif num%100==0:
    print("this not leap year")
elif num%400==0:
    print("this is leap year")
else:
    print("this is not leap year")    

