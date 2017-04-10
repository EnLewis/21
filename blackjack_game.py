from TwentyOne import *

def checkBet(player, lower_limit):
    """
        getBet takes a player and the lower bet limit
        and asks for a bet input from the player

        Returns: bet amount (int)
    """
    bet = input("Place your bet, {}. The lower limit is {} and you have {} left.\n".format(player.name(), lower_limit,player.wallet()))
    while(True):
        # input check for integer
        while(not bet.isdigit()):
            bet = input("Bets must be integers, lower limit is {}.\n".format(lower_limit))
        # input check for within number of players
        bet = int(bet)
        if bet < lower_limit:
            bet = input("Bet is too low, lower limit is {}.\n".format(lower_limit))
        elif bet > player.wallet():
            bet = input("You cannot afford that bet {}.\n".format(player.name()))
        else:
            # exit input check loop
            return bet

def list_converter(lst, sep=' ', final_sep=None):
    '''
        Returns a space seperated 'list' as a string.
        Args:
            lst: list of items to be printed as a string
            (optional) sep: the seperator, default space
        Returns:
            Space seperated string (default)
    '''
    if final_sep is None:
        final_sep = sep

    string = '{}'.format(lst[0])
    for i in range(len(lst)-1):
        if i != 0:
            string = '{}{}{}'.format(string, sep, lst[i])

    string = '{}{}{}'.format(string,final_sep,lst[-1])
    return string

def makeChoiceString(player, hand):
    '''
        Returns a list of choices, choices are limited
        by the options available to the player.
        Also returns a string to be displayed to the player.

        Args:
            player (Player): current player
            hand (Hand): current hand of the current player

        Returns:
            (list, string): list of choices and the string
                            to display at the user
    '''
    choice_list = ['Hit','Stay', 'Surrender']
    cards = hand.cards()
    if hand.canSplit(player):
        choice_list.append('Split')
    if player.canDouble(hand):
        choice_list.append('Double Down')

    return (choice_list, list_converter(choice_list,sep=', ', final_sep=', or '))

def modify_hi_lo(hi_lo_counter, card):
    if card.rank() in '23456':
        hi_lo_counter += 1
    elif card.rank() in 'TJQKA':
        hi_lo_counter -= 1
    return hi_lo_counter

def makeAiChoice(hand, dealer_upcard):
    # TODO: CHOOSE AI IMPLEMENTATION
    return 'Hit'



# NOTE:program start

print("Welcome to Blackjack!")

num_players = input("How many players are with us today?\n")
# check for proper input
while(not num_players.isdigit()):
    num_players = input("Please enter a valid number of players.\n")

num_players = int(num_players)
num_AI = input("And how many should be computer controlled? (max: {})\n".format(num_players))

while(True):
    # input check for integer
    while(not num_AI.isdigit()):
        num_AI = input("Please enter a valid number of computer players. (max: {})\n".format(num_players))
    # input check for within number of players
    num_AI = int(num_AI)
    if num_AI > num_players:
        num_AI = input("Please enter a valid number of computer players. (max: {})\n".format(num_players))
    else:
        # exit input check loop if number is integer and within number of players limit
        break

players = list()

# initialize player names and wallets
for i in range(num_players - num_AI):
    name = input("Player{}'s name?\n".format(i+1))
    wallet = input("How much money is {} carrying?\n".format(name))

    # check wallet input
    while(not wallet.isdigit()):
        wallet = input("Please enter a valid amount of money.\n")

    wallet = int(wallet)
    players.append(Player(name, wallet))

# initialize computer player names and inputs
for i in range(num_AI):
    name = input("Computer{}'s name?\n".format(i+1))
    wallet = input("How much money is {} carrying?\n".format(name))

    # check wallet input
    while(not wallet.isdigit()):
        wallet = input("Please enter a valid amount of money.\n")

    wallet = int(wallet)
    betting_unit = input("What betting unit should this computer use?\n")

    while(not betting_unit.isdigit()):
        betting_unit = input("Please enter a valid amount of money per unit.\n")
    # create a player in the player list with AI set to true

    players.append(Player(name, wallet, True, betting_unit))

# initialize decks, define lower table limit
deck = Deck(2)
deck.shuffle()
lower_limit = 5

# card counters
#
# high low counter demonstrates the player advantage.
# Positive counter means the player has the advantage.
# Negative counter means the dealer has the advantage.
# increase by 1 for every low card (2,3,4,5,6)
# decrease by 1 for every high card (10,J,Q,K,A)
# else do nothing
# high low AI will use this for determining bet
hi_lo_counter = 0

print("Preperations are completed, Blackjack will now commence.")

