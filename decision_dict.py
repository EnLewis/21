################################
# THIS CODE IMPLEMENTS BLACKJACK BASIC STRATEGY
# ACCORDING TO THESE CHARTS:
# https://www.blackjackapprenticeship.com/wp-content/uploads/2012/12/BJA-basic-strategy2.png
################################

dealer_upcards = [x for x in range(1,11)]
split_decision = set()
# generate all possible soft totals
totals = [2*x for x in range(1,11)]

# generate split totals decision set
for total in totals:
    for dealer_upcard in dealer_upcards:
        # 5s and 10s
        if total in {20,10}:
            continue
        # aces and 8s
        elif total in {2,16}:
            split_decision.add((total, dealer_upcard))
        # 9s
        elif total == 18 and not dealer_upcard in {7,10,1}:
            split_decision.add((total, dealer_upcard))
        # 7s
        elif total == 14 and dealer_upcard < 8:
            split_decision.add((total, dealer_upcard))
        # 6s
        elif total == 12 and dealer_upcard < 7:
            split_decision.add((total, dealer_upcard))
        # 4s
        elif total == 8 and dealer_upcard in {5,6}:
            split_decision.add((total, dealer_upcard))
        # 3s and 2s
        elif total in {4,6} and dealer_upcard < 8:
            split_decision.add((total, dealer_upcard))

hard_decision = dict()
# generate all possible hard totals
totals = [x for x in range(4,22)]

for total in totals:
    for dealer_upcard in dealer_upcards:
        #17 and higher
        if total >= 17:
            hard_decision[(total, dealer_upcard)] = 'Stay'
        # 8 and lower
        elif total <= 8:
            hard_decision[(total, dealer_upcard)] = 'Hit'
        # 16 to 13
        elif total < 17 and total > 12:
            if dealer_upcard in {1,7,8,9,10}:
                hard_decision[(total, dealer_upcard)] = 'Hit'
            else:
                hard_decision[(total, dealer_upcard)] = 'Stay'
        # 12
        elif total == 12:
            if dealer_upcard in {4,5,6}:
                hard_decision[(total, dealer_upcard)] = 'Stay'
            else:
                hard_decision[(total, dealer_upcard)] = 'Hit'
        # 11
        elif total == 11:
            hard_decision[(total, dealer_upcard)] = 'Double Down'
        # 10
        elif total == 10:
            if dealer_upcard in {1, 10}:
                hard_decision[(total, dealer_upcard)] = 'Hit'
            else:
                hard_decision[(total, dealer_upcard)] = 'Double Down'
        # 9
        elif total == 9:
            if dealer_upcard in {3,4,5,6}:
                hard_decision[(total, dealer_upcard)] = 'Double Down'
            else:
                hard_decision[(total, dealer_upcard)] = 'Hit'

soft_decision = dict()
# generate all possible soft totals
totals = [x for x in range(13,22)]

for total in totals:
    for dealer_upcard in dealer_upcards:
        # 20 and 21
        if total >= 20:
            soft_decision[(total, dealer_upcard)] = 'Stay'
        # 19
        elif total == 19:
            if dealer_upcard == 6:
                soft_decision[(total, dealer_upcard)] = 'Double Down'
            else:
                soft_decision[(total, dealer_upcard)] = 'Stay'
        # 18
        elif total == 18:
            if dealer_upcard in {2,3,4,5,6}:
                soft_decision[(total, dealer_upcard)] = 'Double Down'
            elif dealer_upcard in {7,8}:
                soft_decision[(total, dealer_upcard)] = 'Stay'
            else:
                soft_decision[(total, dealer_upcard)] = 'Hit'
        # 17
        elif total == 17:
            if dealer_upcard in {3,4,5,6}:
                soft_decision[(total, dealer_upcard)] = 'Double Down'
            else:
                soft_decision[(total, dealer_upcard)] = 'Hit'
        # 16 and 15
        elif total in {16,15}:
            if dealer_upcard in {4,5,6}:
                soft_decision[(total, dealer_upcard)] = 'Double Down'
            else:
                soft_decision[(total, dealer_upcard)] = 'Hit'
        # 14 and 13
        elif total in {14,13}:
            if dealer_upcard in {5,6}:
                soft_decision[(total, dealer_upcard)] = 'Double Down'
            else:
                soft_decision[(total, dealer_upcard)] = 'Hit'
