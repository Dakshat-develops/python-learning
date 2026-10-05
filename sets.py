#Sets unordered, mutable, and NO duplicates
myset={1,2,3,1,1,2}
print(myset)
#can use set function to create a set
myset1= set([1,2,3,4,5,6])#must use an iterable in the parentheses of the set function
print(myset1)
# we can use a string in as an argument to the set function
myset2= set("Hello")#unordered and no duplicates
print(myset2)
#if we want an empty set, we must use the set function. Using {} will create an empty dictionary
#Set is mutable, we can add elements using the .add method
myset1.add(7)
myset1.add(8)
myset1.add(9)
print(myset1)
#can remove elements using the .remove method
myset1.remove(9)
myset1.remove(8)
print(myset1)
#alternate method
myset1.discard(7)#removes an element if it is a member of the set and does nothing if it isnt
print(myset1)
#clear method to empty the set
myset1.clear()
print(myset1)
#pop method, removes an arbitrary value of the set and returns it
print(myset2.pop()) 
print(myset2)
#iterate over set with a for-in loop
for i in myset:
    print(i)
#to check if element is in a set
if 4 in myset:
    print("yes")
else:
    print("no")
#UNION AND INTERSECTION
odds= {1,3,5,7,9}
evens= {0,2,4,6,8}
primes= {2,3,5,7}
#union method
u= odds.union(evens)
print(u)
#intersection method
i= odds.intersection(evens)
print(i)
#Difference between two sets
set1= {1,2,3,4,5}
set2={1,2,6,7,8}
diff= set1.difference(set2)
print(diff)
#symmetric difference method
sym_diff= set1.symmetric_difference(set2)#takes the values in set1 and set2 but not the ones common to both
print(sym_diff)
#the above methods dont modify the original sets, but we can use the update methods to modify the original sets
set1.update(set2)#basically a modification version of the union method
print(set1)
#intersection_update method
setA= {1,2,3,4,5}
setB= {1,2,6,7,8}
setA.intersection_update(setB)#modifies setA to only contain the elements that are common to both sets
print(setA)
#difference_update method
setC= {1,2,3,4,5}
setD= {1,2,6,7,8}
setC.difference_update(setD)#modifies setC to only contain the elements that are not in setD
print(setC)
#symmetric_difference_update method
setE= {1,2,3,4,5}
setF= {1,2,6,7,8}
setE.symmetric_difference_update(setF)#modifies setE to only contain the elements that are in setE or setF but not both
print(setE)
#to check if a set is a subset and superset using the issubset and issuperset methods
setG= {1,2,3}
setH= {1,2,3,4,5}
print(setG.issubset(setH))  # True
print(setH.issuperset(setG))  # True
#disjoint function checks if two sets have no elements in common
print(setG.isdisjoint(setH))  # False
#The copy methodology is the same as the other collection items
#a frozenset is an immutable version of the set
a= frozenset([1,2,3,4,5])
a.add(2)#will raise an exception
a.remove(3)#will raise an exception
print(a)
