from pymongo import MongoClient
from bson import ObjectId
from class_definitions import User, Vehicle, UsedVehicle, Customer, Purchase, Admin

def connect_to_mongo():
    """Connects to the MongoDB database"""
    # try-except block to check if the server url exists
    try:
        with open('server_url.txt', 'r') as file:
            url = file.read()
        # check if the url is a valid mongodb url
        if not url.startswith('mongodb://') and not url.startswith('mongodb+srv://'):
                raise Exception("Please enter the server url in the server_url.txt file with the MongoDB Server URL.")
    except FileNotFoundError:
        raise Exception("Please create a server_url.txt file with the MongoDB Server URL.")
    client = MongoClient(url)
    db = client['car-dealership']
    return db

def car_decoder(obj):
    if '_id' in obj:
        obj['_id'] = ObjectId(obj['_id'])
    car_kwargs = obj.copy()
    car_kwargs.pop('_id', None)
    return Vehicle(**car_kwargs)

def used_car_decoder(obj):
    if '_id' in obj:
        obj['_id'] = ObjectId(obj['_id'])
    car_kwargs = obj.copy()
    car_kwargs.pop('_id', None)
    return UsedVehicle(**car_kwargs)

def customer_decoder(obj):
    if '_id' in obj:
        obj['_id'] = ObjectId(obj['_id'])
    car_kwargs = obj.copy()
    car_kwargs.pop('_id', None)
    return Customer(**car_kwargs)

def purchase_decoder(obj):
    if '_id' in obj:
        obj['_id'] = ObjectId(obj['_id'])
    car_kwargs = obj.copy()
    car_kwargs.pop('_id', None)
    car_kwargs.pop('car_id', None)
    return Purchase(**car_kwargs)

def user_decoder(obj):
    if '_id' in obj:
        obj['_id'] = ObjectId(obj['_id'])
    car_kwargs = obj.copy()
    car_kwargs.pop('_id', None)
    return User(**car_kwargs)

def admin_decoder(obj):
    if '_id' in obj:
        obj['_id'] = ObjectId(obj['_id'])
    car_kwargs = obj.copy()
    car_kwargs.pop('_id', None)
    return Admin(**car_kwargs)

def object_encoder(obj):
    if isinstance(obj, Vehicle):
        return {
            "vin": obj.get_vin(),
            "make": obj.get_make(),
            "model": obj.get_model(),
            "year": obj.get_year(),
            "color": obj.get_color(),
            "transmission": obj.get_transmission(),
            "engine": obj.get_engine(),
            "price": obj.get_price(),
        }
    elif isinstance(obj, UsedVehicle):
        return {
            "vin": obj.get_vin(),
            "make": obj.get_make(),
            "model": obj.get_model(),
            "year": obj.get_year(),
            "color": obj.get_color(),
            "transmission": obj.get_transmission(),
            "engine": obj.get_engine(),
            "price": obj.get_price(),
            "mileage": obj.get_mileage(),
            "title": obj.get_title(),
            "condition": obj.get_condition(),
            "num_owners": obj.get_num_owners(),
        }
    elif isinstance(obj, Customer):
        return {
            "name" : obj.get_name(),
            "phone" : obj.get_phone(),
            "email" : obj.get_email(),
        }
    elif isinstance(obj, Purchase):
        return {
            "vin" : obj.get_vin(),
            "date" : obj.get_date()
        }
    elif isinstance(obj, User):
        return {
            "username" : obj.get_username(),
            "password" : obj.get_password(),
            "name" : obj.get_name(),
            "phone" : obj.get_phone(),
            "email" : obj.get_email(),
        }
    elif isinstance(obj, Admin):
        return {
            "username" : obj.get_username(),
            "password" : obj.get_password(),
            "name" : obj.get_name(),
            "phone" : obj.get_phone(),
            "email" : obj.get_email(),
        }
    else:
        raise TypeError(f"Object of type '{type(obj)}' is not JSON serializable")
 
def get_inventory():
    """Gets the car list from the database"""
    db = connect_to_mongo()
    car_list = []
    for car in db['inventory'].find():
        if car.get('mileage') is not None:
            car_list.append(UsedVehicle(used_car_decoder(car)))
        else:
            car_list.append(car_decoder(car))
    return car_list

