from pymongo import MongoClient
from bson import ObjectId
from class_definitions import User, Vehicle, UsedVehicle, Customer, Purchase, Admin

def connect_to_mongo():
    """Connects to the MongoDB database"""
    # try-except block to check if the server url exists
    try:
        with open('server_url.txt', 'r') as file:
            url = file.read()
        if url == "# Replace this line with the server url.":
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

def object_encoder(obj, car_details=None):
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
        dict = {
            "vin" : obj.get_vin(),
            "customer_id" : obj.get_customer_id(),
            "date" : obj.get_date(),
        }
        if car_details is not None:
            dict.update(car_details)
        return dict
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

def insert_object(object, car_details=None):
    """Inserts an object into the database"""
    db = connect_to_mongo()
    if isinstance(object, Vehicle) or isinstance(object, UsedVehicle):
        collection = db['inventory']
    elif isinstance(object, Customer):
        collection = db['customer']
    elif isinstance(object, Purchase):
        collection = db['purchase']
        result = collection.insert_one(object_encoder(object, car_details))
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
