#TODO: Implement handling for two aces in hand at once
import itertools
import random

# Two dictionary of more verbose card suits and ranks for output purposes
suit_verbose = {"s":"Spades", "c":"Clubs", "h":"Hearts", "d":"Diamonds"}
rank_verbose = {2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", "T": "10",
                    "J":"Jack", "Q":"Queen", "K":"King", "A":"King"}
class Card:
    def __init__(self,rank,suit):
        
class Deck:

    suit = "schd"
    rank = "23456789TJQKA"

    def __init__(self):
        self._deck = [''.join(card) for card in itertools.product(Deck.suit,Deck.rank)]

    def shuffle(self):
        ''' Shuffles the current deck '''
        random.shuffle(self._deck)

    def draw(self,num_todraw):
        ''' Draws a select number of cards from the current deck and returns them
        as a list
        '''
        result = list()

        for i in range(num_todraw):
            #Draw off the top of the deck
            result.append( self._deck.pop(0) )

        return result

    def isEmpty(self):
        ''' Checks of the deck is empty '''

        if len(self._deck) > 0:
            return False
        else:
            return True

    def cardsLeft(self):
        ''' Returns the number of cards left in the deck. This is mostly
        to improve readability
         '''
        return len(self._deck)

class Player:

    def __init__(self,name,wallet):
        self._name = name
        self._wallet = wallet
        self._hand = []
        self._bet = 0
        self._isBust = False


    def play(self,deck,choice):
        ''' Exectute the players choice for this hand '''
        # Hit
        if choice == 1:
            if deck.cardsLeft() >= 1:
                self._hand.append(deck.draw(1))

        # Stay
        elif choice == 2:
            pass

        # DoubleDown
        elif choice == 3:
            self.getBet(0,True)

        # Split
        elif choice == 4:
            # Make two seperate hands out of the cards currently in hand if
            # allowed (i.e cards_in_hand < 3, card[0] == card[1])
            pass

    def getBet(self, wager, doubleDown = False):
        ''' Place a bet on a hand and remove the amount wagered from the player's
        wallet'''
        if wager <= self._wallet:
            if doubleDown:
                self._wallet -= self._bet
                self._bet += self._bet
            else:
                self._wallet -= wager
                self._bet += wager

    def canDouble(self):
        ''' Determines whether a player has enough money to double down '''

        if (self._wallet - (2*self._bet)) < 0:
            return False
        else:
            return True

    def handValue(self):
        ace = 0
        value = 0
        alt_value = None
        for card in self._hand:
            rank = ord(card[1])

            if rank == 65: # Ace
                ace += 1
                value += 1

            elif rank in range(50,57): # Non face card or ten
                value += int(chr(rank))

            else: # All remaining cards are worth 10
                value += 10

        if ace:
            alt_value = value + ace*10
            output = (value,alt_value)
            return output
        else:
            return value

    def Reset(self):
        self._hand = []
        self._bet = 0
        self._isBust = False








print("Hello and welcome to 21.py! ")
print("please enter your total purse")
wallet = int(input())

player1 = Player("Daniel N.",wallet)


print(player1._wallet)
deck = Deck()
print(len(deck._deck))
deck.shuffle()
print(len(deck._deck))



#
# class Hand(self, cards):
#
# class Card(self, suit, rank):
