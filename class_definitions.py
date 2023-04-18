"""A module that contains the main class definitions."""
import time

class Vehicle:
    """A class that represents a Vehicle.
    It contains the following attributes: VIN, make, model, year, color,
    transmission, engine, and price.
    The VIN must be 17 characters long and correspond to the VIN of a vehicle in the inventory. 
    The year must be between 1900 and 2020. The price must be greater than or equal to 0. 
    The transmission must be one of the following: Automatic, Manual, or CVT."""
    # # dealership inventory
    # inventory = []

    def __init__(self, vin, make, model, year, color, transmission, engine, price):
        # check if a vehicle with the same VIN already exists (do this in the menu maker instead)
        # for vehicle in Vehicle.inventory:
        #     if vehicle.get_vin() == vin:
        #         raise ValueError("Vehicle with same VIN already exists.")
        # check if the VIN is valid
        if len(vin) != 17:
            raise ValueError("Invalid VIN.")
        # check if the year is valid
        if year < 1900 or year > int(time.strftime("%Y")):
            raise ValueError("Invalid year.")
        # check if the price is valid
        if price < 0:
            raise ValueError("Invalid price.")
        # check if the transmission is valid
        if transmission not in ["Automatic", "Manual", "CVT", "Electric", "Hybrid"]:
            raise ValueError("Invalid transmission.")
        # set the attributes
        self.__vin = vin
        self.__make = make
        self.__model = model
        self.__year = year
        self.__color = color
        self.__transmission = transmission
        self.__engine = engine
        self.__price = price

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

    def get_vehicle_details_as_list(self):
        """Returns the details of the car as a list."""
        return [self.__vin, self.__make, self.__model, self.__year, self.__color, self.__transmission, self.__engine, self.__price]

    
    # @staticmethod
    # def search_inventory(criteria):
    #     """Searches the dealership inventory for a vehicle that matches the given criteria.
    #     Returns a list of vehicles that match the criteria."""
    #     matching_vehicles = []
    #     if criteria == "":
    #         return matching_vehicles
    #     if criteria.isdigit():
    #         criteria = int(criteria)
    #     if str(criteria).replace(".", "", 1).isdigit():
    #         criteria = float(criteria)
    #     for vehicle in Vehicle.inventory:
    #        if criteria in vehicle.get_vehicle_details_as_list():
    #             matching_vehicles.append(vehicle)
    #     return matching_vehicles


class UsedVehicle(Vehicle):
    """A class that represents a used car. It inherits from the Vehicle class.
    It has an additional attributes mileage, title, condition and number of owners. 
    Milage should be a positive integer. Title should be one of the following: Clean, Salvage, Rebuilt.
    Condition should be one of the following: Excellent, Good, Fair, Poor."""

    def __init__(self, vin, make, model, year, color, transmission,
                 engine, price, mileage, title, condition, num_owners):
        """Initializes the used car object."""
        # check if the mileage is valid
        if mileage < 0:
            raise ValueError("Invalid mileage.")
        # check if the title is valid
        if title not in ["Clean", "Salvage", "Rebuilt"]:
            raise ValueError("Invalid title.")
        # check if the condition is valid
        if condition not in ["Excellent", "Good", "Fair", "Poor"]:
            raise ValueError("Invalid condition.")
        # check if the number of owners is valid
        if num_owners < 0:
            raise ValueError("Invalid number of owners.")
        # set the attributes
        super().__init__(vin, make, model, year, color, transmission, engine, price)
        self.__mileage = mileage
        self.__title = title
        self.__condition = condition
        self.__num_owners = num_owners

    def get_mileage(self):
        """Returns the mileage of the car."""
        return self.__mileage

    def get_title(self):
        """Returns the title of the car."""
        return self.__title

    def get_condition(self):
        """Returns the condition of the car."""
        return self.__condition

    def get_num_owners(self):
        """Returns the number of owners of the car."""
        return self.__num_owners

    def set_mileage(self, mileage):
        """Sets the mileage of the car."""
        self.__mileage = mileage

    def set_title(self, title):
        """Sets the title of the car."""
        self.__title = title

    def set_condition(self, condition):
        """Sets the condition of the car."""
        self.__condition = condition

    def set_num_owners(self, num_owners):
        """Sets the number of owners of the car."""
        self.__num_owners = num_owners

    def print_details(self):
        """Prints the details of the car."""
        super().print_details()
        print("Mileage: " + str(self.__mileage))
        print("Title: " + self.__title)
        print("Condition: " + self.__condition)
        print("Number of Owners: " + str(self.__num_owners))

    def get_vehicle_details_as_list(self):
        """Returns the details of the car as a list."""
        return super().get_vehicle_details_as_list() + [self.__mileage, self.__title, self.__condition, self.__num_owners]


