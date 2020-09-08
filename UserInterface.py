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
        #self.canvas = None
        self.topFrame,self.bodyFrame,self.bottomFrame = self.initWindowFrame(self.window)
        self.clock = None

    #public function, used to start the gameUI
    def drawMain(self):
        self.initWindow()
        self.setMenuBar(self.window)
        self.topFrame.pack()
        self.bodyFrame.pack()
        self.bottomFrame.pack()
        self.setTopFrame(self.topFrame)
        self.setGameBody(self.bodyFrame)
        self.setControlButton(self.bottomFrame)
        self.window.mainloop()


    
    #initialize rootwindow basic attribute, length height and titile
    #photo = None
    def initWindow(self):    
        from PIL import ImageTk, Image
        length = consts.WINDOW_WIDTH
        height = consts.WINDOW_HEIGHT
        # global photo
        self.window.title(consts.GAME_NAME)
        self.window.geometry("%dx%d" % (length,height))

        # canvas = tk.Canvas(self.window, width=length,height=height,bd=0, highlightthickness=0)
        # imgpath = consts.BACKGROUND_IMAGE_PATH
        # img = Image.open(imgpath)
        # img = self.controller.resize(img,2)
        # photo = ImageTk.PhotoImage(img)
 
        # canvas.create_image(400, 200, image=photo)
        # canvas.pack()
        # return canvas
        


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
        self.setRestartButton(topFrame)

    def setClock(self,topFrame):
        self.clock = GameClock.Clock(self.window,topFrame)
        self.window.protocol("WM_DELETE_WINDOW", self.controller.onClosingLambda(self.window,self.deck,self.clock) )
    
    def setRestartButton(self,topFrame):
        restart = tk.Button(topFrame,
                        # width = consts.BUTTON_WIDTH,
                        # height = consts.BUTTON_HEIGHT,
                        text = "restart game",
                        justify="center",
                        pady=0,
                        anchor = 's',
                        #padx=100, background="blue",
                        command = self.controller.restartLambda(self.deck,self)
                        )
        restart.grid(row = consts.RESTART_ROW, column=consts.RESTART_COL)

    #-------------------------------------bodyFrame start here------------------------------------------------
    def setGameBody(self,bodyFrame): 
        self.deskCardImages = []
        self.controller.loadCardsImage(self.deck.deskCards,self.deskCardImages)
        self.showDesk(bodyFrame)
        # canvas.create_image(0,0, anchor='nw', image=img)
        # canvas.pack()
    
    def showCards(self,filled,frame):
        for key in filled:
            row = key//consts.DESK_CARDS_ONEROW
            col = key%consts.DESK_CARDS_ONEROW
            self.makeButton(row,col,frame)
    
    def showDesk(self,bodyFrame):
        index=0
        for i in range(0,consts.DESK_CARDS_ONECOL):
            for j in range(0,consts.DESK_CARDS_ONEROW):
                self.makeButton(i,j,bodyFrame)
                index+=1

    def clickCardLambda(self,i,j,deck,bodyFrame):
        return lambda: self.controller.clickCard(i,j,deck,self,bodyFrame)
    
    def makeLabel(self,p,bodyFrame,image,bg='grey',text='empty',fg='white',compound='center'):
        row = p//consts.DESK_CARDS_ONEROW
        col = p%consts.DESK_CARDS_ONEROW
        label = tk.Label(bodyFrame,width = consts.BUTTON_WIDTH,
                        height = consts.BUTTON_HEIGHT,padx=0,pady=0,image =image,relief="ridge",)
        label.config(bg=bg,text=text,fg=fg, compound = compound)
        label.grid(row=row,column=col)

    def makeButton(self,row,col,bodyFrame,bd=None,relief='raised',callback = clickCardLambda,thickness=consts.NORMAL_THICKNESS):
        key = row*consts.DESK_CARDS_ONEROW+col
        if self.deskCardImages[key] == None:
            img = self.controller.get_resize_image_from_url(consts.EMPTY_IMAGE_PATH)
            self.makeLabel(key,bodyFrame,img,text="empty")
            return
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
        filldesk = tk.Button(bottomFrame,
                        # width = consts.BUTTON_WIDTH,
                        # height = consts.BUTTON_HEIGHT,
                        text = "fill desk",
                        justify="left",
                        pady=0,
                        anchor = 's',
                        #padx=100, background="blue",
                        command = self.controller.fillDeskLambda(self.deck,self),
                        )
        filldesk.grid(row = 6, column = 2)

        submit = tk.Button(bottomFrame,
                        # width = consts.BUTTON_WIDTH,
                        # height = consts.BUTTON_HEIGHT,
                        text = "submit",
                        justify="center",
                        pady=0,
                        anchor = 's',
                        #padx=100, background="blue",
                        command = self.validator.validateLambda(self.deck,self),
                        )
        submit.grid(row = 6, column = 3)

        string = self.controller.getCurrentGameLog(self.deck)
        w = tk.Label(bottomFrame, text=string)
        w.grid(row=6,column=4)


        # p = 6*consts.DESK_CARDS_ONEROW+5
        # pilImage = Image.open(self.deck.cardDict[0].getUrl())
        # img = self.controller.resize(pilImage,1)
        # self.makeLabel(p,bottomFrame,image=img,text=string)
        
    #set up submitted button

    #set up memu