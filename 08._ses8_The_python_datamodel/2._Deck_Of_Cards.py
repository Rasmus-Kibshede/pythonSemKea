class Deck:
    def __init__(self):
        self.cards = ('A', 'K', 4, 7)
    

    def __repr__(self):
        return f'{vars(self)}'

    def __str__(self):
        return f'{self.cards}'

    # Checker om value er i cards
    def __contains__(self, value):
        if value in self.cards:
            return True
        else:
            return False
    
    # Tager index af cards
    def __getitem__(self, key):
        return self.cards[key]

    def __len__(self):
        return len(self.cards)
    
    def __add__(self, other):
        deck = Deck()
        deck.cards = self.cards + other.cards
        return deck
    
    def __setitem__(self, index, card):
        __cardList = list(self.cards)
        __cardList.insert(index, card)
        self.cards = tuple(__cardList)
    
    def __delitem__(self, key):
        self.cards = list(self.cards)
        del(self.cards[key])
        self.cards = tuple(self.cards)
        
    
    

deck = Deck()
deck2 = Deck()

print('A' in deck)

print(deck[1])

print(deck + deck2)

print(len(deck))


print(repr(deck))

deck[0] = 12

print(deck)

del(deck[0])

print(deck)