class Purchase:
    """A class that represents a purchase of a car.
    It has attributes vehicle_obj, customer_obj and date.
    It takes the VIN of the car, the customer ID and the date of the purchase as arguments.
    It raises a ValueError if the inventory is empty or the vehicle is not found in the inventory.
    It raises a ValueError if the customer list is empty or the customer is not found in the customer list.
    It raises a ValueError if the date is not of the format mm/dd/yyyy and is not a valid date.
    If all of the arguments are valid, it assigns vehicle_obj and customer_obj to the corresponding objects."""

    def __init__(self, vin, customer_id, date):
        """Initializes the purchase object."""
        self.__vin = vin
        self.__customer_id = customer_id
        # date exception handling. Should be of the format mm/dd/yyyy
        if len(date) != 10:
            raise ValueError("Invalid date.")
        if date[2] != "/" or date[5] != "/":
            raise ValueError("Invalid date.")
        if int(date[0:2]) < 1 or int(date[0:2]) > 12:
            raise ValueError("Invalid date.")
        if int(date[0:2]) == 2 and int(date[3:5]) > 29:
            raise ValueError("Invalid date.")
        if int(date[0:2]) in [4, 6, 9, 11] and int(date[3:5]) > 30:
            raise ValueError("Invalid date.")
        if int(date[3:5]) < 1 or int(date[3:5]) > 31:
            raise ValueError("Invalid date.")
        if int(date[6:]) > time.localtime().tm_year:
            raise ValueError("Invalid date.")
        self.__date = date

    def get_vin(self):
        """Returns the VIN of the car."""
        return self.__vin
    
    def set_vin(self, vin):
        """Sets the VIN of the car."""
        self.__vin = vin
    
    def get_customer_id(self):
        """Returns the customer ID."""
        return self.__customer_id
    
    def set_customer_id(self, customer_id):
        """Sets the customer ID."""
        self.__customer_id = customer_id

    def get_date(self):
        """Returns the date of the purchase."""
        return self.__date

    def set_date(self, date):
        """Sets the date of the purchase."""
        self.__date = date

    def print_purchase(self):
        """Prints the details of the purchase."""
        self.vehicle_obj.print_details()
        print("Customer: " + self.customer_obj.get_name())
        print("Date: " + self.__date)

    def get_purchase_details_as_list(self):
        """Returns the details of the purchase as a list."""
        return self.vehicle_obj.get_vehicle_details_as_list() + [self.customer_obj.get_name(), self.__date]

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

    @staticmethod
    def search_purchases(criteria):
        """Searches for purchases based on the criteria.
        It takes the criteria as an argument.
        It returns a list of purchases that match the criteria."""
        matching_purchases = []
        if criteria == "":
            return matching_purchases
        if criteria.isdigit():
            criteria = int(criteria)
        if str(criteria).replace(".", "", 1).isdigit():
            criteria = float(criteria)
        for purchase in Purchase.purchase_history:
            if criteria in purchase.get_purchase_details_as_list():
                matching_purchases.append(purchase)
        return matching_purchases

class Customer:
    """A class that represents the customer.
    It has attributes name, phone, email and customer_id.
    The phone number should be of the format xxx-xxx-xxxx.
    It takes the name, phone and email as arguments."""

    def __init__(self, name, phone, email):
        if not name.isalpha():
            raise ValueError("Invalid name.")
        # phone number exception handling - should be of the format xxx-xxx-xxxx
        if len(phone) != 12 or phone[3] != "-" or phone[7] != "-":
            raise ValueError("Invalid phone number.")
        if email == "" or "@" not in email or "." not in email:
            raise ValueError("Invalid email.")
        self.__name = name
        self.__phone = phone
        self.__email = email

    def set_name(self, name):
        """Sets the name of the customer"""
        self.__name = name

    def set_phone(self, phone):
        """Sets the phone number of cutomer"""
        self.__phone = phone

    def set_email(self, email):
        """Sets the email of the customer"""
        self.__email = email

    def get_name(self):
        """Returns the name of the customer as a string"""
        return self.__name

    def get_phone(self):
        """Returns the phone of the customer as a string"""
        return self.__phone

    def get_email(self):
        """Returns the email of the customer as string"""
        return self.__email

    def print_details(self): # needs to be fixed
        """Prints the details of the customer"""
        print(f"Name: {self.__name}")
        print(f"ID: {self.__customer_id}")
        print(f"Phone: {self.__phone}")
        print(f"Email: {self.__email}")

    def get_details_as_list(self): # needs to be fixed
        """Returns the details of the customer as a list"""
        return [self.__name, self.__customer_id, self.__phone, self.__email]

    # @staticmethod
    # def get_customer_list():
    #     """Returns the list of customers"""
    #     return Customer.customer_list

    # @staticmethod
    # def print_customer_list():
    #     """Prints the list of customers"""
    #     print("Customer List".center(45, "-"))
    #     print()
    #     for customer in Customer.customer_list:
    #         customer.print_details()

    @staticmethod
    def print_numbered_customer_list_names_only():
        """Prints the list of customers with their names and their corresponding numbers"""
        if len(Customer.customer_list) == 0:
            print("No customers found.")
            return
        print("Customer List".center(45, "-"))
        print()
        for i, customer in enumerate(Customer.customer_list):
            print(f"{i + 1}. {customer.get_name()}")

    @staticmethod
    def search_customer(criteria):
        """Searches for a customer in the customer_list.
        It takes the criteria as an argument.
        It appends the customer object to the list if the criteria matches the name, id, phone or email of the customer."""
        search_results = []
        for customer in Customer.customer_list:
            if criteria in customer.get_details_as_list():
                search_results.append(customer)
        return search_results

