import random

highest = 1000      #assigning a variable allows you to make a single change to the values you want at the highest side of your game
answer = random.randint(1, highest)

guess = 1024        #you can use anything that's not b/w 1 and 1000

print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == answer:
        print("Well done, you guessed it ")
        break
    elif guess == 0:
        print("GAME OVER")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
