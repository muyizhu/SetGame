import Constants as consts
from PIL import Image, ImageTk 
import tkinter.messagebox
import Music
class GameValidator:
    def _init_(self):
        pass

    def validateSet(self,chosenCards):
        # Colors = set([str(card.getColor()) for card in chosenCards])
        # Fills = set([card.getFill() for card in chosenCards])
        # Shapes = set([card.getShape() for card in chosenCards])
        # Numbers = set([card.getNumber() for card in chosenCards])
        # if (len(Colors) == 3 or len(Colors) == 1) and (len(Fills) == 3 or len(Fills) == 1) and (len(Shapes) == 3 or len(Shapes) == 1) and ((len(Numbers) == 3 or len(Numbers) == 1)):
        #     return True
        # else:
        #     return False
        return True
    
    def canGameContinue(self,deck):
        import copy
        if deck.getNumberOfCardsOndesk() == consts.DESK_CARDS_CAPACITY:
            for i in range(0, consts.DESK_CARDS_CAPACITY - 2):
                setDraft = [-1, -1, -1]
                setDraft[0] = deck.deskCards[i]
                for j in range(i + 1,consts.DESK_CARDS_CAPACITY - 1 ):
                    setDraft[1] = deck.deskCards[j]
                    for k in range(j + 1, consts.DESK_CARDS_CAPACITY):
                        setDraft[2] = deck.deskCards[k]
                        if self.validateSet(setDraft):
                            return True
            return False
        elif (deck.getNumberOfCardsOndesk() == 0) and (len(deck.cardPool) == 0):
                return False
        else:
            if len(deck.cardPool) == 0:
                if deck.getNumberOfCardsOndesk() == 0:
                    return False
                else:
                    deskCardsDraft = copy.deepcopy(deck.deskCards)
                    for i in range(0, deskCardsDraft.count(-1)):
                        deskCardsDraft.remove(-1)
                    for i in range(0, len(deskCardsDraft) - 2):
                        setDraft = [-1, -1, -1]
                        setDraft[0] = deskCardsDraft[i]
                        for j in range(i + 1, len(deskCardsDraft) - 1):
                            setDraft[1] = deskCardsDraft[j]
                            for k in range(j + 1, len(deskCardsDraft)):
                                setDraft[2] = deskCardsDraft[k]
                                print(setDraft)
                                if self.validateSet(setDraft):
                                    return True
                    return False
            else:
                return True
        

    def validateView(self,deck,ui):
        if(self.validateSet(deck.chosenCards)):
            positions = deck.deleteChosenCardsFromDesk()
            for p in positions:
                control = GameController()
                img = control.get_resize_image_from_url(consts.EMPTY_IMAGE_PATH)
                ui.deskCardImages[p] = -1
                ui.makeLabel(p,ui.bodyFrame,img,text="empty")
            self.updateMessage(deck,ui)
            if (not self.canGameContinue(deck)):
                import time
                tkinter.messagebox.askokcancel("Game report", "Exllent!! you find all set in "+str(time.time()-ui.clock.time_start)+" seconds")
        else:
            tkinter.messagebox.askokcancel("game mention", "chosen set is not right!!")

    def validateLambda(self,deck,ui):
        return lambda: self.validateView(deck,ui)
    
    def getCurrentGameLog(self,deck):
        return "you have finished "+str(len(deck.finishCards))+"cards. "+str(len(deck.cardDict)-len(deck.finishCards))+" cards left."
    
    def updateMessage(self,deck,ui):
        import tkinter
        string = self.getCurrentGameLog(deck)
        w = tkinter.Label(ui.bottomFrame, text=string)
        w.grid(row=consts.MESSAGE_ROW,column=consts.MESSAGE_COL)

