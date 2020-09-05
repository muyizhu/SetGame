class Card:

    def __init__(self, ID, Color, Shape, Fill, Number,url):
        self.beChosen = False
        self.id = ID
        self.color = Color
        self.fill = Fill
        self.shape = Shape
        self.number = Number
        self.url = url

    #create the methods for getting the properties of the card
    def getColor(self):
        return self.color

    def getFill(self):
        return self.fill

    def getShape(self):
        return self.shape

    def getNumber(self):
        return self.number

    def getAll(self):
        return (self.id,self.color, self.fill,self.shape,self.number,self.url)

    def getUrl(self):
        return self.url

    def getID(self):
        return self.id

    def chooseCard(self):
        self.beChosen = True

    def cancelChooseCard(self):
        self.beChosen = False