class User:
    """A class that represents a user. 
    It has attributes name, phone, email and password.
    Phone numbers should be of the format xxx-xxx-xxxx."""

    def __init__(self, name, phone, email, password, username):
        if not name.isalpha():
            raise ValueError("Invalid name.")
        # phone number exception handling - should be of the format xxx-xxx-xxxx
        if len(phone) != 12 or phone[3] != "-" or phone[7] != "-":
            raise ValueError("Invalid phone number.")
        if email == "" or "@" not in email or "." not in email:
            raise ValueError("Invalid email.")
        self.__name = name
        self.__username = username
        self.__phone = phone
        self.__password = password
        self.__email = email

    def display_user(self):
        """Returns the credentials of the user"""
        print("Name: ", self.__name)
        print("Phone:", self.__phone)
        print("Email:", self.__email)
        print("Password:", self.__password)
    
    def get_username(self):
        """Returns the username of the user"""
        return self.__username

    def get_name(self):
        """Returns the name of the user"""
        return self.__name
    
    def get_phone(self):
        """Returns the phone number of the user"""
        return self.__phone
    
    def get_email(self):
        """Returns the email of the user"""
        return self.__email
    
    def get_password(self):
        """Returns the password of the user"""
        return self.__password
    
    def set_name(self, name):
        """Sets the name of the user"""
        self.__name = name

    def set_phone(self, phone):
        """Sets the phone number of the user"""
        self.__phone = phone

    def set_email(self, email):
        """Sets the email of the user"""
        self.__email = email

    def set_password(self, password):
        """Sets the password of the user"""
        self.__password = password

    def get_details_as_list(self):
        """Returns the details of the user as a list (But not the password)"""
        return [self.__name, self.__phone, self.__email]

    

    # needs to be fixed
    # @staticmethod
    # def search_user(criteria):
    #     """Searches for a user in the users list.
    #     It takes the criteria as an argument.
    #     It appends the user object to the list if the criteria matches the name, username, phone or email of the user."""
    #     search_results = []
    #     for user in User.users:
    #         if criteria in user.get_details_as_list():
    #             search_results.append(user)
    #     return search_results


class Admin(User):
    """A class that represents an admin. 
    It has attributes name, phone, email, and password.
    Phone numbers should be of the format xxx-xxx-xxxx."""
    
    @staticmethod
    def change_password(user, password):
        """Changes the password of another user"""
        user.set_password(password)
    
    @staticmethod
    def create_user():
        """Creates a new user"""
        name = input("Enter name: ")
        while 1:
            phone_candidate = input("Enter phone number: ")
            if len(phone_candidate) != 12 or phone_candidate[3] != "-" or phone_candidate[7] != "-":
                print("Invalid phone number. Please enter in the format xxx-xxx-xxxx.")
                continue
            else:
                phone = phone_candidate
                break
        while 1:
            email_candidate = input("Enter email: ")
            if email_candidate == "" or "@" not in email_candidate or "." not in email_candidate:
                print("Invalid email.")
                continue
            else:
                email = email_candidate
                break
        while 1:
            username_candidate = input("Enter username: ")
            if username_candidate in [user.get_username() for user in User.users]:
                print("Username already exists.")
                continue
            else:
                username = username_candidate
                break
        while 1:
            password_candidate = input("Enter password: ")
            password_candidate_2 = input("Confirm password: ")
            if password_candidate == "":
                print("Password cannot be empty.")
                continue
            elif password_candidate != password_candidate_2:
                print("Passwords do not match.")
                continue
            else:
                password = password_candidate
                break
        return User(name, phone, email, password, username)
