import tkinter as tk
import Constants as consts
import GameClock

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
        self.setTopFrame(topFrame)
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

    #----------------------------------Set up TopFrame here---------------------------------------------------  
    def setTopFrame(self,topFrame):
        self.setClock(topFrame)

    def setClock(self,topFrame):
        GameClock.Clock(self.window,topFrame)
        

    #-------------------------------------bodyFrame start here------------------------------------------------
    def setGameBody(self,bodyFrame):  
        self.controller.loadCardsImage(self.deck.deskCards,self.deskCardImages)
        self.showDesk(bodyFrame)
        # canvas.create_image(0,0, anchor='nw', image=img)
        # canvas.pack()

    
    def showDesk(self,bodyFrame):
        index=0
        for i in range(0,consts.DESK_CARDS_ONECOL):
            for j in range(0,consts.DESK_CARDS_ONEROW):
                self.makeButton(i,j,bodyFrame)
                index+=1

    def clickCardLambda(self,i,j,deck,bodyFrame):
        return lambda: self.controller.clickCard(i,j,deck,self,bodyFrame)

    def makeButton(self,row,col,bodyFrame,bd=None,relief='raised',callback = clickCardLambda,thickness=consts.NORMAL_THICKNESS):
        key = row*consts.DESK_CARDS_ONEROW+col
        button = tk.Button(bodyFrame,
                        width = consts.BUTTON_WIDTH,
                        height = consts.BUTTON_HEIGHT,
                        image = self.deskCardImages[key],
                        relief = relief,
                        command = callback(self,row,col,self.deck,bodyFrame),
                        borderwidth=bd)
        button.config(highlightthickness=thickness)
        button.grid(row = row,column=col)
    #-------------------------------------bodyFrame End here--------------------------------------------------
    def setControlButton(self,bottomFrame):
        button = tk.Button(bottomFrame,
                        # width = consts.BUTTON_WIDTH,
                        # height = consts.BUTTON_HEIGHT,
                        text = "submit",
                        justify="center",
                        pady=0,
                        anchor = 's',
                        #padx=100, background="blue",
                        command = self.validator.validateLambda(self.deck),
                        )
        button.grid(row = 6, column = 3)
        
    #set up submitted button

    #set up memu