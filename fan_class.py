class Fan:
    slow=1
    medium=2
    fast=3

    def __init__(self,speed=slow, radius=5, color="blue", on=False):
        self.__speed=speed
        self.__radius=radius
        self.__color=color
        self.__on=on
        
    def set_speed(self,speed):
        self.__speed=speed

    def set_radius(self,radius):
        self.__radius=radius