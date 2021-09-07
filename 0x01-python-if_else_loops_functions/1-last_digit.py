#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    copy = (((number * (-1)) % 10) * -1)
else:
    copy = number % 10

if copy > 5:
    print("Last digit of {} is {} and is greater than 5"
          .format(number, copy))
elif (copy < 6) and (copy != 0):
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, copy))
elif copy == 0:
    print("Last digit of {} is {} and is 0".format(number, copy))
