# @Author: ashnwor
# @Date:   28-Oct-2018
# @Email:  ashnwor@gmail.com
# @Last modified by:   ashnwor
# @Last modified time: 03-Nov-2018
import random
# Hangman game combined with guess the number game
print("Hangman X Guess the number")
print("Guess the random number that between 1-100 in 5 tries.")
print("If you can't hangman will lose a part.")
print("If you lose 5 games he will die.")
tries = 0
game = 0
lostLimb = 0
number = random.randint(1, 100)


def reRandom():
    global number
    number = random.randint(1, 100)


while True:
    guess = int(input("Enter your guess: "))
    tries = tries+1
    if guess < number:
        print("Your number is low!", "tries: " + str(tries))
    if guess > number:
        print("Your number is high!", "tries: " + str(tries))
    if guess == number:
        game = game+1
        print("Your number is equal!" "tries: " + str(tries), "Game:", game)
        reRandom()
        tries = 0
    if tries == 5:
        game = game+1
        print("You tried 5 times! He lost a limb. Game:", game)
        reRandom()
        tries = 0
        lostLimb = lostLimb+1
    if lostLimb == 5:
        print("He died and you have lost!")
        break
    if game == 5 and lostLimb != 5:
        print("You have won! He is not dead!")
        break
quit()
