import Constants as consts
from PIL import Image, ImageTk
import tkinter.messagebox
import copy


class GameValidator:

    def _init_(self):
        pass

    def validateSet(self, chosenCards):
        # if len(chosenCards) == 3:
        #     return True
        # else:
        #     return False
         Colors = set([str(card.getColor()) for card in chosenCards])
         Fills = set([card.getFill() for card in chosenCards])
         Shapes = set([card.getShape() for card in chosenCards])
         Numbers = set([card.getNumber() for card in chosenCards])
         if (len(Colors) == 3 or len(Colors) == 1) and (len(Fills) == 3 or len(Fills) == 1) and (
                 len(Shapes) == 3 or len(Shapes) == 1) and ((len(Numbers) == 3 or len(Numbers) == 1)) and len(chosenCards) == 3:
             return True
         else:
             return False

    def canGameContinue(self, platform):
        if platform.getNumberOfCardsOnDesk() == consts.DESK_CARDS_CAPACITY:
            for i in range(0, consts.DESK_CARDS_CAPACITY - 2):
                setDraft = [-1, -1, -1]
                setDraft[0] = platform.cardsOnDesk[i]
                for j in range(i + 1, consts.DESK_CARDS_CAPACITY - 1):
                    setDraft[1] = platform.cardsOnDesk[j]
                    for k in range(j + 1, consts.DESK_CARDS_CAPACITY):
                        setDraft[2] = platform.cardsOnDesk[k]
                        if self.validateSet(setDraft):
                            return True
            return False
        elif (platform.getNumberOfCardsOnDesk() == 0) and (len(platform.cardPool) == 0):
            return False
        else:
            if len(platform.cardPool) == 0:
                if platform.getNumberOfCardsOnDesk() == 0:
                    return False
                else:
                    deskCardsDraft = copy.deepcopy(platform.cardsOnDesk)
                    for i in range(0, deskCardsDraft.count(-1)):
                        deskCardsDraft.remove(-1)
                    for i in range(0, len(deskCardsDraft) - 2):
                        setDraft = [-1, -1, -1]
                        setDraft[0] = deskCardsDraft[i]
                        for j in range(i + 1, len(deskCardsDraft) - 1):
                            setDraft[1] = deskCardsDraft[j]
                            for k in range(j + 1, len(deskCardsDraft)):
                                setDraft[2] = deskCardsDraft[k]
                                if self.validateSet(setDraft):
                                    return True
                    return False
            else:
                return True

    def validateView(self, platform, ui):
        if (self.validateSet(platform.chosenCards)):
            positions = platform.makeSet()
            for p in positions:
                control = GameController()
                if (len(platform.cardPool) != 0) and len(platform.cardPool) >= (consts.DESK_CARDS_CAPACITY - platform.getNumberOfCardsOnDesk()):
                    img = control.resizeCardToNormal(platform.cardPool[0])
                    ui.makeLabel(p, ui.bodyFrame, img, text="empty")
                elif (len(platform.cardPool) != 0) and len(platform.cardPool) < (consts.DESK_CARDS_CAPACITY - platform.getNumberOfCardsOnDesk()):
                    img = control.resizeCardToNormal(platform.cardPool[0])
                    ui.makeLabel(p, ui.bodyFrame, img, text="empty")
                elif len(platform.cardPool) == 0:
                    img = control.resizeCardToNormal(-1)
                    ui.makeLabel(p, ui.bodyFrame, img, text="empty")
                else:
                    img = control.resizeCardToNormal(-1)
                    ui.makeLabel(p, ui.bodyFrame, img, text="empty")
            self.updateMessage(platform, ui)
            if (not self.canGameContinue(platform)):
                import time
                tkinter.messagebox.askokcancel("Game report", "Exllent!! you find all set in " + str(
                    time.time() - ui.clock.time_start) + " seconds")
        else:
            tkinter.messagebox.askokcancel("game mention", "chosen set is not right!!")

    def validateLambda(self, platform, ui):
        return lambda: self.validateView(platform, ui)

    def getCurrentGameLog(self, platform):
        return "you have finished " + str(len(platform.historicalCards)) + "cards. " + str(
            platform.totalCardsNumber - len(platform.historicalCards)) + " cards left." + str(len(platform.cardPool)) + " unfilled cards."

    def updateMessage(self, platform, ui):
        import tkinter
        string = self.getCurrentGameLog(platform)
        w = tkinter.Label(ui.bottomFrame, text=string)
        w.grid(row=6, column=4)


