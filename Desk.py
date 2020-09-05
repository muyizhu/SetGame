import Constants
import Deck
import Card

class Desk:

    def __init__(self):
        self.cardGrave = []
        self.cardsOnDesk = []
        self.choseCardsIndex = []
        self.numberOfCardsOnDesk = 0
        self.cardDeck = Deck()
        self.cardDeck.shuffle()

    def deskIsEmpty(self):
        if self.getNumberOfCardsOnDesk() == 0:
            return True
        else:
            return False

    def setNumberOfCardsOnDesk(self):
        count = 0
        for card in self.cardsOnDesk:
            if card == None:
                count += 1
        self.numberOfCardsOnDesk = Constants.DESK_CARDS_CAPACITY - count

    def setNumberOfCardsOnDesk(self, number):
        self.numberOfCardsOnDesk = number

    def getNumberOfCardsOnDesk(self):
        return self.numberOfCardsOnDesk

    def getNumberOfRestOfCards(self):
        return len(self.cardDeck.cardPool)

    def dealCards(self):
        if self.getNumberOfRestOfCards() != 0 and self.getNumberOfCardsOnDesk() < Constants.DESK_CARDS_CAPACITY:
            if self.deskIsEmpty():
                for i in range(0, Constants.DESK_CARDS_CAPACITY):
                    self.cardsOnDesk.append(self.cardDeck.cardPool.pop())
                self.setNumberOfCardsOnDesk(Constants.DESK_CARDS_CAPACITY)
            else:
                dealCardsNumber = Constants.DESK_CARDS_CAPACITY - self.getNumberOfCardsOnDesk()
                for i in range(0, dealCardsNumber):
                    self.cardsOnDesk[self.cardGrave(i,1)] = self.cardDeck.cardPool.pop()
                self.setNumberOfCardsOnDesk(Constants.DESK_CARDS_CAPACITY)


    def chooseCard(self, index):
        self.cardsOnDesk[index].chooseCard()
        self.choseCardsIndex.append(index)

    def cancelChooseCard(self, index):
        self.cardsOnDesk[index].cancelChooseCard()
        self.choseCardsIndex.remove(index)

    def removeCards(self):
        for index in self.choseCardsIndex:
            self.cardGrave.insert(0, (self.cardsOnDesk[index], index))
            self.cardsOnDesk[index] = None
        self.choseCardsIndex = []
        self.setNumberOfCardsOnDesk()