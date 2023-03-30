import time
import class_definitions as cd
james_admin = cd.Admin("James", "555-555-5555", "james@test.test", "jkq", "jkq")



# def password_unlock():
#    password = input("Enter password: ")
#    if password == "opensaysame": 
#        return True
#    else:
#        print("Wrong password.")
#        return False

     
# if password_unlock():
  
#   while (1):
    
#     print("option 1: Display User")
#     print("option 2: ")

#     option = input()






#     if option == 1:
#       N = input("Enter name: ")

#       UserAndy = cd.User("Andy", "555-555-5555", "koernera@jbu.edu")
#       if N == 'Andy' or N== 'andy':
#         UserAndy.display_user()

#       UserJames = cd.User("James", "666-666-6666", "keysj@jbu.edu")
#       if N== 'James' or N == 'james':
#         cd.User.display_user()

#       else:
#         print("Not a user")

# login
while 1:
    print("Welcome!".center(50, "-"))
    print("1. Login")
    print("2. Exit")
    while 1:
        selection_candidate = str(input("Enter selection: "))
        if not selection_candidate.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        else:
            selection = int(selection_candidate)
            break
    if selection == 1:
        print("Login".center(50, "-"))
        username = input("Username: ")
        password = input("Password: ")
        if cd.User.authenticate_user(username, password)[0]:
            print("Login successful!")
            print("Welcome, {}!".format(username))
            global current_user
            current_user = cd.User.authenticate_user(username, password)[1]
            break
        else:
            print("Invalid username or password.")
    elif selection == 2:
        exit(0)
    else:
        print("Invalid selection. Please enter a number from the list.")
        continue

