class Pixel:
    def __init__(self, x_value, y_value):
        self.x_value = x_value
        self.y_value = y_value
        self.color = "RED"
        self.colored = False

    def getX(self):
        return self.x_value

    def getY(self):
        return self.y_value

    def moveX(self):
        self.x_value += 20
        return self.x_value

    def moveY(self):
        self.y_value += 20
        return self.y_value
