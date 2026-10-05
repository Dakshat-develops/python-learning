#dicts, key-value pairs, unordered, mutable
mydict= {"name":"Ram", "age":19, "city":"Kathmandu"}
print(mydict)
#creating a dictionary using dict function
mydict2= dict(name="Shyam", age=20, city="Pokhara")
print(mydict2)
#accessing values
value = mydict["name"]
print(value)
#adding a new key-value pair
mydict["Gender"]="Male"
print(mydict)
#if the key-value pair already exists, the item gets overwritten
mydict["age"]=18
print(mydict)
#deleting items
#METHOD 1
del mydict["Gender"]
print(mydict)
#METHOD 2
mydict.pop("city")
print(mydict)
#METHOD 3
mydict.popitem()#post python 3.7 it pops the last item, before thet it used to pop a random item
print(mydict)
#to check if a key is present in the dictionary
#METHOD 1
if "name" in mydict2:
    print( mydict2["name"])
#METHOD 2
try:
    print(mydict2["lastname"])
except:
    print("ERROR")
#LLooping through a dictionary
#KEYS
#method 1
for key in mydict2:
    print(key)  
#method 2
for key in mydict2.keys():
    print(key)  
#VALUES
for value in mydict2.values():
    print(value)
#KEY-VALUE PAIRS
for key, value in mydict2.items():
    print(key, value)  
#while copying a dictionary, be carefull. You can change the value of the original dictionary if you change the value of the copied dictionary.
#.copy() method
mydict_cpy =  mydict2.copy()
mydict_cpy["name"]="Hari"
print(mydict2)
print(mydict_cpy)
#dict built-in function method
mydict_cpy1= dict(mydict2)
mydict_cpy1["email"]="hari@example.com"
print(mydict_cpy1)
print(mydict2)
#merging two dictionaries
mydict1=dict(name="Hari", age=21, city="Lalitpur")
mydict1.update(mydict_cpy1)#overwrites values of the keys present in the first dictionary with the values of the second dictionary
print(mydict1)
#key types in python dictionary
#keys can be of any immutable type, like strings, numbers, tuples. Lists and sets cannot be used as keys because they are mutable.
