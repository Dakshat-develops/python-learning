#creating a contacts book without any tutorials, must use: list, dicts, namedtuple, *args or **kwargs, and f-strings.
from collections import namedtuple
Contacts={}

def Add_Contact(**kwargs): 
    for Key in kwargs:
        if Key=='Name':
            name=kwargs[Key]
        elif Key=='Num':
            num=kwargs[Key]
        elif Key=='Address':
            add=kwargs[Key]
    Cname=namedtuple(name,'Number,Address')
    namet=Cname(num,add)
    Contacts[name]=namet


def Search_contact(SE):
    for Key in Contacts:
        if Key== SE:
            print("Details of",Key ,":")
            print("Phone number:",Contacts[Key][0])
            print("Address:",Contacts[Key][1])

def Display_Contacts():
    for Key in Contacts:
        cname=Key
        phnum=Contacts[Key][0]
        address=Contacts[Key][1]
        print(f"Name:{cname}" ,f"Phone Number:{phnum}",f"Address:{address}")








i=0
while i >=0:
    print("Menu")
    print("1.Add  new contact")
    print("2.Search contact")
    print("3.view all contacts")
    print("4.Exit")
    ch=int(input("Enter your choice(1-4):"))

    if ch==1:
        name=input("Enter Name of contact:")
        num=int(input("Enter phone number of contact:"))
        address=input("Enter Address of the contact:")
        Add_Contact(Name=name,Num=num,Address=address)
    elif ch==2:
        print("Searching for contact")
        SE=input("Enter name to be searched:")
        Search_contact(SE)
    elif ch==3:
        Display_Contacts()
    elif ch==4:
        print("Exited")
        i=-999
    else:
        print("Invalid Choice")
        