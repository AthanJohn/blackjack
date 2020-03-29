import random
from functions import try_except_else

class Deck():

    
    def __init__(self,cards,deck):
        self.cards = cards
        self.deck = deck


    def create(self,suits):
        for card in self.cards:
            for suit in suits:
                complete_card = card + ' of ' + suit
                self.deck.append(complete_card)
        return self.deck

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck





class Balance():


    def __init__(self,amount,bet):
        self.amount = amount
        self.bet = bet

    def add_bet(self):

        while True:
            if self.amount < self.bet:
                message = 'Your bet is bigger than your balance. Please choose another bet: '
                self.bet = try_except_else(message)
            else:
                print('Your bet is: ', self.bet)
                self.amount -= self.bet
                break

    def print_balance(self):
        print('Your balance is: ',self.amount)

    def win(self):

        self.amount += (self.bet*2)

    def tie(self):
        self.amount += self.bet


class Hands():

    def __init__(self,player,deck,h_cards,score):
        self.player = player
        self.deck = deck
        self.h_cards = h_cards
        self.score = score


    def give_hand(self):
            self.h_cards.append(self.deck[0])
            self.deck.pop(0)

    def show_cards(self):
        print("The {}'s cards are:".format(self.player))
        print(*self.h_cards, sep= "\t,\t")
        print("Total points: {}".format(self.score))
        print('\n')

    def calculate_score(self,cards):
        rank_only = self.h_cards[-1].split()
        self.score += cards[rank_only[0]]