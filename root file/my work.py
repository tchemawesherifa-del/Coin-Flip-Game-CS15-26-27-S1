import random


strikes = 0
streak = 0
while True:
    coin = random.choice(["heads", "tails"])
    while True:
        guess = input("Heads or Tails? ").lower()
        if guess == "heads" or guess == "tails":
            break
        else:
            print("That's not an option, Try again")

    if guess == coin:
        print("right/correct")
        streak = streak + 1
        print("streak:", streak)
    else:
        print("Wrong")
        strikes = strikes + 1
        print("strikes:", strikes)
    if strikes == 3:
        print("3 Strikes! You're out Baldies basics!")
        break
    if streak == 3:
        print("You win!")
        print("Game ended, Bald silly bean!")
        break
