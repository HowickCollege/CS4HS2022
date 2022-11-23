# A game of guessing the number
# Your name

import random

# pick a random number
num = random.randint(1, 10)
print(num)

# repeat for three attempts 
for i in range(3):
    guess = int(input("Guess the number: "))
    if guess < num:
        print("Too low")
    elif guess > num:
        print("Too high")
    else:
        print("You are amazing!")
        break  # stop the loop

# display when all three guesses are wrong
if guess != num:
    print("Better luck next time")