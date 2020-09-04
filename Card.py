class Card:

    def __init__(self, Color, Shape, Fill, Number,url):
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
        return (self.color, self.fill,self.shape,self.number)
    def getUrl(self):
        return self.url
