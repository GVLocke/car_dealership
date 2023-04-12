import time
import class_definitions as cd
test_admin = cd.Admin("test", "555-555-5555", "test@test.test", "test", "test")
toyota = cd.Vehicle("ttttttttttttttttt", "Toyota", "Camry", 2023, "Black", "Automatic", "2.5L 4-Cylinder", 20000.00)
toyota2 = cd.Vehicle("tttttttttttt3tttt", "Toyota", "Camry", 2023, "Black", "Automatic", "2.5L 4-Cylinder", 20000.00)
joe_customer = cd.Customer("joe", "555-555-5555", "kjoe@ntn.co")
joe_purchase = cd.Purchase("ttttttttttttttttt", joe_customer.get_id(), "01/01/2021")

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
    # if isinstance(current_user, cd.Admin):
    #     print("5. Admin Menu")
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
    elif selection == 1:
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
            # get condition, validate input
            while 1:
                condition_candidate = str(input("Condition (E for Excellent / G for Good / F for Fair / P for Poor): "))
                if condition_candidate.upper() == "E":
                    condition = "Excellent"
                    break
                elif condition_candidate.upper() == "G":
                    condition = "Good"
                    break
                elif condition_candidate.upper() == "F":
                    condition = "Fair"
                    break
                elif condition_candidate.upper() == "P":
                    condition = "Poor"
                    break
                else:
                    print("Invalid input. Please enter E, G, F, or P.")
                    continue
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
                               title_status, condition, num_owners)
            print("Car added to inventory.")
            continue
        except ValueError as e:
            print(e)
            break
    # record a sale
    elif selection == 2:
        print("Record a Sale".center(50, "-"))
        # search for a car in the list of cars
        # print list of cars
        cd.Vehicle.print_numbered_vehicle_list()
        # get car selection, validate input
        while 1:
            car_selection_candidate = str(input("Enter car number or enter 0 to exit: "))
            if not car_selection_candidate.isdigit() or int(car_selection_candidate) < 0 or int(car_selection_candidate) > len(cd.Vehicle.inventory):
                print(f"Invalid input. Please enter a number between 1 and {len(cd.Vehicle.inventory)}.")
                continue
            elif int(car_selection_candidate) == 0:
                break
            else:
                car_selection = int(car_selection_candidate)
                # get vin of selected car
                vin = cd.Vehicle.inventory[car_selection - 1].get_vin()
                break
        if int(car_selection_candidate) == 0:
            continue
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
                    customer_id = cd.Customer.customer_list[-1].get_id()
                    break
                except ValueError as e:
                    print(e)
                    break
            else:
                customer_selection = int(customer_selection_candidate)
                # get id of selected customer
                customer_id = cd.Customer.customer_list[customer_selection - 1].get_id()
                break
        # get sale date, validate input
        while 1:
            sale_date_candidate = str(input("Sale Date (MM/DD/YYYY): "))
            if len(sale_date_candidate) != 10 or sale_date_candidate[2] != "/" or sale_date_candidate[5] != "/":
                print("Invalid input. Please enter a date in the format MM/DD/YYYY.")
                continue
            # check if date is valid (month must be between 1 and 12, day must be between 1 and 31, year must be between 1900 and current year)
            # also check if day is valid for the month (e.g. 2/29/2020 is not valid)
            elif int(sale_date_candidate[0:2]) < 1 or int(sale_date_candidate[0:2]) > 12:
                print("Invalid input. Please enter a valid month.")
                continue
            elif int(sale_date_candidate[3:5]) < 1 or int(sale_date_candidate[3:5]) > 31:
                print("Invalid input. Please enter a valid day.")
                continue
            elif int(sale_date_candidate[6:10]) < 1900 or int(sale_date_candidate[6:10]) > time.localtime().tm_year:
                print("Invalid input. Please enter a valid year.")
                continue
            elif int(sale_date_candidate[0:2]) == 2 and int(sale_date_candidate[3:5]) > 29:
                print("Invalid input. Please enter a valid day.")
                continue
            elif int(sale_date_candidate[0:2]) in [4, 6, 9, 11] and int(sale_date_candidate[3:5]) > 30:
                print("Invalid input. Please enter a valid day.")
                continue
            else:
                sale_date = sale_date_candidate
                break
        # try to create a new sale
        try:
            cd.Purchase(vin, customer_id, sale_date)
            print("Sale recorded.")
            continue
        except ValueError as e:
            print(e)
            continue
    # search
    elif selection == 3:
        while 1:
            print("Search".center(50, "-"))
            print("1. Search for a car")
            print("2. Search for a customer")
            print("3. Search for a Purchase")
            print("4. Exit")
            # get search selection, validate input
            while 1:
                search_selection_candidate = str(input("Enter selection: "))
                if not search_selection_candidate.isdigit() or int(search_selection_candidate) < 1 or int(search_selection_candidate) > 4:
                    print("Invalid input. Please enter a number between 1 and 4.")
                    continue
                else:
                    search_selection = int(search_selection_candidate)
                    break
            # search for a car
            if search_selection == 1:
                print("Search for a Car".center(50, "-"))
                search_criteria = str(input("Enter search criteria: "))
                if len(cd.Vehicle.search_inventory(search_criteria)) == 0:
                    print("No cars found.")
                    continue
                else:
                    for car in cd.Vehicle.search_inventory(search_criteria):
                        car.print_details()
                    continue
            # search for a customer
            elif search_selection == 2:
                print("Search for a Customer".center(50, "-"))
                search_criteria = str(input("Enter search criteria: "))
                if len(cd.Customer.search_customer(search_criteria)) == 0:
                    print("No customers found.")
                    continue
                else:
                    for customer in cd.Customer.search_customer(search_criteria):
                        customer.print_details()
                continue
            # search for a purchase
            elif search_selection == 3:
                print("Search for a Purchase".center(50, "-"))
                search_criteria = str(input("Enter search criteria: "))
                if len(cd.Purchase.search_purchases(search_criteria)) == 0:
                    print("No sales found.")
                    continue
                else:
                    for sale in cd.Purchase.search_purchases(search_criteria):
                        sale.print_purchase()
                continue
            # exit
            elif search_selection == 4:
                break
    # user settings
    elif selection == 4:
        while 1:
            print("User Settings".center(50, "-"))
            print("1. Change password")
            print("2. Exit")
            # get user settings selection, validate input
            while 1:
                user_settings_selection_candidate = str(input("Enter selection: "))
                if not user_settings_selection_candidate.isdigit() or int(user_settings_selection_candidate) < 1 or int(user_settings_selection_candidate) > 2:
                    print("Invalid input. Please enter a number between 1 and 2.")
                    continue
                else:
                    user_settings_selection = int(user_settings_selection_candidate)
                    break
            # change password
            if user_settings_selection == 1:
                while 1:
                    old_password_candidate = str(input("Old Password: "))
                    if old_password_candidate != current_user.get_password():
                        print("Incorrect password.")
                        continue
                    else:
                        old_password = old_password_candidate
                        break
                while 1:
                    new_password_candidate = str(input("New Password: "))
                    if len(new_password_candidate) < 8:
                        print("Password must be at least 8 characters.")
                        continue
                    else:
                        new_password = new_password_candidate
                        break
                while 1:
                    confirm_password_candidate = str(input("Confirm Password: "))
                    if confirm_password_candidate != new_password:
                        print("Passwords do not match.")
                        continue
                    else:
                        confirm_password = confirm_password_candidate
                        break
                # try to change password
                try:
                    current_user.set_password(new_password)
                    print("Password changed.")
                    break
                except ValueError as e:
                    print(e)
                    break
            # exit
            elif user_settings_selection == 2:
                break