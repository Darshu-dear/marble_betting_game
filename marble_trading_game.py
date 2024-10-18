import random
def marble_trading_game():
    money=1000
    bag=["red", "red", "red", "black", "green", "green", "green", "green", "green", "white"]
    while money>=500:
        bet=int(input(f"Enter how much you want to bet for this round, you have {money} dollars left: "))
        draw=random.choice(bag)
        if draw=="green":
            money+=bet
            print("You won!")
            print(f"You now have {money} dollars left.")
        elif draw=="white":
            money+=bet*5
            print("You won 5X Jackpot!")
            print(f"You now have {money} dollars left.")
        elif draw=="black":
            money-=bet*5
            print("You got the lose 5X curse!")
            print(f"You now have {money} dollars left.")
        else:
            money-=bet
            print("You lost! better luck next time!")
            print(f"You now have {money} dollars left.")
    print("You have lost more than 500 dollars, Game ends.")
    print("Thanks for playing")
marble_trading_game()