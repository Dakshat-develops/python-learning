#List creation-use square brackets and seperate elements with a comma
mylist =["apple","banana","cherry"]
print(mylist)
#creating an empty list with the list function
mylist2 = list()
print(mylist2)
#lists can contain duplicate elements and diff data types
mylist3=[5,True, "apple","apple"]
print(mylist3)
#Accesing elements using index
item=mylist[1]
print(item)
#using negative indexing
item1=mylist[-1]#-1 refers to the last element, -2 to the second last and so on
print(item1)
#iterating a list with for loop
for i in mylist:
    print(i)
#to check if an element exist in the list
if "lemon" in mylist:
    print("yes")
else:
    print("no")
#check the number of elements in the list
print(len(mylist))
#append items to the list
mylist.append("lemon")
print(mylist)
#insert an element at a specific position
mylist.insert(1,"pear")
print(mylist)
#removing an element from the end of the list
item2=mylist.pop()
print(item2)
print(mylist)
#remove a specific element from the list
mylist.remove("cherry")
print(mylist)
#remove all element from the list
mylist3.clear()
print(mylist3)
#reversing the list
mylist.reverse()
print(mylist)
#sorting the list
mylist.sort()
print(mylist)
#alternate method for sorting a list
list1=[-5,1,5,7,-2]
newlist=sorted(list1)
print(list1)
print(newlist)
#create a list with same element multiple times
list2=[0]*5
print(list2)
#adding two lists
list3=[1,2,3]
new_list= list2 + list3
print(new_list)
#access subparts of your list using the slicing method
list4=[1,2,3,4,5,6,7,8]
a=list4[1:5]#default start is 0 and default end is the last element of the list
print(a)
#using step in slicing
b=list4[1::2]#default step is 1
print(b)
#copying of list
list_org=["banana","apple","cherry"]
list_cpy=list_org#both the lists refer to the same list in the memory. making a change to one will also affect the otther
list_cpy.append("lemon")
print(list_cpy)
print(list_org)#this above method creates an alias of the original list, so any changes made to the copy will also affect the original list
#other methods
list_org1=["banana","apple","cherry"]
list_cpy1=list_org1.copy()#method 1
list_cpy2=list(list_org1)#method 2
list_cpy3=list_org1[:]#method 3
list_cpy1.append("lemon")
list_cpy2.append("grapes")
list_cpy3.append("kiwi")
print(list_org1)
print(list_cpy1)
print(list_cpy2)
print(list_cpy3)
#advanced technique:list comprehension
x=[1,2,3,4,5,6]
y=[i**3 for i in x]#["expression" for "item" in "list"]
print(x)
print(y)