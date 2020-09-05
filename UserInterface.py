import tkinter as tk
import Constants as consts

class UserInterface:
    def __init__(self,deck,validator,controller):
        self.validator = validator
        self.controller = controller
        self.deck = deck
        self.window = tk.Tk()
    #initialize start menu (graphical interface for user)
    def initWindow(self):
        length = consts.WINDOW_LENGTH
        height = consts.WINDOW_HEIGHT
        self.window.title(consts.GAME_NAME)
        self.window.geometry("%dx%d" % (length,height))
    def drawStartMenu(self):
        self.initWindow()
        self.window.mainloop()