def insert_object(object):
    """Inserts an object into the database"""
    db = connect_to_mongo()
    if isinstance(object, Vehicle) or isinstance(object, UsedVehicle):
        collection = db['inventory']
    elif isinstance(object, Customer):
        collection = db['customer']
    elif isinstance(object, Purchase):
        collection = db['purchase']
        result = collection.insert_one(object_encoder(object))
        # update the purchase document with the car_id
        db['purchase'].update_one({'_id': result.inserted_id}, {'$set': {'car_id': db['inventory'].find_one({'vin': object.get_vin()}).get('_id')}})
        # update the purchase document with the customer_id
        db['purchase'].update_one({'_id': result.inserted_id}, {'$set': {'customer_id': db['customer'].find_one({'_id': object.get_customer_id()}).get('_id')}})
        # copy the car document to the sold-vehicles collection
        db['sold-vehicles'].insert_one(db['inventory'].find_one({'vin': object.get_vin()}))
        # remove the sold car from the inventory
        db['inventory'].delete_one({'vin': object.get_vin()})
        return result.inserted_id
    elif isinstance(object, User):
        collection = db['user']
    elif isinstance(object, Admin):
        collection = db['admin']
    else:
        raise TypeError(f"Object of type '{type(object)}' is not JSON serializable")
    result = collection.insert_one(object_encoder(object))
    return result.inserted_id

def get_user_list():
    """Gets the user list from the database"""
    db = connect_to_mongo()
    user_list = []
    for user in db['user'].find():
        user_list.append(user_decoder(user))
    for user in db['admin'].find():
        user_list.append(admin_decoder(user))
    return user_list

def get_customer_list():
    """Gets the customer list from the database"""
    db = connect_to_mongo()
    customer_list = []
    for customer in db['customer'].find():
        customer_list.append(customer_decoder(customer))
    return customer_list

def authenticate_user(username, password):
    """Authenticates a user"""
    user_list = get_user_list()
    for user in user_list:
        if user.get_username() == username and user.get_password() == password:
            return True, user
    return False, None

def check_vin(vin):
    """Checks if a vin is already in the database"""
    car_list = get_inventory()
    for car in car_list:
        if car.get_vin() == vin:
            return True
    return False

def print_numbered_vehicle_list():
    """Prints the inventory list with numbers"""
    car_list = get_inventory()
    if len(car_list) == 0:
        print("There are no cars in the database")
        return
    for i in range(len(car_list)):
        print(f"{i+1}. {car_list[i].get_year()} {car_list[i].get_make()} {car_list[i].get_model()}")

def print_numbered_customer_list():
    """Prints the customer list with numbers"""
    customer_list = get_customer_list()
    if len(customer_list) == 0:
        print("There are no customers in the database")
        return
    for i in range(len(customer_list)):
        print(f"{i+1}. {customer_list[i].get_name()}")

def get_customer_id(customer_name, customer_phone, customer_email):
    """Gets the ObjectID of a customer from the database"""
    db = connect_to_mongo()
    customer = db['customer'].find_one({'name': customer_name, 'phone': customer_phone, 'email': customer_email})
    return customer['_id']

def search_cars(search_critera):
    """Searches the database for cars"""
    db = connect_to_mongo()
    car_list = []
    for car in db['inventory'].find(search_critera):
        if car.get('mileage') is not None:
            car_list.append(UsedVehicle(used_car_decoder(car)))
        else:
            car_list.append(car_decoder(car))
    return car_list

def search_sold_cars(search_critera):
    """Searches the database for cars"""
    db = connect_to_mongo()
    car_list = []
    for car in db['sold-vehicles'].find(search_critera):
        if car.get('mileage') is not None:
            car_list.append(UsedVehicle(used_car_decoder(car)))
        else:
            car_list.append(car_decoder(car))
    return car_list

def search_users(search_critera):
    """Searches the database for users"""
    db = connect_to_mongo()
    user_list = []
    for user in db['user'].find(search_critera):
        user_list.append(user_decoder(user))
    for user in db['admin'].find(search_critera):
        user_list.append(admin_decoder(user))
    return user_list

