li=[100,200,300,400,500,600]  #list of all elements
for i in li:
    print(i)

li1=[100,200,300,400,500]        #append
print("before adding number",li1)
li1.append(600)
print("after adding number",li1)
print(li1)

li2=[250,350,450,550,650]    #insert
print("before inserting",li2)
li2.insert(0,150)
print("after inserting",li2)
print(li2)

li3=[220,440,320,520]     #remove
print("before removing",li3)
li3.remove(520)
print("after removing",li3)
print(li3)

li4=[29,40,5,33,22,77,88,90,80]  #sublist
sublist=li4[2:8]
print("original list",li4)
print("sublist",sublist)

li5=[29,40,5,33,22,66]    #reverse
print(li5[1:4])
li5.reverse()
print("reverse list",li5)

li6=[29,40,5,33,22,77,88,90,80]   #sorting 
print("before sorting list",li6)
li6.sort(reverse= True)
print("after sorting list",li6)
print(li6)

li7=[29,40,5,33,22,77,88,90,80]  #length
length=len(li7)
print("the length of list",length)
  
li7=[29,40,5,33,22,77,88,90,80]  #in(membership) 
print(88 in li7)

li7=[29,40,5,33,22,77,88,90,80]  #pop
print("before pop element",li7)
print("after pop element",li7.pop())
print(li7)

li7=[29,40,5,33,22,77,88,90,80]   #delete
del li7[5]
print(li7)

li6=[29,40,5,33,22,77,88,90,80,88,40]  #count
count=li6.count(40)
print(count)

li6=[29,40,5,33,22,77,88,90,80,88,40]  #index
print(li6.index(88))


number=input("enter the numbers seperated by space: ").split()  # create list form user input
list=[int(i) for i in number]                                   # numbers
print(" ".join(str(i) for i in number))

items=input("enter the items seperated by commas: ").split(',') # items(in characters format)
print("list:",items)

nums=[10,20,30,10,40,50] #remove duplicate values
new=[]
for i in nums:
    if i not in new:
        new.append(i)
print(new)

li9=[1,2,3,4,5] #merge list
li8=[6,7,8,9,10]
print(li9+li8)

li6=[29,40,5,33,22,77,88,90,80,88,40] # large and small number in list
print(max(li6))
print(min(li6))

li6=[29,40,5,33,22,77,88,90,80,88,40] #finding of average of list
total=sum(li6)
average=total/len(li6)
print("sum:",total)
print("average:",average)

li9=li8.copy() #cpoy
print(li9)

li6=[29,40,5,33,22,77,88,90,80,88,40]  #swap
li6[0],li6[-1]=li6[-1],li6[0]
print("after swap:",li6)

li6=[29,40,5,33,22,77,88,90,80,88,40] #print even and odd from list
even=[i for i in li6 if i%2==0]
odd=[i for i in li6 if i%2!=0]
print("even numbers:",even)
print("odd numbers:",odd)

