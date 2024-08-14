import random

list = [3,-3,0]

number = random.choice(list)

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
elif number == 0:
    print("Zero")