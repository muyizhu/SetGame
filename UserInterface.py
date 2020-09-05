import tkinter as tk
import Constants as consts

class UserInterface:
    def __init__(self,deck,validator,controller):
        self.validator = validator
        self.controller = controller
        self.deck = deck
        self.window = tk.Tk()

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
        bodyWidth = consts.DESK_WIDTH
        bodyHeight = consts.DESK_HEIGHT
        canvas = tk.Canvas(bodyFrame,height = bodyHeight,width=bodyWidth)
        cardsOneRow = consts.DESK_CARDS_ONEROW
        cardsOneCol = consts.DESK_CARDS_ONECOL
        deskCards = self.deck.deskCards
        index = 0
        for i in range(cardsOneCol):
            for j in range(cardsOneRow):
                card = deskCards[index]
                image = tk.PhotoImage(file=card.getUrl())
                index = index+1
                tk.Label(bodyFrame, image=image).grid(row=i, column=j)#, padx=10, pady=10, ipadx=5, ipady=5

    #-------------------------------------bodyFrame End here--------------------------------------------------


    def setControlButton(self,frameBottom):
        pass
    #set up submitted button

    #set up memu