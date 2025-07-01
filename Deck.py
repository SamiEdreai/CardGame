import random
import Card

class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in Card.suits:
            for rank in Card.ranks:
                self.deck.append(Card.Card(suit,rank))  # build Card objects and add them to the list

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

new_deck = Deck()
var = new_deck.deck[0]
print(var)

class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet