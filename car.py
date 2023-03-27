"""A module that contains the Car class."""

class Car:
    """A class that represents a car."""
    def __init__(self, make, model, year, color, transmission, engine, price):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__color = color
        self.__transmission = transmission
        self.__engine = engine
        self.__price = price

    def get_make(self):
        """Returns the make of the car."""
        return self.__make

    def get_model(self):
        """Returns the model of the car."""
        return self.__model

    def get_year(self):
        """Returns the year of the car."""
        return self.__year

    def get_color(self):
        """Returns the color of the car."""
        return self.__color

    def get_transmission(self):
        """Returns the transmission of the car."""
        return self.__transmission

    def get_engine(self):
        """Returns the engine of the car."""
        return self.__engine

    def get_price(self):
        """Returns the price of the car."""
        return self.__price

    def set_make(self, make):
        """Sets the make of the car."""
        self.__make = make

    def set_model(self, model):
        """Sets the model of the car."""
        self.__model = model

    def set_year(self, year):
        """Sets the year of the car."""
        self.__year = year

    def set_color(self, color):
        """Sets the color of the car."""
        self.__color = color

    def set_transmission(self, transmission):
        """Sets the transmission of the car."""
        self.__transmission = transmission

    def set_engine(self, engine):
        """Sets the engine of the car."""
        self.__engine = engine

    def set_price(self, price):
        """Sets the price of the car."""
        self.__price = price
