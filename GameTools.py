import Constants as consts
from PIL import Image, ImageTk 
import tkinter.messagebox
class GameValidator:
    def _init_(self):
        pass

    def validateSet(self,chosenCards):
        return True

    def validateView(self,deck,ui):
        if(self.validateSet(deck.chosenCards)):
            positions = deck.deleteChosenCardsFromDesk()
            for p in positions:
                control = GameController()
                img = control.resizeCardToNormal(deck.cardDict[0])
                ui.makeLabel(p,ui.bodyFrame,img,text="empty")
        else:
            tkinter.messagebox.askokcancel("game mention", "chosen set is not right!!")

    def validateLambda(self,deck,ui):
        return lambda: self.validateView(deck,ui)
    

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
    
    def loadCardsImage(self,cards,container):
        for card in cards:
            img = self.resizeCardToNormal(card)
            container.append(img)

    def resizeCardToChosen(self,card):
        pilImage = Image.open(card.getUrl())
        resize = self.resize(pilImage,consts.CHOSEN_RESIZE_RATIO)
        img = ImageTk.PhotoImage(resize)
        return img

    def resizeCardToNormal(self,card):
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
            needToBack = deck.chooseCardFromDesk(key)
            relief = "ridge"
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
    
    
        