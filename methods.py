set1={10,20,30,40,50}
set1.add(60)
print(set1)

set1={10,20,30,40,50}
set1.pop()
print(set1)

set1={10,20,30,40,50}
set1.remove(30)
print(set1)

set1={10,20,30,40,50}
set1.discard(20)
print(set1)

set1={10,20,30,40,50}
set2={10,20,60,70,80}
set1=set2.copy()
print(set1)

set1={10,20,30,40,50}
set2={10,20,60,70,80}
print(set1.isdisjoint(set2))

set1={10,20}
set2={10,20}
print(set1.issubset(set2))

set1={10,20,30}
set2={10,20,30}
print(set1.issuperset(set2))

set1={10,20,30,40,50}
set2={10,20,60,70,80}
set1.intersection_update(set2)
print(set1)

set1={10,20,30,40,50}
set2={10,20,60,70,80}
set1.symmetric_difference_update(set2)
print(set1)

set1={10,20,30,40,50}
set1.clear()
print(set1)

s={10,20}
s.update([30,40])
print(s)