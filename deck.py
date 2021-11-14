import random

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    
    def __unicode__(self):
        return self.show()
    def __str__(self):
        return self.show()
    def __repr__(self):
        return self.show()
        
    def show(self):
        if self.value == 1:
            val = "Туз"
        elif self.value == 11:
            val = "Валет"
        elif self.value == 12:
            val = "Дама"
        elif self.value == 13:
            val = "Король"
        else:
            val = self.value

        return "{} {}".format(val, self.suit)


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    # Показати усі карти в колоді
    def show(self):
        for card in self.cards:
            print (card.show())

    # Генерує 52 карт
    def build(self):
        self.cards = []
        for suit in ['Чирва', 'Хреста', 'Бубна', 'Піка']:
            for val in range(1,14):
                self.cards.append(Card(suit, val))

    # Тусувати колоду
    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            # алгоритм
            for i in range(length-1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]
            
            # random.shuffle(self.cards)

    # повернути верхню карту
    def deal(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def sayHello(self):
        print ("Привіт, моє ім'я {}".format(self.name))
        return self

    # Витащити кількість карт з колоди
    # Повертається true в n картках, false, якщо менше, ніж це
    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else: 
                return False
        return True

    # Покажіть усі карти в руці гравця
    def showHand(self):
        print ("рука {}а : {}".format(self.name, self.hand))
        return self

    def discard(self):
        return self.hand.pop()

# тест
# card = Card('Spades', 6)
# print card

# тест колоди
myDeck = Deck()
myDeck.shuffle()
#deck.show()

maxim = Player("Maxim")
maxim.sayHello()
maxim.draw(myDeck, 6)
maxim.showHand()



