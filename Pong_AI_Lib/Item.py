class Item:
    def __init__(self):
        self.__xpos = 50
        self.__ypos = 50
        self.__color = (255, 255, 255)
        self.__speed = 3

    def draw(self, context):
        pass

    def set_xpos(self, xpos):
        self.__xpos = xpos

    def get_xpos(self):
        return self.__xpos

    def set_ypos(self, ypos):
        self.__ypos = ypos

    def get_ypos(self):
        return self.__ypos

    def set_speed(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

