import random

coin = ["heads", "tails"]
toss = random.choice(coin)  # This simulates the coin being tossed

selection = input("Heads or Tails: ")

if selection == toss:
    print("You win! The coin landed on " + toss)
    decision = input('What would you like to do first?')
    if decision == 'bat':
        print('Congratulations and put up a good score!!!')
    elif decision == 'bowl':
        print('Well best of luck on bowling them out!!!')


else:
    print("You lose! The coin landed on " + toss)
