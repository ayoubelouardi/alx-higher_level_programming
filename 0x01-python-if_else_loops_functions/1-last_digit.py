#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last = number % 10
else:
    last = abs(number) % 10
if last == 0:
    print("Last digit of", number, "is", last, "and is 0")
elif last < 6:
    print("Last digit of", number, "is", last, "and is less than 6 and not 0")
else:
    print("Last digit of", number, "is", last, "and is greater than 5")