class GameController:
    # Control methods for options in menubar
    def _init_(self):
        pass

    def enlargeWindow(self,window):
        pass

    def reduceWindow(self,window):
        pass

    def changeGameDifficulty(self,newDiff,deck):
        pass

    # GUI SHOWING METHOD
    def onClosingLambda(self, window, platform, clock):
        return lambda: self.on_closing(window, platform, clock)

    def on_closing(self, window, platform, clock):
        import time
        if tkinter.messagebox.askokcancel("Quit", "are you really sure you want to give up?"):
            tkinter.messagebox.askokcancel("Game report",
                                           "you finished " + str(len(platform.historicalCards)) + " cards in " + str(
                                               time.time() - clock.time_start) + " seconds")
            window.destroy()

    # Controll method for UserInterface
    def resize(self, pil_image, ratio):
        w, h = pil_image.size
        width = int(w * ratio)
        height = int(h * ratio)
        return pil_image.resize((width, height), Image.ANTIALIAS)

    def loadCardsImage(self, cards, container):
        for card in cards:
            img = self.resizeCardToNormal(card)
            container.append(img)

    def resizeCardToChosen(self, card):
        pilImage = Image.open(card.getImage())
        resize = self.resize(pilImage, consts.CHOSEN_RESIZE_RATIO)
        img = ImageTk.PhotoImage(resize)
        return img

    def resizeCardToNormal(self, card):
        if card != -1:
            pilImage = Image.open(card.getImage())
            resize = self.resize(pilImage, consts.RESIZE_RATIO)
            img = ImageTk.PhotoImage(resize)
            return img
        else:
            pilImage = Image.open(consts.EMPTY_IMAGE)
            resize = self.resize(pilImage, consts.RESIZE_RATIO)
            img = ImageTk.PhotoImage(resize)
            return img

    # Event Listener
    def clickCard(self, i, j, platform, ui, bodyFrame):
        key = i * consts.DESK_CARDS_ONEROW + j
        card = platform.cardsOnDesk[key]
        relief = None
        needToBack = -1
        thick = consts.NORMAL_THICKNESS
        if card not in platform.chosenCards:
            needToBack = platform.chooseCard(key)
            relief = "ridge"
            thick = consts.CHOSEN_THICKNESS
        else:
            platform.cancelChosen(card)
            relief = "raised"
        if needToBack != -1:
            self.changeChosenCardImage(platform, ui.deskCardImages, needToBack)
            row = needToBack // consts.DESK_CARDS_ONEROW
            col = needToBack % consts.DESK_CARDS_ONEROW
            ui.makeButton(row, col, bodyFrame, relief='raised', thickness=consts.NORMAL_THICKNESS)
        if(card != -1):
            self.changeChosenCardImage(platform, ui.deskCardImages, key)
            ui.makeButton(i, j, bodyFrame, relief=relief, thickness=thick)
        else:
            img = self.resizeCardToNormal(-1)
            ui.makeLabel(key, ui.bodyFrame, img, text="empty")


    def changeChosenCardImage(self, platform, deskCardImages, index):
        card = platform.cardsOnDesk[index]
        if card in platform.chosenCards:
            deskCardImages[index] = self.resizeCardToChosen(card)
        else:
            deskCardImages[index] = self.resizeCardToNormal(card)

    def fillDeskLambda(self, platform, ui):
        return lambda: self.fillDesk(platform, ui)

    def fillDesk(self, platform, ui):
        platform.fillCardsOnDesk()
        ui.setGameBody(ui.bodyFrame)
        gamevalidator = GameValidator()
        if (not gamevalidator.canGameContinue(platform)):
            import time
            tkinter.messagebox.askokcancel("Game report", "Exllent!! you find all set in " + str(
                time.time() - ui.clock.time_start) + " seconds")

    def getCurrentGameLog(self, platform):
        return "you have finished " + str(len(platform.historicalCards)) + "cards. " + str(
            platform.totalCardsNumber - len(platform.historicalCards)) + " cards left." + str(len(platform.cardPool)) + " unfilled cards."

    def restartLambda(self, platform, ui):
        return lambda: self.restart(platform, ui)

    def restart(self, platform, ui):
        platform.readForGame()
        ui.setTopFrame(ui.topFrame)
        ui.setGameBody(ui.bodyFrame)
        ui.setControlButton(ui.bottomFrame)