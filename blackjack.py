import random


def add(n1, n2):
    return n1 + n2


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7,
         8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def playgame():
    dealercards.append(cards.pop())
    dealertotal = sum(dealercards)
    print(f"One of the dealers cards is {dealertotal}")
    dealercards.append(cards.pop())
    dealertotal = sum(dealercards)
    while dealertotal < 17:
        dealercards.append(cards.pop())
        dealertotal = sum(dealercards)
    usercards.append(cards.pop())
    usertotal = sum(usercards)
    hitorstand = "hit"
    while hitorstand == "hit":
        usercards.append(cards.pop())
        usertotal = sum(usercards)
        for item in usercards:
            if item == 11 and usertotal > 21:
                usercards.append(1)
                usercards.remove(11)
                usertotal = sum(usercards)
        if usertotal < 22:
            print(f"Your score is currently {usertotal} with the cards: {usercards}")
            hitorstand = input("hit or stand? ")
        if usertotal > 21:
            hitorstand = "stand"
    if usertotal > 21 and dealertotal > 21:
        print(f"both are over 21; both lose with {usertotal} vs {dealertotal}")
    elif usertotal < 22 and dealertotal > 21:
        print(f"You win! Dealer went over and loses")
    elif usertotal > dealertotal and usertotal < 22:
        print(f"User wins with {usertotal}, dealer loses with {dealertotal}")
    elif usertotal == dealertotal:
        print(f"Draw! {usertotal} and {dealertotal}")
    elif usertotal < dealertotal and usertotal < 22:
        print(f"User loses with {usertotal}, dealer wins with {dealertotal}")
    elif usertotal > dealertotal and usertotal >= 22:
        print(f"User loses with {usertotal}, dealer wins with {dealertotal}")


while input("press yes to play a game of blackjack "):
    dealercards = []
    usercards = []
    random.shuffle(cards)
    playgame()
