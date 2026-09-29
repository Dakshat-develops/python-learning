#Tuple: ordered, immutable, and allows duplicate elements
mytuple="max",5,"boston"#optional parentheses
print(mytuple)
# tuple for 1 element
mytuple1=("max",)#comma is mandatory otherwise it will be considered a string
print(type(mytuple1))
#can creat tuple from the tuple function
mytuple2=tuple(["max",28,"boston"])
print(mytuple2)
# referring to elements with the use of index
item=mytuple[1]
print(item)
#cannot change the elements of the tuple as it is immutable
# iterate over tuple
for i in mytuple:
    print(i)
#to check if an element is present in the tuple
if "max" in mytuple:
    print("yes")
else:
    print("no")
#find the number of elements in a tuple
print(len(mytuple2))
#count the number of a specificelement in a tuple
print(mytuple.count("max"))
#find index of a specific element in the tuple
print(mytuple.index("boston"))
#can covert tuple to list and vice versa using the tuple and list functions
mylist=list(mytuple)
list1=[1,2,3,4,5,6]  
tuple1=tuple(list1)
print(mylist)
print(tuple1)
#access subparts of your tuple using slicing
a=(1,2,3,4,5,6,7,8,9,10)
b=a[2:5]
print(b)
#optional step argument
c=a[::2]
print(c)
#can also reverse the tuple using slicing
d=a[::-1]
print(d)
#unpacking a tuple(assigning the elements of a tuple to variables)
name,age,city=mytuple#the number of variable assigned to unpack should be equal to the numnber of elements in the list
print(name)
print(age)
print(city)
#unpacking multiple elements
x=(0,1,2,3,4,5)
i1,*i2,i3,i4=x
print(i1)
print(i3)
print(i2)
#working with tuples can be more efficient than working with list as
#tuples are immutable and python cannot change anything in the tuple internally
import sys
mylist=[1,2,3,4,5,6]
mytuple=(1,2,3,4,5,6)
print(sys.getsizeof(mylist),"bytes")
print(sys.getsizeof(mytuple),"bytes")
#tuples are faster than lists
import timeit
print(timeit.timeit(stmt="[1,2,3,4,5,6]", number=1000000))
print(timeit.timeit(stmt="(1,2,3,4,5,6)", number=1000000))