import Deck
import Constants
import copy

class Platfrom:

    def __init__(self, deck):
        self.deck = deck
        self.cardPool = []
        self.cardsOnDesk = []
        self.chosenCards = []
        self.historicalCards = []
        self.totalCardsNumber = 45 #len(deck.cardList)

    def getNumberOfCardsOnDesk(self):
        count = 0
        for card in self.cardsOnDesk:
            if card != -1:
                count += 1
        return count

    def restOfCard(self):
        return len(self.cardPool)

    def fillCardsOnDesk(self):
        if len(self.cardsOnDesk) == 0:
            for i in range(0, Constants.DESK_CARDS_CAPACITY):
                self.cardsOnDesk.append(self.cardPool.pop())
        else:
            if len(self.cardPool) > 0:
                if Constants.DESK_CARDS_CAPACITY - self.getNumberOfCardsOnDesk() <= len(self.cardPool):
                    for i in range(0, Constants.DESK_CARDS_CAPACITY):
                        if self.cardsOnDesk[i] == -1:
                            self.cardsOnDesk[i] = self.cardPool.pop()
                else:
                    for i in range(0, len(self.cardPool)):
                        self.cardsOnDesk[self.cardsOnDesk.index(-1)] = self.cardPool.pop()

    def chooseCard(self, index):
        card = self.cardsOnDesk[index]
        result = -1
        if card in self.chosenCards:
            return -1
        elif len(self.chosenCards)==Constants.MAX_SUBMIT_CARDS_NUM:
            first = self.chosenCards[0]
            self.chosenCards = self.chosenCards[1:]
            result = self.findCardOnDesk(first)
        self.chosenCards.append(card)
        return result

    def findCardOnDesk(self,card):
        for i in range(0,len(self.cardsOnDesk)):
            if self.cardsOnDesk[i]!=-1 and self.cardsOnDesk[i] == card:
                return i
        return -1

    def cancelChosen(self, card):
        if self.chosenCards[0]==card:
            self.chosenCards = self.chosenCards[1:]
            return
        if self.chosenCards[len(self.chosenCards)-1]==card:
            self.chosenCards = self.chosenCards[0:len(self.chosenCards)-1]
            return
        for i in range(0,len(self.chosenCards)):
            if self.chosenCards[i] == card:
                self.chosenCards = self.chosenCards[0:i-1]+self.chosenCards[i+1:]
                return

    def cancelAllChosen(self):
        self.chosenCards = []

    def clearDesk(self):
        self.cardsOnDesk = []

    def clearHistory(self):
        self.historicalCards = []

    def makeSet(self):
        position = []
        for card in self.chosenCards:
            index = self.findCardOnDesk(card)
            self.cardsOnDesk[index] = -1
            self.historicalCards.append((card,index))
            position.append(index)
        self.cancelAllChosen()
        return position

    def getHistory(self):
        return self.historicalCards

    def readForGame(self):
        self.clearDesk()
        self.clearHistory()
        self.cancelAllChosen()
        self.cardPool = copy.deepcopy(self.deck.shuffle())
        self.cardPool = self.cardPool[:33]
        print(len(self.cardPool))
        self.fillCardsOnDesk()
