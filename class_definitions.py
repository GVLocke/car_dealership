"""A module that contains the main class definitions."""
import shortuuid

class Vehicle:
    """A class that represents a Vehicle."""
    # dealership inventory
    inventory = []

    def __init__(self, vin, make, model, year, color, transmission, engine, price):
        self.__vin = vin
        self.__make = make
        self.__model = model
        self.__year = year
        self.__color = color
        self.__transmission = transmission
        self.__engine = engine
        self.__price = price
        # add the car to the inventory
        Vehicle.inventory.append(self)
    
    def get_vin(self):
        """Returns the VIN of the car."""
        return self.__vin

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
    
    def set_vin(self, vin):
        """Sets the VIN of the car."""
        self.__vin = vin

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

    def print_details(self):
        """Prints the details of the car."""
        print(f"{self.__year} {self.__make} {self.__model}".center(50, "-"))
        print("VIN: " + self.__vin)
        print("Make: " + self.__make)
        print("Model: " + self.__model)
        print("Year: " + str(self.__year))
        print("Color: " + self.__color)
        print("Transmission: " + self.__transmission)
        print("Engine: " + self.__engine)
        print("Price: $" + str(self.__price))

    @staticmethod
    def get_inventory():
        """Returns the dealership inventory."""
        return Vehicle.inventory
    
    @staticmethod
    def print_inventory():
        """Prints the dealership inventory."""
        print("Dealership Inventory".center(55, "-"))
        print()
        for vehicle in Vehicle.inventory:
            vehicle.print_details()

class Purchase:
    """A class that represents a purchase of a car."""
    # purchase history
    purchase_history = []
    def __init__(self, vin, customer_id, price, date):
        """Initializes the purchase object."""
        # check if the inventory is empty
        if len(Vehicle.inventory) == 0:
            raise ValueError("Inventory is empty.")
        for vehicle in Vehicle.inventory:
            if vehicle.get_vin() == vin:
                self.__vehicle_obj = vehicle
                Purchase.purchase_history.append(self)
                Vehicle.inventory.remove(vehicle)
                break
            else:
                raise ValueError("Vehicle not found in inventory.")
        if len(Customer.customer_list) == 0:
            raise ValueError("Customer list is empty.")
        for customer in Customer.customer_list:
            if customer.get_id() == customer_id:
                self.__customer_obj = customer
                break
            else:
                raise ValueError("Customer not found in customer list.")
        self.__price = price
        self.__date = date

    def get_vin(self):
        """Returns the VIN of the car."""
        return self.__vin

    def get_customer(self):
        """Returns the customer who purchased the car."""
        return self.__customer

    def get_price(self):
        """Returns the price of the car."""
        return self.__price

    def get_date(self):
        """Returns the date of the purchase."""
        return self.__date

    def set_car(self, car):
        """Sets the car that was purchased."""
        self.__car = car

    def set_customer(self, customer):
        """Sets the customer who purchased the car."""
        self.__customer = customer

    def set_price(self, price):
        """Sets the price of the car."""
        self.__price = price

    def set_date(self, date):
        """Sets the date of the purchase."""
        self.__date = date

    def print_purchase(self):
        """Prints the details of the purchase."""
        self.__vehicle_obj.print_details()
        print("Customer: " + self.__customer_obj.get_name())
        print("Date: " + self.__date)

    @staticmethod
    def get_purchase_history():
        """Returns the purchase history."""
        return Purchase.purchase_history
    
    @staticmethod
    def print_purchase_history():
        """Prints the purchase history."""
        print("Purchase History".center(55, "-"))
        print()
        for purchase in Purchase.purchase_history:
            purchase.print_purchase()

class Customer:
    """A class that represents the customer"""
    # list of all customers
    customer_list = []
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__id = str(shortuuid.uuid())
        Customer.customer_list.append(self)

    def set_name(self, name):
        """Sets the name of the customer"""
        self.__name=name
    
    def set_phone(self, phone):
        """Sets the phone number of cutomer"""
        self.__phone=phone
    
    def set_email(self, email):
        """Sets the email of the customer"""
        self.__email=email
    
    def set_id(self, id):
        """Sets the id of the customer"""
        self.__id = id

    def regenerate_id(self):
        """Generates a new id"""
        self.__id = str(shortuuid.uuid())

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_id(self):
        return self.__id

    def print_details(self):
        """Prints the details of the customer"""
        print(f"Name: {self.__name}")
        print(f"ID: {self.__id}")
        print(f"Phone: {self.__phone}")
        print(f"Email: {self.__email}")
    
    @staticmethod
    def get_customer_list():
        """Returns the list of customers"""
        return Customer.customer_list
    
    @staticmethod
    def print_customer_list():
        """Prints the list of customers"""
        print("Customer List".center(55, "-"))
        print()
        for customer in Customer.customer_list:
            customer.print_details()

class User:
  """A class that represents a user"""
  def __init__(self, name, phone, email):
    self.__name = name
    self.__phone = phone
    self.__email = email

  def display_user(self):
    """Returns the credentials of the user"""
    print("Name: ", self.__name)
    print("Phone:", self.__phone)
    print("Email:", self.__email)