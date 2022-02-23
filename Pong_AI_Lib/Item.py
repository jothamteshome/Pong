class Item:
    def __init__(self):
        # Store the position of the item
        self.__xpos = 50
        self.__ypos = 50

        # Store the color of the item
        self.__color = (255, 255, 255)

        # Store the speeds of the item
        self.__y_speed = 3
        self.__x_speed = 0

    def draw(self, context):
        pass

    def update(self):
        pass

    def set_xpos(self, xpos):
        self.__xpos = xpos

    def get_xpos(self):
        return self.__xpos

    def set_ypos(self, ypos):
        self.__ypos = ypos

    def get_ypos(self):
        return self.__ypos

    def set_y_speed(self, y_speed):
        self.__y_speed = y_speed

    def get_y_speed(self):
        return self.__y_speed

    def set_x_speed(self, x_speed):
        self.__x_speed = x_speed

    def get_x_speed(self):
        return self.__x_speed

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color


