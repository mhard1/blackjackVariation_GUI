import random

class Deck:
    def __init__(self):
        self.deck = []
        self.hand=[]
        self.suits = ['S', 'H', 'D', 'C']
        self.faces = ['J', 'Q', 'K', 'A']
        self.numbers = [x for x in range(2,11)]
        for suit in self.suits:
            for num in self.numbers:
                self.deck.append(str(num)+suit)
        for suit in self.suits:
            for face in self.faces:
                self.deck.append(face+suit)

    def showDeck(self):
        print(self.deck)

    def shuffleDeck(self):
        random.shuffle(self.deck)

    def deal(self, numCards=1, skip=None):
        if numCards == 1:
            self.hand.append(self.deck[0])
        else:
            if skip == None:
                for i in range(numCards):
                    self.hand.append(self.deck[i])
                return self.hand
            else:
                current = 0
                self.hand.append(self.deck[current])
                for i in range(numCards):
                    current += skip + 1
                    self.hand.append(self.deck[current])
                    return self.hand
    def dealMore(self):
        index = len(self.hand)
        nextCard = self.deck[index]
        self.hand.append(nextCard)
        return self.hand