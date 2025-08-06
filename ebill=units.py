ebill=int(input("enter the units: "))
if ebill==100:
    print("no charge")
elif ebill>100:
    print("5rupees per unit")
elif ebill>=200:
    print("10rupees per unit")
else:
    print("exit from app")            