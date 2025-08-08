d={1:20,2:30,3:40} #basic dictionary
print(d)
print(d[3])

d={1:20,2:30,3:40} #adding new keyvalue
print(d)
d[1]=1000
d[5]=100
print(d)

d={1:20,2:30,3:40} #delete data form dictionary
del d[1]
print(d)

d={"device":"phone",1:15,"url":"present"} #methods of dictionary
print(d.get(15, "user not found"))
print("return values",d.values())
print("return key",d.keys())
print("both key and values",d.items())

d={"device":"phone",1:15,"url":"present"} #pop
print(d.pop(1))
print(d.popitem())

d1={1:20,2:30,3:40} #update
d2={4:50,5:60,6:70}
d1.update(d2)
print("after update d1 is",d1) 

d1={1:20,2:30,3:40} #setdefault
d1.setdefault(100,200)
print(d1)

res={i:i*i for i in range(1,11) if i%2!=0} #dictionary comprhension
print(res)

a=[1,2,3] #zip(dictionary version)
b=[10,20,30]
print(dict(zip(a,b)))

res=frozenset([1,2,3,4]) #forzenset
print(res)