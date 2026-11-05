import random
import time

def Intro():
    print('''You are in a land full of dragons.
    In front of you there are three caves.
    in one cave there is a friendly dragon who will give you all its TREASURE.
    The second cave has a dragon that will EAT you on sight
    the third cave has a funny dragon who will tell you a JOKE!''')

def choosecave():
    cave = ''
    while cave != '1' and cave != '2' and cave != '3':
        print('Which cave will you go into? (1, 2, or 3)')
        cave = input()
    return cave

def checkcave(chosencave):
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! It opens its jaws and...")
    print()
    time.sleep(2)

    friendlycave = random.randint(1, 3)
    random2=[1,2,3]
    random2.remove(friendlycave)
    jokingcave= random.randint(random2[0], random2[1])
    

    if chosencave == str(friendlycave):
        print("Gives you his treasure!")
    elif chosencave == str(jokingcave):
        print("It tells you a joke:\n I ate a clock yesterday, it was very time consuming!\nHA HA HA HA...")
    else:
        print("Gobbles you down in one bite!")

Playagain = 'yes'
while Playagain == 'yes' or Playagain == 'y':
    Intro()
    caveNumber = choosecave()
    checkcave(caveNumber)
    print('Do you want to play again? (yes or no)')
    Playagain=input()