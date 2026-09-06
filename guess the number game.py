import random
secret=random.randint(1,10)
print("Guess the number")
user=int(input("Please enter your number"))
if user==secret:
    print("You guessed the number correctly")
else:
    print("You guessed the number wrong lol try again")

