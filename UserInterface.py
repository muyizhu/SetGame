import Tkinter as tk
import Constants as consts

class UserInterface:
    def __init__(self,deck,validator,controller):
        self.validator = validator
        self.controller = controller
        self.deck = deck

    #initialize start menu (graphical interface for user)
    def drawStartMenu(self):
        pass