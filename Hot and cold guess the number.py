#Guess the number game
import random
print('Hello! What is your name?')
name=input()

guessestaken=0

number= random.randint(1,20)
print("Well "+name+", I am thinking of number between 1 and 20.")

for guessestaken in range(6):
    print("Take a guess")
    guess=int(input())
    guessestaken+=1
    
    if guess==number:
        break
    elif guess <=number+1 and guess>=number-1:
        print("your guess is Very hot")
    elif guess > number-5 and guess<= number+5:
        print("your guess is warm")
    else:
        print("your guess is cold")
    

if guess==number:
    print("Good job"+name+", your guessed my number in", guessestaken, "guesses!")

if guess!=number:
    number=str(number)
    print("Unfortunate, the number I was thinking of was "+number)