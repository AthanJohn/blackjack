from functions import try_except_else,who_wins,making_choice
from classes import *


cards = {'Ace': 1 , 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
                     'Jack': 10, 'Queen': 10, 'King': 10}
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

Deck = Deck(cards,[])
deck = Deck.create(suits)

message = 'Please, enter your Balance: '
balance = try_except_else(message)
Balance = Balance(balance,0)

while True:
    sh_deck = Deck.shuffle()
    Balance.print_balance()

    message = 'Please, enter your bet: '
    Balance.bet = try_except_else(message)

    Balance.add_bet()

    p_h_cards = []
    d_h_cards = []

    pl_hands = Hands("Player", sh_deck, p_h_cards,0)
    de_hands = Hands("Dealer", sh_deck, d_h_cards,0)

    for i in range(2):
        
        de_hands.give_hand()
        de_hands.calculate_score(cards)
        if i == 0:
            de_hands.show_cards()
        
        
        pl_hands.give_hand()
        pl_hands.calculate_score(cards)
        if i == 1:
            pl_hands.show_cards()
        

    who_wins(Balance, de_hands, pl_hands, cards)

    print('\n')
    Balance.print_balance()

    if(Balance.amount == 0):
        print("You lost all of your money! See ya!")
        break

    message = "Do you want to play again? Y or N\t"
    play_again = making_choice(message)
        
    if play_again == 'N':
        print('See ya!')
        break
