( Ai ussage fixed)( follow along in class)
import random

while True:
    coin = random.choice(["heads", "Tails"])

    while True:
        guess = input("Guess heads or tails: ")


        if guess == "heads" or guess == "tails":
            break
        else:
            print("oops! wrong type heads or tails input.")

    if guess == coin.lower():
        print("correct!")
    else:
        print("incorrect!")
