# Car Dealership Management System

## Abstract
Car dealerships across the country must keep track of a lot of information to ensure that their operations run smoothly. Every vehicle that enters their lot has numerous data points that are relevant to both customers considering the vehicle and salespeople selling it. Important metrics include car miles, owner history, make, model, and trim. With so much information to manage, it's easy for smaller dealerships to become disorganized and lose track of this essential data.

To address this issue, this project aims to assist car dealerships in managing sales, as well as past and present inventory, by implementing a Python-based management system. This system will help dealerships stay organized and make it easier for them to access important information about each vehicle they currently have or have ever sold. The information will be stored in a neatly-organized, easily-searchable database. By streamlining information access, car dealerships can save time and resources, while also improving customer satisfaction.

Overall, this project seeks to provide an effective solution to a common problem faced by car dealerships. By implementing a management system in Python, dealerships can better manage their operations, improve their bottom line, and enhance the overall customer experience.

## Modules

### User Login
The owners and employees of the dealership will login to the database using a username and password to keep the system secure. Admins will have privileged access to sensitive customer information. 

### Menu
The main menu will allow users to access the functions of the program. The program will be a command-line interface.

### Add a Car to Inventory
The first function allows users to add cars to the current inventory and record relevant metadata. The cars inputted are then pushed to the MongoDB database.

### Record a Sale
The second function allows users to record a sale of a car to a customer. Selling the car removes it from the inventory.

### Search
The third function of the program will be the ability to search the entire database based on particular filters like make/model/year, price range, etc. They will be able to search their current inventory as well as the sales history. Users can also search for data on previous customers.

### User Menu
Users are able to change their own password.

### Admin Menu
Admins are able to add new users/admins or remove existing ones.

### Database Implementation
To keep the data safe and available, we need to save it permanently. That's why we must use a reliable and secure database system to store all the information recorded by users.


## Installation
Dependencies: pymongo

You also need to create a file called server_url.txt and put the url of your mongoDB server in it.

You can install using `pip install -r requirements.txt`
