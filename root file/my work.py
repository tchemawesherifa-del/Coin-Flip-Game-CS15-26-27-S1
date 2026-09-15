import random
 
strikes = 0

while True:
    coin = random.choice(["heads", "tails"])

    while True:
        guess = input("Heads or Tails? ").lower()
        if guess == "heads" or guess == "tails":
            break
        else:
            print("That's not an option silly bean. Try again.")

    if guess == coin:
        print("Correct!")
        strikes = 0
    else:
        print("Wrong silly! It was " + coin)
        strikes = strikes + 1

    print("Current strikes: " + str(strikes) + "/3")
    print("--------------------")

    if strikes == 3:
        print("3 strikes in a row! Game over.")
        break
