import Constants
import Deck
class Desk:
    def __init__(self):
        self.cardGrave = []
        self.cardsOnDesk = []
        self.numberOfCardsOnDesk
        self.cardDeck = Deck()
        self.cardDeck.shuffle()

    def setNumberOfCardsOnDesk(self):
        self.numberOfCardsOnDesk = len(self.cardsOnDesk)

    def getNumberOfCardsOnDesk(self):
        return self.numberOfCardsOnDesk

    def getNumberOfRestOfCards(self):
        return len(self.cardDeck.cardPool)

    def dealCards(self):
        if self.getNumberOfRestOfCards() != 0:
            if self.getNumberOfCards() == 0:
                for index in range(0, Constants.DESK_CARDS_CAPACITY):
                    self.cardsOnDesk = self.cardDeck.cardPool.pop()
                self.setNumberOfCardsOnDesk()
            else:
                