class GameController:
    #Control methods for options in menubar
    def _init_(self):
        pass

    def enlargeWindow(self,window):
        pass

    def reduceWindow(self,window):
        pass

    def changeGameDifficulty(self,newDiff,deck):
        pass

    #GUI SHOWING METHOD
    def onClosingLambda(self,window,deck,clock):
        return lambda: self.on_closing(window,deck,clock)

    def on_closing(self,window,deck,clock):
        import time
        if tkinter.messagebox.askokcancel("Quit", "are you really sure you want to give up?"):
            tkinter.messagebox.askokcancel("Game report", "you finished "+str(len(deck.finishCards))+" cards in "+str(time.time()-clock.time_start)+" seconds")
            window.destroy()
        
    #Controll method for UserInterface
    def resize(self,pil_image,ratio):  
        w,h =  pil_image.size
        width = int(w*ratio)  
        height = int(h*ratio)  
        return pil_image.resize((width, height),Image.ANTIALIAS) 
    
    def get_resize_image_from_url(self,url):
        pilImage = Image.open(url)
        resize = self.resize(pilImage,consts.RESIZE_RATIO)
        img = ImageTk.PhotoImage(resize)
        return img
    
    def loadCardsImage(self,cards,container):
        for i in range(0,len(cards)):
            card = cards[i]
            img = self.resizeCardToNormal(card)
            if i == len(container):
                container.append(img)
            else:
                container.insert(i,img)
            

    def resizeCardToChosen(self,card):
        if card == -1:
            return None
        pilImage = Image.open(card.getUrl())
        resize = self.resize(pilImage,consts.CHOSEN_RESIZE_RATIO)
        img = ImageTk.PhotoImage(resize)
        return img

    def resizeCardToNormal(self,card):
        if card == -1: 
            return None
        pilImage = Image.open(card.getUrl())
        resize = self.resize(pilImage,consts.RESIZE_RATIO)
        img = ImageTk.PhotoImage(resize)
        return img

    #Event Listener 
    def clickCard(self,i,j,deck,ui,bodyFrame):
        key = i*consts.DESK_CARDS_ONEROW+j
        card = deck.deskCards[key]
        relief = None
        needToBack = -1
        thick = consts.NORMAL_THICKNESS
        if card not in deck.chosenCards:
            Music.clickSound.play()
            needToBack = deck.chooseCardFromDesk(key)
            relief = "sunken"
            thick = consts.CHOSEN_THICKNESS
        else:
            deck.cancelChosen(card)
            relief = "raised"
        if needToBack !=-1:
            self.changeChosenCardImage(deck,ui.deskCardImages,needToBack)
            row = needToBack//consts.DESK_CARDS_ONEROW
            col = needToBack%consts.DESK_CARDS_ONEROW
            ui.makeButton(row,col,bodyFrame,relief = 'raised',thickness=consts.NORMAL_THICKNESS)
        self.changeChosenCardImage(deck,ui.deskCardImages,key)
        ui.makeButton(i,j,bodyFrame,relief = relief,thickness=thick)

    def changeChosenCardImage(self,deck,deskCardImages,index):
        card = deck.deskCards[index]
        if card in deck.chosenCards:
            deskCardImages[index] = self.resizeCardToChosen(card)
        else:
            deskCardImages[index] = self.resizeCardToNormal(card)
    
    def fillDeskLambda(self,deck,ui):
        return lambda:self.fillDesk(deck,ui)

    def fillDesk(self,deck,ui):
        filled = deck.fillDesk()
        self.loadCardsImage(ui.deck.deskCards,ui.deskCardImages)
        ui.showCards(filled,ui.bodyFrame)
    
    def getCurrentGameLog(self,deck):
        return "you have finished "+str(len(deck.finishCards))+"cards. "+str(len(deck.cardDict)-len(deck.finishCards))+" cards left."
    
    def restartLambda(self,deck,ui):
        return lambda: self.restart(deck,ui)
    
    def restart(self,deck,ui):
        deck.readyForGame()
        ui.setTopFrame(ui.topFrame)
        ui.setGameBody(ui.bodyFrame)
        ui.setControlButton(ui.bottomFrame)
    
    def replaceAllCardsLambda(self,deck,ui):
        return lambda: self.replaceAllCards(deck,ui)

    def replaceAllCards(self,deck,ui):
        Music.replaceAll.play()
        keys = deck.findKeysOfDeskCards()
        replace = deck.changeDeskCards(keys)
        # ui.deskCardImages=[]
        # deck.clearDesk()
        if len(replace)!=0:
            self.loadCardsImage(ui.deck.deskCards,ui.deskCardImages)
            ui.showCards(replace,ui.bodyFrame)
    
    def replaceCardLambda(self,pui):
        return  lambda event,p=pui: self.replaceCard(event,p)
    
    def replaceCard(self,event, positionandui):
        Music.replaceSound.play()
        ui = positionandui[1]
        deck = ui.deck
        if len(ui.deck.cardPool)==0:
            return
        key = positionandui[0]
        temp = deck.deskCards[key]
        deck.cancelChosen(temp)
        deck.shuffle()
        card = deck.cardPool.pop()
        deck.deskCards[key] = card
        deck.cardPool.append(temp)
        ui.deskCardImages[key] = self.get_resize_image_from_url(card.url)
        filled = [key]
        ui.showCards(filled,ui.bodyFrame)
        
    
    
        