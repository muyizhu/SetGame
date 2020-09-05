import tkinter as tk
import Constants as consts

class UserInterface:
    def __init__(self,deck,validator,controller):
        self.validator = validator
        self.controller = controller
        self.deck = deck
        self.window = tk.Tk()
        self.deskCardImages = []
        self.buttonList = []

    #public function, used to start the gameUI
    def drawMain(self):
        self.initWindow()
        self.setMenuBar(self.window)
        topFrame,bodyFrame,bottomFrame = self.initWindowFrame(self.window)
        topFrame.pack()
        bodyFrame.pack()
        bottomFrame.pack()
        self.setGameBody(bodyFrame)
        self.setControlButton(bottomFrame)
        self.window.mainloop()
    
    #initialize rootwindow basic attribute, length height and titile
    def initWindow(self):
        length = consts.WINDOW_WIDTH
        height = consts.WINDOW_HEIGHT
        self.window.title(consts.GAME_NAME)
        self.window.geometry("%dx%d" % (length,height))

    #set up window outline(divide it into frames)
    def initWindowFrame(self,window):
        return [tk.Frame(window),tk.Frame(window),tk.Frame(window)]

    #Set up----------------------------------Menubar start from here----------------------------------------------
    def setMenuBar(self,window):
        menubar = tk.Menu(window)
        self.setOptionMenu(menubar)
        self.setDifficultyMenu(menubar)
        window.config(menu=menubar)

    def setOptionMenu(self,menubar):
        optionMenu = tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label='Option',menu=optionMenu)
        optionMenu.add_command(label="Window size +",command=self.controller.enlargeWindow(self.window))
        optionMenu.add_command(label="Window size -",command=self.controller.reduceWindow(self.window))
        optionMenu.add_separator()
        optionMenu.add_command(label='Exit',command=self.window.quit)
    
    def setDifficultyMenu(self,menubar):
        difficultyMenu = tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label='Difficulty',menu=difficultyMenu)
        difficultyMenu.add_command(label="easy",command=self.controller.changeGameDifficulty(consts.EASY,self.deck))
        difficultyMenu.add_command(label="middle",command=self.controller.changeGameDifficulty(consts.MIDDLE,self.deck))
        difficultyMenu.add_command(label="hard",command=self.controller.changeGameDifficulty(consts.HARD,self.deck))
    #-------------------------------------MenuBar End here-----------------------------------------------------


    #-------------------------------------bodyFrame start here------------------------------------------------
    def setGameBody(self,bodyFrame):  
        self.controller.loadCardsImage(self.deck.deskCards,self.deskCardImages)
        self.showDesk(bodyFrame)
        # canvas.create_image(0,0, anchor='nw', image=img)
        # canvas.pack()

    def showDesk(self,bodyFrame):
        index = 0
        buttonList = []
        for i in range(0,consts.DESK_CARDS_ONECOL):
            rowList = []
            for j in range(0,consts.DESK_CARDS_ONEROW):
                button = tk.Button(bodyFrame,
                                image = self.deskCardImages[index],
                                command = lambda: self.controller.chooseCard(i,j,self.deck,button) )
                button.grid(row = i,column=j)
                rowList.append(button)
                index+=1
            buttonList.append(rowList)

    #-------------------------------------bodyFrame End here--------------------------------------------------


    def setControlButton(self,frameBottom):
        pass
    #set up submitted button

    #set up memu