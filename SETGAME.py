import Deck
import Card
import UserInterface as UI
import GameTools
class SETGAME:
    def __init__(self):
        self.deck = Deck.Deck()
        self.validator = GameTools.GameValidator()
        self.UIController = GameTools.UIController()
        self.ui = UI.UserInterface(self.deck,self.validator,self.UIController)
    
    def start(self):
        self.ui.drawStartMenu()

if __name__=="__main__":
    setGame = SETGAME()
    setGame.start()