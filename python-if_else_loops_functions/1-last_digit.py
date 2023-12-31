#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

sign = 1 if number >= 0 else -1

last_digit = abs(number) % 10  # Abs handles neg numbers

message = f"Last digit of {number} is {sign * last_digit} and is"

if last_digit > 5:
    message += " greater than 5"
elif last_digit == 0:
    message += " 0"
else:
    message += f" less than 6 and not 0"
print(message)
