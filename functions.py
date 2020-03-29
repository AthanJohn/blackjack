def making_choice(message):
    choice = input(message)
    
    while True:
        if choice == 'Y' or choice == 'N':
            break
        else:
            choice = input('Choose Y or N: ')

    return choice


def try_except_else(message):
    while True:
        try:
            choice = float(input(message))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break

    return choice


def turns(player, cards):

    player.give_hand()
    player.calculate_score(cards)
    player.show_cards()

    

def who_wins(Balance, de_hands, pl_hands, cards):
    while True:
        message = "Do you want to draw another card? Y or N\t"
        draw_again = making_choice(message)
        if draw_again == 'N':
            break
        
        turns(pl_hands,cards)
        if pl_hands.score > 21:
            print('Player is busted with {} score! Dealer won!'.format(pl_hands.score))
            break
    
    if pl_hands.score <= 21:
        while de_hands.score < 17:
            turns(de_hands,cards)

        if de_hands.score > 21:
            print('Dealer is busted with {} score! Player won!'.format(de_hands.score))
            Balance.win()
        else:
            if de_hands.score > pl_hands.score:
                print("Dealer's points:\t{}\nPlayer's points:\t{}\nDealer wins!".format(de_hands.score,pl_hands.score))
            elif de_hands.score < pl_hands.score:
                print("Dealer's points:\t{}\nPlayer's points:\t{}\nPlayer wins!".format(de_hands.score,pl_hands.score))
                Balance.win()
            else:
                print('We have a tie!')
                Balance.tie()
    