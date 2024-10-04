import random

while True:
    Number = (random.randrange(1, 7))
    print(Number)
    reply = (input("Do you want to roll the dice again? Reply with y or n ").lower())
    if reply == "n":
        print("Thank you for trying!")
        break

