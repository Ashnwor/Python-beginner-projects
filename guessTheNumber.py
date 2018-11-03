import random
randomerino = random.randint(1,100)
print("Guess the number game")
end = 0
tries = 0
while end == 0:
    inpt = int(input("your guess?..: "))
    tries = tries+1
    if inpt > randomerino:
        print("Your guess is high!")
    if inpt < randomerino:
        print("Your guess is low!")
    if inpt == randomerino:
        print("YOU WON! You found the number in" , tries , "tries." )
        quit()