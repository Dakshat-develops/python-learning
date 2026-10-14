#Copying
#we can use the assigment operator to make a copy
org= 6#this is an immutable data type, so there isnt a problem with this method. 
cpy = org
cpy = 8
print(cpy)
print(org)
org1=[0, 1, 2, 3]
cpy1=org1#because this is a mutable data type, it changes the orignal one also
cpy1[0]=-10
print(cpy1)
print(org1)
#we must use the copy function to make a proper copy
#shallow copy: One level deep and then only references of the nested child objects
#deep copy:A full independant copy
#Shallow copy:
import copy
org= [0,1,2,3,4]
#cpy= copy.copy(org)
#cpy=org.copy()
cpy=list(org)
cpy[0]=-10
print(cpy)
print(org)
#error
org=[[0,1,2,3,4], [5,6,7,8]]
cpy=copy.copy(org)#creates a shallow copy that only goes one level deep, cannot be used properly when there is a nested object
cpy[0][1]=-10
print(cpy)
print(org)
# we must use a deep copy
org=[[0,1,2,3,4], [5,6,7,8]]
cpy=copy.deepcopy(org)
cpy[0][1]=-10
print(cpy)
print(org)
#we can use a deep copy for custom objects also
class Person:
    def __init__(self, Name, Age):
        self.Name=Name
        self.Age=Age

class Company:
    def __init__(self, boss, employee):
        self.boss=boss
        self.employee=employee

p1=Person('Alex',27)
p2=Person('john',18)

company=Company(p1,p2)
company_cpy=copy.deepcopy(company)
company_cpy.boss.Age=28
print(company_cpy.boss.Age)
print(company.boss.Age)
