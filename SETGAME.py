import Deck
import Platform
import UI
import CoreSystem


class SETGAME:
    def __init__(self):
        self.deck = Deck.Deck()
        self.platfrom = Platform.Platfrom(self.deck)
        self.validator = CoreSystem.GameValidator()
        self.GameController = CoreSystem.GameController()
        self.ui = UI.UserInterface(self.platfrom, self.validator, self.GameController)

    def start(self):
        self.platfrom.readForGame()
        self.ui.drawMain()


if __name__ == "__main__":
    setGame = SETGAME()
    setGame.start()
