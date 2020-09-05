import Card
import tkinter as tk
import Constants as consts
Card = Card.Card

class Deck:
    
    def __init__(self):
        self.cardList = []
        self.chosenCards = []
        self.deskCards = []
        self.deskSize = consts.DESK_CARDS_CAPACITY
        self.colorList = consts.COLOR_LIST
        self.fillList = consts.FILL_LIST
        self.shapeList = consts.SHAPE_LIST
        self.numList = consts.NUM_LIST
        index = 1
        for color in self.colorList:
            for fill in self.fillList:
                for shape in self.shapeList:
                    for number in self.numList:
                        cardUrl = consts.IMAGE_PATH+color+" "+fill+" "+shape+str(index)+consts.IMAGE_FORMAT
                        self.cardList.append(Card(color, fill, shape, number,cardUrl))
                        index = index+1

    def getNumberOfCards(self):
        return len(self.cardList)

    #takes in an integer (1-81) and returns the index at that card
    def getCard(self, CardNumber):
        return self.cardList[CardNumber]
    
    #takes in an interger index and choose the card from deskCards, put its index into chosenCards
    def chooseCardFromDesk(self,index):
        pass

    
    def chooseCardsFromDesk(self,indexes):
        pass

    #randomly choose a card from deskCards, put its index into chosenCards
    def chooseCardFromDeskRandom(self):
        pass

    
    def chooseCardsFromDeskRandom(self):
        pass

    #cancel the chosen statue of one card, given index of the card in chosenList
    def cancelChosen(self, index):
        pass

    #cancel all the chosen cards'chosen statue, clear chosenList and put all cards in it back to cardList
    def cancelAllChosen(self):
        pass

    #takes an input n (1-len(cardList)) and randomly pick cards and put them on the desk util reach n
    def fillDesk(self,n):
        pass

    #put all deskcards back to cardList
    def clearDesk(self):
        pass

    #initialize the desk
    def initializeDeck(self):
        self.cancelAllChosen()
        self.clearDesk()
        self.shuffle()
        self.fillDesk(self.deskSize)

    #shuffle method with three shuffles
    def shuffle(self):
        import random
        random.shuffle(self.cardList)
        random.shuffle(self.cardList)
        random.shuffle(self.cardList)
        return self.cardList