def search_customers(search_critera):
    """Searches the database for customers"""
    db = connect_to_mongo()
    customer_list = []
    for customer in db['customer'].find(search_critera):
        customer_list.append(customer_decoder(customer))
    return customer_list

def search_purchases(search_critera):
    """Searches the database for purchases"""
    db = connect_to_mongo()
    purchase_list = []
    # if the search criteria is for a car
    if 'make' in search_critera.keys() or 'model' in search_critera.keys() or 'year' in search_critera.keys() or 'mileage' in search_critera.keys() or 'price' in search_critera.keys() or 'color' in search_critera.keys() or 'transmission' in search_critera.keys() or 'engine' in search_critera.keys() or 'number_of_owners' in search_critera.keys() or 'vin' in search_critera.keys() or 'title' in search_critera.keys() or 'condition' in search_critera.keys():
        for car in db['sold-vehicles'].find(search_critera):
            # get the id of the car
            car_id = car['_id']
            # search for the purchase with the car id
            for purchase in db['purchase'].find({'car_id': car_id}):
                purchase_list.append(purchase_decoder(purchase))
    # if the search criteria is for a customer
    elif 'name' in search_critera.keys() or 'phone' in search_critera.keys() or 'email' in search_critera.keys():
        # get the id of the customer
        customer = db['customer'].find_one(search_critera)
        customer_id = customer['_id']
        # search for the purchase with the customer id
        for purchase in db['purchase'].find({'customer_id': customer_id}):
            purchase_list.append(purchase_decoder(purchase))
    # if the search criteria is vin, customer_id, or date
    else:
        for purchase in db['purchase'].find(search_critera):
            purchase_list.append(purchase_decoder(purchase))
    return purchase_list

def print_purchase(purchase):
    """Prints the details of a purchase"""
    db = connect_to_mongo()
    result = db['purchase'].find_one({'vin': purchase.get_vin(), 'date': purchase.get_date()})
    customer_id = result['customer_id']
    customer = search_customers({'_id': customer_id})
    car_id = result['car_id']
    car = search_sold_cars({'_id': car_id})
    print(f"-------{car[0].get_year()} {car[0].get_make()} {car[0].get_model()} purchased by {customer[0].get_name()} on {result['date']}-------")
    print(f"VIN: {result['vin']}")
    print(f"Price: ${car[0].get_price()}")
    print(f"Customer ID: {customer_id}")
    print(f"Customer Name: {customer[0].get_name()}")
    print(f"Customer Phone: {customer[0].get_phone()}")
    print(f"Customer Email: {customer[0].get_email()}")
    print(f"Make: {car[0].get_make()}")
    print(f"Model: {car[0].get_model()}")
    print(f"Year: {car[0].get_year()}")
    print(f"Color: {car[0].get_color()}")
    print(f"Engine: {car[0].get_engine()}")
    print(f"Transmission: {car[0].get_transmission()}")
    if isinstance(car[0], UsedVehicle):
        print(f"Mileage: {car[0].get_mileage()}")
        print(f"Condition: {car[0].get_condition()}")
        print(f"Title Status: {car[0].get_title()}")


def change_password(user, password):
    """Changes the password of a user"""
    db = connect_to_mongo()
    if isinstance(user, Admin):
        db['admin'].update_one({'username': user.get_username()}, {'$set': {'password': password}})
    else:
        db['user'].update_one({'username': user.get_username()}, {'$set': {'password': password}})

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
            # check if username already exists in users or admins collection
            if search_users({'username': username_candidate}):
                print("Username already exists.")
                continue
            else:
                username = username_candidate
                break
        while 1:
            password_candidate = input("Enter password: ")
            if password_candidate == "":
                print("Password cannot be empty.")
                continue
            elif len(password_candidate) < 8:
                print("Password must be at least 8 characters.")
                continue
            else:
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
        user = User(name, phone, email, password, username)
        try:
            insert_object(user)
            print("User created successfully.")
        except:
            print("Error creating user.")
