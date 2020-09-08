import Card
import tkinter as tk
import Constants as consts
import random
Card = Card.Card

class Deck:
    
    def __init__(self):
        self.cardDict = []  # card dictionary only for index or read card
        self.chosenCards = [] # cards who are chosen by player
        self.deskCards = [] # cards that player is playing 
        self.cardPool = [] # cards that store the real cards, it will decrease and increase dynamically.
        self.finishCards = []
        self.deskCapacity = consts.DESK_CARDS_CAPACITY 
        self.colorList = consts.COLOR_LIST
        self.fillList = consts.FILL_LIST
        self.shapeList = consts.SHAPE_LIST
        self.numList = consts.NUM_LIST
        index = 0
        num = 0
        for color in self.colorList:
            for fill in self.fillList:
                for shape in self.shapeList:
                    for number in self.numList:
                        cardUrl = consts.IMAGE_PATH+color+" "+fill+" "+shape+str(num%3+1)+consts.IMAGE_FORMAT
                        card = Card(index,color, fill, shape, number,cardUrl)
                        self.cardDict.append(card)
                        num = num+1
                        index = index+1

    def getNumberOfCards(self):
        return len(self.cardDict)

    #takes in an integer (1-81) and returns the index at that card
    def getCard(self, ID):
        return self.cardDict[ID]
    
    #takes in an interger index and choose the card from deskCards, put the card into chosenCards
    def chooseCardFromDesk(self,index):
        card = self.deskCards[index]
        result = -1
        if card in self.chosenCards:
            return -1
        elif len(self.chosenCards)==consts.MAX_SUBMIT_CARDS_NUM:
            first = self.chosenCards[0]
            self.chosenCards = self.chosenCards[1:]
            result = self.findCardInDesk(first)
        self.chosenCards.append(card)
        return result

    def changeDeskCards(self,keys):
        if len(self.cardPool)==0:
            return []
        desk = []
        replace = []
        for key in keys:
            desk.append(self.deskCards[key])
            if len(self.cardPool) > 0:
                self.deskCards[key] = self.cardPool.pop()
                replace.append(key)
            else:
                desk.pop()
                break
        for card in desk:
            self.cardPool.append(card)
        return replace

    def findCardInDesk(self,card):
        for i in range(0,len(self.deskCards)):
            if self.deskCards[i]!=-1 and self.deskCards[i] == card:
                return i
        return -1
    
    def findKeysOfDeskCards(self):
        keys = []
        for i in range(0,len(self.deskCards)):
            card = self.deskCards[i]
            if card!=-1:
                keys.append(i)
        return keys

    # def chooseCardsFromDesk(self,IDs):
    #     pass

    #randomly choose a card from deskCards, put its index into chosenCards
    def chooseCardFromDeskRandom(self):
        pass

    
    def chooseCardsFromDeskRandom(self):
        pass

    #cancel the chosen statue of one card, given index of the card in chosenList
    def cancelChosen(self, card):
        if self.chosenCards[0]==card:
            self.chosenCards = self.chosenCards[1:]
            return
        if self.chosenCards[len(self.chosenCards)-1]==card:
            self.chosenCards = self.chosenCards[0:len(self.chosenCards)-1]
            return
        for i in range(0,len(self.chosenCards)):
            if self.chosenCards[i] == card:
                self.chosenCards = self.chosenCards[0:i]+self.chosenCards[i+1:]
                return

    #cancel all the chosen cards'chosen statue, clear chosenList and put all cards in it back to cardList
    def cancelAllChosen(self):
        self.chosenCards = []

    #Fill the Desk with cards until its MAX capacity
    def fillDesk(self):
        filled = []
        random.shuffle(self.cardPool)
        for i in range(0,self.deskCapacity):
            if len(self.cardPool) == 0:
                return filled
            if i<len(self.deskCards) and self.deskCards[i] == -1:
                self.deskCards[i] = self.cardPool.pop()
                filled.append(i)
            elif i>=len(self.deskCards):
                filled.append(len(self.deskCards))
                self.deskCards.append(self.cardPool.pop())
        return filled
    
    

    #put all cards on desk back to cardList
    def clearDesk(self):
        for card in self.deskCards:
            if card != -1:
                self.cardPool.append(card)
        self.deskCards = []

    #initialize the desk
    def readyForGame(self):
        import copy
        self.clearFinishCards()
        self.cancelAllChosen()
        self.clearDesk()
        self.cardPool = copy.deepcopy(self.cardDict)
        self.shuffle()
        self.fillDesk()

    #shuffle method with three shuffles
    def shuffle(self):
        random.shuffle(self.cardPool)
        random.shuffle(self.cardPool)
        random.shuffle(self.cardPool)
    
    def clearFinishCards(self):
        self.finishCards = []

    def deleteChosenCardsFromDesk(self):
        uiposition = []
        for card in self.chosenCards:
            index = self.findCardInDesk(card)
            self.deskCards[index] = -1
            self.finishCards.append(index)
            uiposition.append(index)
        self.cancelAllChosen()
        return uiposition
    
    def getNumberOfCardsOndesk(self):
        count = 0
        for card in self.deskCards:
           if card != -1:
               count += 1
        return count
    
