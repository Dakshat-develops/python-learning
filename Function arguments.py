#function arguments
def print_name(name):#here name is the parameter as itis used while defining the function
    print(name)
print_name('Alex')#here 'Alex' is the argument that takes the place of the parameter in the function, used when we call the function

#positional vs. Keyword arguments
def foo(a,b,c):
    print(a,b,c)
foo(1,2,3)#positional arguments: assigns the numbers to a, b, and c based on the postion of the arguments
foo(b=5,a=4,c=6)#Keyword arguments: we have assigned arguments to the parameter by using the '=' operator. the postion or oreder of the numbers dont matter.
#default value
def foo1(b,c=5,a=2):#c has a default value of 5, the assigned default value must always be at the end
    print(a,b,c)
foo1(3)
#variable length arguments: unlimited number of arguments
def foo2(a,b,*args,**kwargs):#'*args' is for positional arguments and is stored as a tuple. '**kwargs' is for keyword arguments and is stored as a dictionary
    print(a,b, end=' ')
    for arg in args:
        print(arg, end=' ')
    for key in kwargs:
        print(key, kwargs[key], end=' ')
foo2(1,2,3,4,5,six=6,seven=7)
#forcing keyword arguments
def foo3(a,b,*,c,d):#all the arguments corresponding to the parameters after '*' is supposed to be a keyword argument
    print(a,b,c,d)
foo3(1,2,c=3,d=4)
#alt. method
def foo4(*args, last):#any argument given after the '*args' must be a keyword argument
    for arg in args:
        print(arg)
    print(last)
foo4(1,2,3,last=100)
#unpacking containers to the function
# to unpack a list, we must use one asterisk
def foo5(a,b,c):
    print(a,b,c)
my_list=[0,1,2]#length must be equal to number of parameters in the function
foo5(*my_list)
my_dict={'a':1, 'b':2, 'c':3}#length of dict/no. of items must be equal to no. of parameters
foo5(**my_dict)#we should use two aasterisks to unpack a dictionary
#Local vs. Global variable
def foo6():
    global number#we use this line to change the global variable in a function
    number=1
    x=number
    print('The number inside function is:', x)

number=0
foo6()
print(number)
def foo7():
    number=3#creates a local variable
    print(number)
foo7()
print(number)
#parameter passing
def poo(x):
    x=5#doesnt change the immutable data type: int, tuple, etc
var=10
poo(var)
print(var)
def doo(a_list):
    a_list.append(4)#can change a mutable collection object,we can also change the immutable data object inside a mutable data object.
    a_list[0]=67
my_list=[1,2,3]
doo(my_list)
print(my_list)
#we cannot reassign the list to a different one, it will act as a local and global variable. and a small difference a+=... will give you the correct ouput but a=a+... will not give oyu the correct output(creates a local variable)
def foo(a):
    a=a+[100,200,300]
    a=[3,4,5]
my_list=[1,2,3]
foo(my_list)
print(my_list)