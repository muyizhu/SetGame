import Card
import tkinter as tk
import Constants as consts
import random
Card = Card.Card

class Deck:
    
    def __init__(self):
        self.cardDict = []
        self.chosenCards = []
        self.deskCards = []
        self.cardPool = []
        self.deskCapacity = consts.DESK_CARDS_CAPACITY
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
                        card = Card(index-1,color, fill, shape, number,cardUrl)
                        self.cardDict.append(card)
                        self.cardPool.append(card)
                        index = index+1

    def getNumberOfCards(self):
        return len(self.cardDict)

    #takes in an integer (1-81) and returns the index at that card
    def getCard(self, ID):
        return self.cardDict[ID]
    
    #takes in an interger index and choose the card from deskCards, put its index into chosenCards
    def chooseCardFromDesk(self,ID):
        pass

    
    def chooseCardsFromDesk(self,IDs):
        pass

    #randomly choose a card from deskCards, put its index into chosenCards
    def chooseCardFromDeskRandom(self):
        pass

    
    def chooseCardsFromDeskRandom(self):
        pass

    #cancel the chosen statue of one card, given index of the card in chosenList
    def cancelChosen(self, ID):
        pass

    #cancel all the chosen cards'chosen statue, clear chosenList and put all cards in it back to cardList
    def cancelAllChosen(self):
        self.chosenCards = []

    #Fill the Desk with cards until its MAX capacity
    def fillDesk(self,n):
        random.shuffle(self.cardPool)
        for i in range(0,len(self.deskCapacity)):
            if len(self.deskCards) <= self.deskCapacity or self.deskCards[i] == None:
                self.deskCards[i] = self.cardPool.pop()

    #put all cards on desk back to cardList
    def clearDesk(self):
        for card in self.deskCards:
            self.cardPool.append(card)
        self.deskCards = []

    #initialize the desk
    def readyForGame(self):
        self.cancelAllChosen()
        self.clearDesk()
        self.shuffle()
        self.fillDesk(self.deskCapacity)

    #shuffle method with three shuffles
    def shuffle(self):
        random.shuffle(self.cardPool)
        random.shuffle(self.cardPool)
        random.shuffle(self.cardPool)