# main menu
while 1:
    print("Main Menu".center(50, "-"))
    print("1. Add a Car to the Inventory")
    print("2. Record a Sale")
    print("3. Search")
    print("4. User Settings")
    # check if current user is an admin
    if isinstance(current_user, cd.Admin):
        print("5. Admin Menu")
    print("0. Exit")
    # get menu selection, validate input
    while 1:
        selection_candidate = str(input("Enter selection: "))
        if not selection_candidate.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        else:
            selection = int(selection_candidate)
            break
    # exit program
    if selection == 0:
        exit(0)
    # add a car to the inventory
    if selection == 1:
        print("Add a Car to the Inventory".center(50, "-"))
        # check if the car is new or used
        while 1:
            new_or_used_candidate = str(input("New or Used? (N/U): "))
            if new_or_used_candidate.upper() == "N":
                new_or_used = "New"
                year = int(time.strftime("%Y"))
                break
            elif new_or_used_candidate.upper() == "U":
                new_or_used = "Used"
                break
            else:
                print("Invalid input. Please enter N or U.")
                continue
        make = input("Make: ")
        model = input("Model: ")
        if new_or_used == "Used":
            # get year, validate input
            while 1:
                year_candidate = str(input("Year: "))
                if not year_candidate.isdigit() or int(year_candidate) < 1900 or int(year_candidate) > int(time.strftime("%Y")):
                    print("Invalid input. Please enter a number.")
                    continue
                else:
                    year = int(year_candidate)
                    break
        color = input("Color: ")
        # get transmission, validate input
        while 1:
            transmission_candidate = str(input("Transmission (A for Automatic / M for Manual / C for CVT / E for Electric / H for Hybrid): "))
            if transmission_candidate.upper() == "A":
                transmission = "Automatic"
                break
            elif transmission_candidate.upper() == "M":
                transmission = "Manual"
                break
            elif transmission_candidate.upper() == "C":
                transmission = "CVT"
                break
            elif transmission_candidate.upper() == "E":
                transmission = "Electric"
                break
            elif transmission_candidate.upper() == "H":
                transmission = "Hybrid"
                break
            else:
                print("Invalid input. Please enter A, M, C, E, or H.")
                continue
        # get engine
        engine = str(input("Engine: "))
        # get price (float), validate input
        while 1:
            price_candidate = str(input("Price: "))
            if not price_candidate.replace(".", "", 1).isdigit() or float(price_candidate) < 0:
                print("Invalid input. Please enter a number.")
                continue
            else:
                price = float(price_candidate)
                break
        # used cars only
        if new_or_used == "Used":
            # get mileage (int), validate input
            while 1:
                mileage_candidate = str(input("Mileage: "))
                if not mileage_candidate.isdigit() or int(mileage_candidate) < 0:
                    print("Invalid input. Please enter a number greater than 0.")
                    continue
                else:
                    mileage = int(mileage_candidate)
                    break
            # get title status, validate input
            while 1:
                title_status_candidate = str(input("Title Status (C for Clean / S for Salvage / R for Rebuilt): "))
                if title_status_candidate.upper() == "C":
                    title_status = "Clean"
                    break
                elif title_status_candidate.upper() == "S":
                    title_status = "Salvage"
                    break
                elif title_status_candidate.upper() == "R":
                    title_status = "Rebuilt"
                    break
                else:
                    print("Invalid input. Please enter C, S, or R.")
                    continue
            # get number of owners (int), validate input
            while 1:
                num_owners_candidate = str(input("Number of Owners: "))
                if not num_owners_candidate.isdigit() or int(num_owners_candidate) < 0:
                    print("Invalid input. Please enter a number greater that 0.")
                    continue
                else:
                    num_owners = int(num_owners_candidate)
                    break
        # get VIN, validate input
        while 1:
            vin = str(input("VIN: "))
            if len(vin) != 17:
                print("Invalid input. Please enter a 17-character VIN.")
                continue
            else:
                break
        # attempt to add car to inventory
        try:
            if new_or_used == "New":
                cd.Vehicle(vin, make, model, year, color, transmission, engine, price)
            else:
                cd.UsedVehicle(vin, make, model, year, color, transmission, engine, price, mileage,
                               title_status, num_owners)
            print("Car added to inventory.")
        except ValueError as e:
            print(e)
            break
    # record a sale
    elif selection == 2:
        print("Record a Sale".center(50, "-"))
        # search for a customer in the list of customers
        # print list of customers
        cd.Customer.print_numbered_customer_list_names_only()
        # get customer selection, validate input
        while 1:
            customer_selection_candidate = str(input("Enter customer number or enter 0 to add a new customer: "))
            if not customer_selection_candidate.isdigit() or int(customer_selection_candidate) < 0 or int(customer_selection_candidate) > len(cd.Customer.customer_list):
                print(f"Invalid input. Please enter a number between 1 and {len(cd.Customer.customer_list)}.")
                continue
            elif int(customer_selection_candidate) == 0:
                # create a new customer
                # get customer name, validate input
                while 1:
                    name_candidate = str(input("Customer Name: "))
                    if not name_candidate.isalpha():
                        print("Invalid input. Please enter a name.")
                        continue
                    else:
                        name = name_candidate
                        break
                # get customer phone number, validate input
                while 1:
                    phone_number_candidate = str(input("Phone Number: "))
                    if len(phone_number_candidate) != 12 or phone_number_candidate[3] != "-" or phone_number_candidate[7] != "-":
                        print("Invalid input. Please enter a phone number in the format XXX-XXX-XXXX.")
                        continue
                    else:
                        phone_number = phone_number_candidate
                        break
                # get customer email, validate input
                while 1:
                    email_candidate = str(input("Email: "))
                    if "@" not in email_candidate or "." not in email_candidate:
                        print("Invalid input. Please enter an email address.")
                        continue
                    else:
                        email = email_candidate
                        break
                # try to create a new customer
                try:
                    cd.Customer(name, phone_number, email)
                    print("Customer added to list.")
                except ValueError as e:
                    print(e)
                    break
            else:
                customer_selection = int(customer_selection_candidate)
                # get id of selected customer
                customer_id = cd.Customer.customer_list[customer_selection - 1].get_id()
                break
