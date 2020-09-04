import Card
import tkinter as tk
Card = Card.Card

class Deck:
    
    def __init__(self):
        self.cardList = []
        self.chosenCards = []
        self.colorList = ['red','blue','green']
        self.fillList = ['solid', 'shaded', 'clear']
        self.shapeList = ['circle', 'triangle','square']
        self.numList = ['1','2','3']

        for color in self.colorList:
            for fill in self.fillList:
                for shape in self.shapeList:
                    for number in self.numList:
                        self.cardList.append(Card(color, fill, shape, number))

    def getNumberOfCards(self):
        return len(self.cardList)

    #takes in an integer (1-81) and returns the index at that card
    def getCard(self, CardNumber):
        return self.cardList[CardNumber]
    
    #takes in an interger index and draw the index card out of cardList, mark it as chosen and return the card
    def chooseCard(self,index){}

    #takes in an index list (1-len(cardList)) and draw all cards out into chosenCards and return the draw out cards as list
    def chooseCards(self,indexes){}

    #random choose one card, and return the card
    def chooseCardRandom(self){}

    #random choose cards, return cards
    def chooseCardsRandom(self){}

    #cancel the chosen statue of one card, given index of the card in chosenList
    def cancelChosen(self, index){}

    #cancel all the chosen cards'chosen statue, clear chosenList and put all cards in it back to cardList
    def cancelAllChosen(self){}

    #initialize the whole deck to its init statue
    def initializeDeck(self){
        cancelAllChosen()
        shuffle()
    }

    #shuffle method with three shuffles
    def shuffle(self):
        import random
        random.shuffle(self.cardList)
        random.shuffle(self.cardList)
        random.shuffle(self.cardList)
        return self.cardList
