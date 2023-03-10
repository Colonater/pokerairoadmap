import random

#defines the Card Class, has # values Self, Suits and Vaule
class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))
#Defines the Deck Class builds the deck, draws, shows and Shuffles the cards
class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))
                #print("{} of {}".format(v, s))
    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return(self.cards.pop())

# defines the player class who has a Name draws a card and can hold a card or discard it
class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()




#card = Card()
#card.show()

deck = Deck()
deck.shuffle()
#deck.show()
Stucky = Player("Stucky")
Stucky.draw(deck).draw(deck)
print("Stucky has the ")
Stucky.showHand()


#card = deck.draw()
#card.show()