import Card
import tkinter as tk
import Constants as consts
Card = Card.Card

class Deck:
    
    def __init__(self):
        self.cardList = []
        self.chosenCards = []
        self.colorList = consts.COLOR_LIST
        self.fillList = consts.FILL_LIST
        self.shapeList = consts.SHAPE_LIST
        self.numList = consts.NUM_LIST
        index = 1
        for color in self.colorList:
            for fill in self.fillList:
                for shape in self.shapeList:
                    for number in self.numList:
                        cardUrl = consts.IMAGE_PATH+color+" "+fill+" "+shape+" "+index+".gif"
                        self.cardList.append(Card(color, fill, shape, number,cardUrl))
                        index = index+1

    def getNumberOfCards(self):
        return len(self.cardList)

    #takes in an integer (1-81) and returns the index at that card
    def getCard(self, CardNumber):
        return self.cardList[CardNumber]
    
    #takes in an interger index and draw the index card out of cardList, mark it as chosen and return the card
    def chooseCard(self,index):
        pass

    #takes in an index list (1-len(cardList)) and draw all cards out into chosenCards and return the draw out cards as list
    def chooseCards(self,indexes):
        pass

    #random choose one card, and return the card
    def chooseCardRandom(self):
        pass

    #random choose cards, return cards
    def chooseCardsRandom(self):
        pass

    #cancel the chosen statue of one card, given index of the card in chosenList
    def cancelChosen(self, index):
        pass

    #cancel all the chosen cards'chosen statue, clear chosenList and put all cards in it back to cardList
    def cancelAllChosen(self):
        pass

    #initialize the whole deck to its init statue
    def initializeDeck(self):
        self.cancelAllChosen()
        self.shuffle()

    #shuffle method with three shuffles
    def shuffle(self):
        import random
        random.shuffle(self.cardList)
        random.shuffle(self.cardList)
        random.shuffle(self.cardList)
        return self.cardList
