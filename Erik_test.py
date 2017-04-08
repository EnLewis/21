from TwentyOne import *

# Code for testing classes
print("            Hello and welcome to 21.py! ")
print("How many players are with us tonight? (max. 4)")
num_players = int(input())
players = list()

if num_players <= 4:
    for i in range(num_players):
        print("player{}'s name?'".format(i))
        name = str(input())
        print("please give your entire bank balance {}".format(name) )
        wallet = int(input())

        player = Player(name, wallet)
        players.append(player)

deck = Deck()
deck.shuffle()
first = 1

print("Thank you for joining us, please place a bet before you are dealt in.")
for player in players:
    print("{}:".format(player._name))
    player_bet = int(input())

    hand = Hand()
    #NOTE: TESTcode for forcing an ace
    while(True):
        new_card = deck.draw()
        # print(new_card.display())
        # print(new_card.isAce())
        if new_card.isAce():
            hand.add(new_card)
            break
        else:
            continue

    hand.add(deck.draw())
    player.addHand(hand)

    # forcing a splittable hand for testing
    # if first:
    #     while(True):
    #         if deck.cardsLeft()>= 2:
    #             player.printHandsHeld(0,True)
    #             if hand.canSplit(player):
    #                 first = 0
    #                 break
    #             else:
    #                 player.reset()
    #                 for i in range(2):
    #                     new_card = deck.draw()
    #                     hand.add(new_card)
    #                 player.addHand(hand)
    #         else:
    #             print("Drew whole deck,try again")
    #             player.reset()
    #             deck.reset()
    #             deck.shuffle()
    #             continue




    player.getBet(hand,player_bet)
    print("{} placed a bet of {}$ on a hand of ".format(player._name, hand._bet))
    player.printHandsHeld(0)


def turn(player):
    for hand in player._hands:
        print("Excellent, what would you like to do {} with hand...".format(player._name) )
        print("{} (bet: {}$)".format(hand.displayHand(),hand._bet))
        values = hand.handValue()
        print(values)
        # Should be contained within a method, is shit
        for value in values:
            if value > 21:
                values.remove(value)
        display = max(values)
        print("The highest hand value is {}".format(display) )
        print("Hit, Stay, Double Down, or Split? (1/2/3/4)")
        player_choice = int(input() )
        while( (player_choice != 2) == (hand._isBust == False) ):

            player.play(player_choice,deck,hand )
            print("You chose {} for a hand of...".format(player_choice))
            print("{} (bet: {}$)".format(hand.displayHand(),hand._bet))
            # Should be contained within a method, is shit

            values = hand.handValue()
            for value in values:
                if value > 21:
                    values.remove(value)
            display = max(values)
            print(values)

            print("This hands value is {}".format(display) )
            if hand._isBust:
                print("You went Bust! You lost {}$".format(hand._bet))
                break
            if player_choice == 3:
                break

            print("Hit, Stay, Double Down, or Split (1/2/3/4)")
            player_choice = int(input() )


    print("{}'s wallet is {}".format(player._name,player._wallet))


for player in players:
    print("")
    print("Its {}'s turn!".format(player._name))
    turn(player)


#NOTE: TESTcode for forcing a splitable hand
# while(first):
#     if deck.cardsLeft()>= 2:
#         if hand.canSplit():
#             print( "{} is holding {}.".format(player1._name,hand1.displayHand()) )
#             break
#
#         player1.reset()
#         for i in range(2):
#             new_card = deck.draw()
#             hand1.add(new_card)
#     else:
#         print("Drew whole deck,trying again")
#         deck = Deck()
#         player1.reset()

#NOTE: TESTcode for forcing an ace
# while(True):
#     new_card = deck.draw()
#     print(new_card.display())
#     print(new_card.isAce())
#     if new_card.isAce():
#         player1_hand1.add(new_card)
#         break
#     else:
#         continue
