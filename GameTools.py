import Constants as consts

class GameValidator:
    def _init_(self):
        pass

    def validateSet(self,chosenCards):
        pass

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

    #Controll method for UserInterface
    def resize(self,pil_image,ratio): 
        from PIL import Image 
        w,h =  pil_image.size
        width = int(w*ratio)  
        height = int(h*ratio)  
        return pil_image.resize((width, height),Image.ANTIALIAS) 
    
    def loadCardsImage(self,cards,container):
        from PIL import Image, ImageTk 
        for card in cards:
            pilImage = Image.open(card.getUrl())
            resize = self.resize(pilImage,consts.RESIZE_RATIO)
            img = ImageTk.PhotoImage(resize)
            container.append(img)
    
    #Event Listener 
    def chooseCard(self,i,j,deck,button):
        print("i",i)
        print("j",j)
        print(button)
        key = i*consts.DESK_CARDS_ONEROW+j
        deck.chooseCardFromDesk(key)
        #print(deck.chosenCards)