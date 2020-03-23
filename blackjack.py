import random

class Deck():


    def __init__(self,cards,deck):
        self.cards = cards
        self.deck = deck


    def create(self):
        for card in self.cards:
            for i in range(4):
                self.deck.append(card)
        return self.deck

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck



class Balance():


    def __init__(self,amount):
        self.amount = amount

    def add_bet(self,bet):

        while True:
            if self.amount < bet:
                print('Your bet must not exceed your available chips.')
                bet = float(input('Please choose another bet: '))
            else:
                self.amount -= bet
                break

    def print_balance(self):
        print('Your balance is: ',self.amount)

    def win(self,bet):

        self.amount += (bet*2)


class Hands():

    def __init__(self,player,deck):
        self.player = player
        self.deck = deck


    def hand(self):
            holding_cards = [self.deck[:1]]
            self.desk.pop(0)


cards = {'A': 1 , 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
                     'Jack': 10, 'Queen': 10, 'King': 10}



Deck = Deck(cards,[])

deck = Deck.create()

sh_deck = Deck.shuffle()

while True:
    try:
        balance = float(input('What is your balance? '))
    except:
        print('An error occurred! Please try again!')
        continue
    else:
        print('Your initial amount is: ',balance)
        break




while True:
    try:
        bet = float(input('How much money do you want to bet? '))
    except:
        print('An error occurred! Please try again!')
        continue
    else:
        print('Your bet is: ',balance)
        break

Balance = Balance(balance)
Balance.add_bet(bet)



