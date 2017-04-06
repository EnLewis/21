from TwentyOne import *

# Code for testing classes
print("Hello and welcome to 21.py! ")
print("please enter your total purse")
wallet = int(input())

player1 = Player("Daniel N.",wallet)


deck = Deck()
print(deck.displayDeck())
deck.shuffle()
card = deck.draw()
print("{} is worth {} points".format(card.display(),card.value() ) )

for i in range(2):
    new_card = deck.draw()
    player1._hand.add(new_card)

while(True):
    new_card = deck.draw()
    print(new_card.display())
    print(new_card.isAce())
    if new_card.isAce():
        player1._hand.add(new_card)
        break
    else:
        continue

print(player1._hand.displayHand() )

print(player1._hand.handValue() )
