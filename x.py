li=[[1,2,3],[4,5,6]]   #flattenlist
for sublist in li:
    for i in sublist:
        print(i)


list1=[1,2,3,4,5] #rotated
k=2
direction="left" 
k=k%len(list1)
if direction=="left":
    rotated=list1[k:]+list1[:k]
elif direction=="right":
    rotated=list1[-k:]+list1[:-k]
else:
    rotated=list1
print("Rotated:",rotated)

list = ["apple", "", "banana", "", "cherry"]  #Remove empty strings from a list
clean_list=[]
for item in list:
    if item!="": 
        clean_list.append(item)
print("Cleaned List:",clean_list)


list=input("Enter list elements separated by space: ").split() #chunk
n=int(input("Enter chunk size: "))
list=[i for i in list]
chunks=[]
for i in range(0,len(list),n):
    chunk=list[i:i+n]
    chunks.append(chunk)
print("Chunks:",chunks)


numbers=[10, 20, 4, 45, 99] #smallest and largest
numbers.sort()
print("Second Smallest:",numbers[1])
print("Second Largest:", numbers[-2])

number=[10,-5,3,0,-2,8,7] #positive negative and even and odd
positive=0
negative=0
even=0
odd=0
for num in number:
    if num>0:
        positive=positive+1
    elif num<0:
        negative=negative+1
    if num%2==0:
        even=even+1
    else:
        odd=odd+1
print("Positive number:",positive)
print("Negative number:",negative)
print("Even number:",even)
print("Odd number:",odd)

list1=[1, 2, 3, 4, 5]  #common
list2=[4, 5, 6, 7, 8]
common=[]
for item in list1:
    if item in list2:
        common.append(item)
print("Common elements:",common)

list1=[1,2,3,4,5] #difference
list2=[4,5,6,7]
diff1=[i for i in list1 if i not in list2]
diff2=[i for i in list2 if i not in list1]
print("list1-list2:",diff1)
print("list2-list1:",diff2)

numbers=[1,2,3,2,4,5,1,6] #duplicates
duplicates=[]
[duplicates.append(i) for i in numbers if numbers.count(i)>1 and i not in duplicates]
print("Duplicates:", duplicates)

numbers=[1,2,3,2,4,1,5,3] #removing duplicates without set
unique=[]
[unique.append(i) for i in numbers if i not in unique]
print("Unique list:",unique)

squares=[] #list of squares
for i in range(1,11):
    squares.append(i*i)
print("Squares from 1 to 10:",squares)

nums=[1,2,3,4,5,6]  #filter even numbers
even=[i for i in nums if i%2==0]
print(even)

list=["apple","banana","cherry"]  #upper case
upper=[list.upper() for list in list]
print(upper)

nums=[20,55,60,30,90]  #greater than 50
greater=[i for i in nums if i>50]
print(greater)

nums=[10,-5,20,-3,0] #replace negative numbers
new_list=[0 if i<0 else i for i in nums]
print(new_list)

list = ["apple", "fig", "banana", "kiwi"] #sort list of strings by using length
print(sorted(list,key=len))

nums=[10,20,30,40] #search for an element using linear search
x=30
print(x in nums)

nums=[10,20,30] #list is in sorted
print(nums==sorted(nums))

nums=[10, 20, 30, 40, 50] #binary search on sorted list
x=30
i=next((i for i in range(len(nums)) if nums[i]>=x),len(nums))
print(i<len(nums) and nums[i]==x)

nums=[2,3,4,5,6,7,9,11] #getting all prime numbers in list
print([n for n in nums if n > 1 and all(n % i != 0 for i in range(2, n))])

nums=[1,2,2,3,3,3] #frequency
freq={}
for n in nums: 
    freq[n]=freq.get(n,0)+1
print(freq)

nums=[1,2,3,4] #rotate list
print("Right:",[nums[-1]]+nums[:-1],"Left:",nums[1:]+[nums[0]])

nums=[1,2,3,2,1] #list is in palidrome
print(nums==nums[::-1])

nums=[1,2,2,3,3,3] #element with high frequency
print(max(set(nums),key=nums.count))

chars=['H','e','l','l','o'] #convert the list of chars into string
print(''.join(chars))

nums=[1,2,3,4] #multiply all numbers in list
prod=1
for n in nums: 
    prod*=n
print(prod)

nums=[-1,2,-3,4] #remove all negative numbers form list
print([n for n in nums if n>=0])

li=[10 20 30 40]