while(players):
    # keep track of players who can't play
    poor_players = []
    # create dealer as extra player
    dealer = Player("Dealer", 0)
    #####################################
    # step 1 of a round: get player bets/hands and dealer hand
    # also remove any player unable to play
    for i,player in enumerate(players):
        if player.wallet() < lower_limit:
            print("We must ask {} to leave the table, as he cannot afford the lower limit bet".format(player.name()))
            poor_players.append(i)
            continue

        if player._ai:
            betting_units = deck.trueCountHiLo(hi_lo_counter)
            if betting_units == 0:
                bet = lower_limit
            else:
                bet = betting_units * player.bettingUnit()

            if bet > player.wallet():
                bet = player.wallet()
            input("Player {} has bet {}.".format(player.name(), bet))
        else:
            # check user input with checkBet and obtain a valid bet
            bet = checkBet(player,lower_limit)

        # create hand for player
        hand = Hand()
        cards = deck.drawMultiple(2)
        for card in cards:
            hand.add(card)

        # apply bet amount to player wallet,
        # associate bet amount to hand
        # give hand to the player
        player.getBet(hand,bet)
        player.addHand(hand)

    poor_players.reverse()
    # remove players who are out of money
    for i in poor_players:
        players.pop(i)
    # exit early if no players left
    if not players:
        break
    # give the dealer a hand
    hand = Hand()
    cards = deck.drawMultiple(2)
    for card in cards:
        hand.add(card)

    dealer.addHand(hand)

    ####################################
    # step 2: display all current hands
    print("The hands have been dealt:")
    for player in players:
        curr_hand = player.hands()[0]

        # manage the card counter for high low counting
        for card in curr_hand.cards():
            hi_lo_counter = modify_hi_lo(hi_lo_counter,card)

        curr_hand = list_converter(curr_hand.displayHand(), sep=', ')
        print("{} has a hand of {}".format(player.name(), curr_hand))
    dealer_upcard = dealer.returnHandsHeld()[0])
    input("The dealer currently holds a {}".format(dealer_upcard))
    # store dealer upcard value for ai implementation
    dealer_upcard = dealer.hands()[0].cards[0].value()

    ###################################
    # step 3: handle each players' turns
    choice_to_num = {'Hit': 1, 'Stay':2, 'Double Down':3, 'Split':4, 'Surrender':5}

    for player in players:
        for hand in player.hands():
            print("\nIt is {}'s turn to play.".format(player.name()))
            while(not hand.isBust()):
                str_hand = list_converter(hand.displayHand(), sep=', ')
                print("\n{}, your current hand is:\n{}".format(player.name(), str_hand))
                input("with a value of {}. The bet on this hand is {}".format(hand.handValue(),hand.bet()))

                # player makes a choice now
                if not player.isAi():
                    choice_list, choice_string = makeChoiceString(player, hand)
                    choice = input('{}?\n'.format(choice_string))
                    while (not choice in choice_list):
                        choice = input('{}?\n'.format(choice_string))
                else:
                    choice = makeAiChoice(hand,dealer_upcard)

                # we have a valid choice now
                if choice == 'Hit' or choice == 'Double Down':
                    card = player.play(choice_to_num[choice],deck,hand)
                    # toggle hi_lo_counter
                    hi_lo_counter = modify_hi_lo(hi_lo_counter,card)

                    if choice == 'Double Down':
                        break

                elif choice == 'Stay':
                    break

                elif choice == 'Split':
                    cards = player.play(choice_to_num[choice],deck,hand)

                    for card in cards:
                        hi_lo_counter = modify_hi_lo(hi_lo_counter,card)

                elif choice == 'Surrender':
                    player.play(choice_to_num[choice],deck,hand)
                    break

            if choice == 'Surrender':
                print("Surrendered, half of bet is returned wallet is now {}.".format(player.wallet()))

            elif hand.isBust():
                print("Bust! {} lost {}$.".format(player.name(), hand.bet()))

    ###################################
    # step 4: play dealer's turn and compare hand values with dealer
    #         dealer stays on 17 or higher.
    while(True):
        dealer_hand = dealer.hands()[0]
        str_hand = list_converter(dealer_hand.displayHand(), sep=', ')
        input("The dealer's hand is:\n{}".format(str_hand))
        dealer_hand_value = dealer_hand.handValue()

        # dealer busted payout to all players who didn't bust
        if dealer_hand.isBust():
            print("Dealer bust!")
            for player in players:
                for hand in player.hands():
                    if not hand.isBust():
                        if hand.handValue() == 21 and len(hand.cards()) == 2:
                            player.addWallet(1.5*hand.bet())
                        player.addWallet(2*hand.bet())
                print("{} now has {}$".format(player.name(),player.wallet()))
            break

        # dealer is at 17 or higher, compare with players
        # add bet to wallet
        elif dealer_hand_value >= 17:
            str_hand = list_converter(dealer_hand.displayHand(), sep=', ')
            print("Dealer stays on\n{}\nHand value of {}".format(str_hand, dealer_hand_value))
            for player in players:
                for hand in player.hands():
                    if not hand.isBust():
                        if dealer_hand_value < hand.handValue():
                            player.addWallet(2*hand.bet())
                        elif dealer_hand_value == hand.handValue():
                            if hand.handValue() == 21 and len(hand.cards()) == 2:
                                player.addWallet(1.5*hand.bet())
                            else:
                                player.addWallet(hand.bet())
                print("{} now has {}$".format(player.name(),player.wallet()))
            break
        elif dealer_hand_value < 17:
            dealer.play(1, deck, dealer_hand)

    ###################################
    # last step: reset all hands
    for player in players:
        player.reset()
