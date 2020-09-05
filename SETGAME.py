import Deck
import Card
import UserInterface as UI
import GameTools
class SETGAME:
    def __init__(self):
        self.deck = Deck.Deck()
        self.validator = GameTools.GameValidator()
        self.GameController = GameTools.GameController()
        self.ui = UI.UserInterface(self.deck,self.validator,self.GameController)
    
    def start(self):
        self.ui.drawMain()

if __name__=="__main__":
    setGame = SETGAME()
    setGame.start()