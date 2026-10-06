#Strings, ordered, immutable, text representation
#Creation of a string
mystring= "Hello world"# we can use single, double or triple(for mutlitline strings) quotes to create a string
print(mystring)
mystring1="""This is a multiline \
string"""
print(mystring1)
#accessing characters in a string
char= mystring[0]#we cannot change the value of a character in a string since strings are immutable
print(char)
#accessing a substring using slicing
substring= mystring[1:5:1]
print(substring)
#we can add string using the addition operator
greeting= "hello"
name= "tom"
sentence=greeting+" "+name
print(sentence)
#iterating through a string
for i in greeting:
    print(i)
#to check if a character or substring present in the string
if "e" in greeting:
    print("yes")
else:
    print("no")
#removing whitespace from the beginning and end of a string using the strip method
mystring2= "  Hello World  "
print(mystring2)
mystring2=mystring2.strip()#we must assign it back to the string so we can see the changes since strings are immutable
print(mystring2)
#to print uppercase and lowercase of a string
print(mystring2.upper())
print(mystring2.lower())
#to check if the string starts or ends with a particular character or substring
print(mystring2.startswith("H"))
print(mystring2.endswith("d"))
#find the index of a character and count the number of times a charcter is present in a string
print(mystring2.find("o"))# if the character is not present, it will return -1
print(mystring2.count("l"))
#replace a character or a substring in a string
print(mystring2.replace("world","universe"))#if a typo is present when reffering to the old string, then it will make no changes
# convert a string into a list
mylist= mystring2.split(" ")# default de-limiter is a space, we can use other ones when needed
print(mylist)
#join a list into a string
new_string= ' '.join(mylist)#it will join the elements of the string with the character specified before the join method
print(new_string)
#expanding on the above method
# bad
"""from timeit import default_timer as timer 
mylist1= ['a'] * 10000
nstring=''
start=timer()
for i in mylist1:
    nstring+=i
stop= timer()
print(stop-start)
#good
nstring1=''
start1= timer()
nstring1=''.join(mylist1)#much faster than the iterating method
stop1= timer()
print(stop1-start1)"""
#formatting strings
#old methods-% and .format()
var="Tom"
mystring3="Hello %s" % var #%s is a placeholder for strings, for int=d, for float=f
print(mystring3)
var1=3.12345
mystring4="the variable is %.4f" %var1
print(mystring4)
#.format()
mystring5="Hello {}".format(var)
print(mystring5)
mystring5="the variable is {:.4f}".format(var1)
print(mystring5)
#new method-fstrings
new_string=f"Hello {var}"
print(new_string)