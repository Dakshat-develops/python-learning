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

    if guess < number:
        print("your guess is too low")
    elif guess > number:
        print("your guess is too high")
    elif guess==number:
        break

if guess==number:
    print("Good job"+name+", your guessed my number in", guessestaken, "guesses!")

if guess!=number:
    number=str(number)
    print("Unfortunate, the number I was thinking of was "+number)