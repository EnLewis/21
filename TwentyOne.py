#TODO: Implement handling for two aces in hand at once
import itertools
import random

# Two dictionary of more verbose card suits and ranks for output purposes
suit_verbose = {"s":"Spades", "c":"Clubs", "h":"Hearts", "d":"Diamonds"}
rank_verbose = {"2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9", "T": "10",
                    "J":"Jack", "Q":"Queen", "K":"King", "A":"Ace"}
class Card:

    def __init__(self,rank,suit):
        self._rank = rank
        self._suit = suit

    def value(self):
        value = 0
        ace = 0
        rank = ord(self._rank)

        if rank == 65: # Ace
            value = 1
            # As of right now aces are only worth one because I need to decide how
            # to deal with multiple aces in one hand

        elif rank in range(50,57): # Non face card or ten
            value = int(chr(rank))

        else: # All remaining cards are worth 10
            value = 10

        return value

    def isAce(self):
        if self._rank == "A":
            return True
        else:
            return False

    def display(self):
        return "{} of {}".format(rank_verbose[self._rank], suit_verbose[self._suit])

class Hand:

    def __init__(self):
        self._hand = []

    def add(self,card):
        self._hand.append(card)

    def handValue(self):
        value = 0
        for card in self._hand:
            value += card.value()

        return value

    def cards(self):
        return self._hand

    def displayHand(self):
        display = list()
        for card in self._hand:
            display.append(card.display())

        return display

class Deck:

    suit = "schd"
    rank = "23456789TJQKA"

    def __init__(self):
        # self._deck = [''.join(card) for card in itertools.product(Deck.suit,Deck.rank)] # list of versions of cards
        self._deck = [Card(j,i) for i in self.suit for j in self.rank]


    def shuffle(self):
        ''' Shuffles the current deck '''
        random.shuffle(self._deck)

    def drawMultiple(self,num_todraw):
        ''' Draws a select number of cards from the current deck and returns them
        as a list
        '''
        result = list()

        for i in range(num_todraw):
            #Draw off the top of the deck
            result.append( self._deck.pop(0) )

        return result

    def draw(self):
        ''' Draw one card from the top of the deck'''

        return self._deck.pop(0)

    def isEmpty(self):
        ''' Checks if the deck is empty '''

        if len(self._deck) > 0:
            return False
        else:
            return True

    def cardsLeft(self):
        ''' Returns the number of cards left in the deck. This is mostly
        to improve readability
         '''
        return len(self._deck)

    def displayDeck(self):
        display = list()
        for card in self._deck:
            display.append(card.display())

        return display

class Player:

    def __init__(self,name,wallet):
        self._name = name
        self._wallet = wallet
        self._hand = Hand()
        self._bet = 0
        self._isBust = False

    def play(self,deck,choice):
        ''' Exectute the players choice for this hand '''
        # Hit
        if choice == 1:
            if deck.cardsLeft() >= 1:
                self._hand.add(deck.draw())
                if self._hand.handValue() > 21:
                    self._isBust = True

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

    def reset(self):
        self._hand = []
        self._bet = 0
        self._isBust = False
