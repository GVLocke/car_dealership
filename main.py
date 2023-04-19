import time
import class_definitions as cd
import functions as fn

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
        if fn.authenticate_user(username, password)[0]:
            print("Login successful!")
            print("Welcome, {}!".format(username))
            current_user = fn.authenticate_user(username, password)[1]
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
    # check if current_user is an admin
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
            elif not vin.isalnum():
                print("Invalid input. Please enter a 17-character VIN.")
                continue
            elif fn.check_vin(vin):
                print("VIN already exists.")
                continue
            else:
                break
        # attempt to add car to inventory
        try:
            if new_or_used == "New":
                car = cd.Vehicle(vin, make, model, year, color, transmission, engine, price)
            else:
                car = cd.UsedVehicle(vin, make, model, year, color, transmission, engine, price, mileage,
                               title_status, condition, num_owners)
            fn.insert_object(car)
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
        fn.print_numbered_vehicle_list()
        inventory = fn.get_inventory()
        if len(inventory) == 0:
            continue
        # get car selection, validate input
        while 1:
            car_selection_candidate = str(input("Enter car number or enter 0 to exit: "))
            if not car_selection_candidate.isdigit() or int(car_selection_candidate) < 0 or int(car_selection_candidate) > len(inventory):
                print(f"Invalid input. Please enter a number between 1 and {len(inventory)}.")
                continue
            elif int(car_selection_candidate) == 0:
                break
            else:
                car_selection = int(car_selection_candidate)
                # get vin of selected car
                vin = inventory[car_selection - 1].get_vin()
                break
        if int(car_selection_candidate) == 0:
            continue
        # search for a customer in the list of customers
        # print list of customers
        customer_list = fn.get_customer_list()
        if len(customer_list) == 0:
            continue
        fn.print_numbered_customer_list()
        # get customer selection, validate input
        while 1:
            customer_selection_candidate = str(input("Enter customer number or enter 0 to add a new customer: "))
            if not customer_selection_candidate.isdigit() or int(customer_selection_candidate) < 0 or int(customer_selection_candidate) > len(customer_list):
                print(f"Invalid input. Please enter a number between 1 and {len(customer_list)}.")
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
                    customer = cd.Customer(name, phone_number, email)
                    fn.insert_object(customer)
                    print("Customer added to list.")
                    customer_id = fn.get_customer_id(name, phone_number, email)
                    break
                except ValueError as e:
                    print(e)
                    break
            else:
                customer_selection = int(customer_selection_candidate)
                name = customer_list[customer_selection - 1].get_name()
                phone_number = customer_list[customer_selection - 1].get_phone()
                email = customer_list[customer_selection - 1].get_email()
                customer_id = fn.get_customer_id(name, phone_number, email)
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
            purchase = cd.Purchase(vin, customer_id, sale_date)
            fn.insert_object(purchase)
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
                search_critera = {}
                while 1:
                    print("Search critera:")
                    print("1. Year")
                    print("2. Make")
                    print("3. Model")
                    print("4. Mileage")
                    print("5. Price")
                    print("6. Color")
                    print("7. Transmission")
                    print("8. Engine")
                    print("9. Number of Owners")
                    print("10. VIN")
                    print("11. Title")
                    print("12. Condition")
                    print("0. Search")
                    if len(search_critera) > 0:
                        print("Current search critera:")
                        for key, value in search_critera.items():
                            print(f"{key}: {value}")
                    choice = input("Enter a number to add to the search criteria or 0 to search with the current criteria: ")
                    if choice == "0":
                        break
                    # get year validate input
                    elif choice == "1":
                        while 1:
                                year = input("Enter a year: ")
                                if year.isdigit():
                                    search_critera.update({'year': int(year)})
                                    break
                                else:
                                    print("Invalid input. Please enter a valid year")
                    # get make validate input
                    elif choice == "2":
                        while 1:
                            make = input("Enter a make: ")
                            if make.isalpha():
                                search_critera.update({'make': make})
                                break
                            else:
                                print("Invalid input. Please enter a valid make")
                    # get model validate input
                    elif choice == "3":
                        while 1:
                            model = input("Enter a model: ")
                            if model.isalpha():
                                search_critera.update({'model': model})
                                break
                            else:
                                print("Invalid input. Please enter a valid model")
                    # get mileage validate input
                    elif choice == "4":
                        while 1:
                            mileage = input("Enter a mileage: ")
                            if mileage.isdigit():
                                search_critera.update({'mileage': int(mileage)})
                                break
                            else:
                                print("Invalid input. Please enter a valid mileage")
                    # get price validate input
                    elif choice == "5":
                        while 1:
                            price = input("Enter a price: ")
                            if price.isdigit():
                                search_critera.update({'price': int(price)})
                                break
                            else:
                                print("Invalid input. Please enter a valid price")
                    # get color validate input
                    elif choice == "6":
                        while 1:
                            color = input("Enter a color: ")
                            if color.isalpha():
                                search_critera.update({'color': color})
                                break
                            else:
                                print("Invalid input. Please enter a valid color")
                    # get transmission validate input
                    elif choice == "7":
                        while 1:
                            transmission = input("Enter a transmission: ")
                            if transmission in ['Automatic', 'Manual', 'CVT', 'Hybrid', 'Electric']:
                                search_critera.update({'transmission': transmission})
                                break
                            else:
                                print("Invalid input. Please enter a valid transmission")
                    # get engine validate input
                    elif choice == "8":
                        while 1:
                            engine = input("Enter a engine: ")
                            if engine.isalpha():
                                search_critera.update({'engine': engine})
                                break
                            else:
                                print("Invalid input. Please enter a valid engine")
                    # get number of owners validate input
                    elif choice == "9":
                        while 1:
                            owners = input("Enter a number of owners: ")
                            if owners.isdigit():
                                search_critera.update({'owners': int(owners)})
                                break
                            else:
                                print("Invalid input. Please enter a valid number of owners")
                    # get vin validate input
                    elif choice == "10":
                        while 1:
                            vin = input("Enter a vin: ")
                            if vin.isalnum() and len(vin) == 17:
                                search_critera.update({'vin': vin})
                                break
                            else:
                                print("Invalid input. Please enter a valid vin")
                    # get title validate input
                    elif choice == "11":
                        while 1:
                            title = input("Enter a title: ")
                            if title in ['Clean', 'Salvage', 'Rebuilt']:
                                search_critera.update({'title': title})
                                break
                            else:
                                print("Invalid input. Please enter a valid title")
                    # get condition validate input
                    elif choice == "12":
                        while 1:
                            condition = input("Enter a condition: ")
                            if condition in ['Excellent', 'Good', 'Fair', 'Poor']:
                                search_critera.update({'condition': condition})
                                break
                            else:
                                print("Invalid input. Please enter a valid condition")
                    else:
                        print("Invalid input. Please enter a valid number")
                for car in fn.search_cars(search_critera):
                    car.print_details()
            # search for a customer
            elif search_selection == 2:
                print("Search for a Customer".center(50, "-"))
                search_critera = {}
                while 1:
                    print("Search Criteria:")
                    print("1. Name")
                    print("2. Phone")
                    print("3. Email")
                    print("0. Search")
                    if len(search_critera) > 0:
                        print("Current Search Criteria:")
                        for key, value in search_critera.items():
                            print(f"{key}: {value}")
                    choice = input("Enter a number to add the search criteria, or enter 0 to search with the current critera: ")
                    # get name, validate
                    if choice == "1":
                        while 1:
                            name = input("Enter a name: ")
                            if not name.isalpha():
                                print("Invalid name")
                            else:
                                search_critera.update({'name': name})
                                break
                    # get phone, validate (must be xxx-xxx-xxxx)
                    elif choice == "2":
                        while 1:
                            phone = input("Enter a phone number: ")
                            if not phone[3] == "-" and phone[7] == "-":
                                print("Invalid phone number")
                            else:
                                search_critera.update({'phone': phone})
                                break
                    # get email, validate
                    elif choice == "3":
                        while 1:
                            email = input("Enter an email: ")
                            if not "@" in email and "." in email:
                                print("Invalid email")
                            else:
                                search_critera.update({'email': email})
                                break
                    # search
                    elif choice == "0":
                        break
                if len(fn.search_customers(search_critera)) == 0:
                    print("No customers found")
                for customer in fn.search_customers(search_critera):
                    customer.print_details()
            # search for a purchase
            elif search_selection == 3:
                print("Search for a Purchase".center(50, "-"))
                search_critera = {}
                while 1:
                    print("Search critera:")
                    print("1. Year")
                    print("2. Make")
                    print("3. Model")
                    print("4. Mileage")
                    print("5. Price")
                    print("6. Color")
                    print("7. Transmission")
                    print("8. Engine")
                    print("9. Number of Owners")
                    print("10. VIN")
                    print("11. Title")
                    print("12. Condition")
                    print("13. Customer Name")
                    print("14. Customer Phone")
                    print("15. Customer Email")
                    print("0. Search")
                    if len(search_critera) > 0:
                        print("Current search critera:")
                        for key, value in search_critera.items():
                            print(f"{key}: {value}")
                    choice = input("Enter a number to add to the search criteria or 0 to search with the current criteria: ")
                    if choice == "0":
                        break
                    # get year validate input
                    elif choice == "1":
                        while 1:
                                year = input("Enter a year: ")
                                if year.isdigit():
                                    search_critera.update({'year': int(year)})
                                    break
                                else:
                                    print("Invalid input. Please enter a valid year")
                    # get make validate input
                    elif choice == "2":
                        while 1:
                            make = input("Enter a make: ")
                            if make.isalpha():
                                search_critera.update({'make': make})
                                break
                            else:
                                print("Invalid input. Please enter a valid make")
                    # get model validate input
                    elif choice == "3":
                        while 1:
                            model = input("Enter a model: ")
                            if model.isalpha():
                                search_critera.update({'model': model})
                                break
                            else:
                                print("Invalid input. Please enter a valid model")
                    # get mileage validate input
                    elif choice == "4":
                        while 1:
                            mileage = input("Enter a mileage: ")
                            if mileage.isdigit():
                                search_critera.update({'mileage': int(mileage)})
                                break
                            else:
                                print("Invalid input. Please enter a valid mileage")
                    # get price validate input
                    elif choice == "5":
                        while 1:
                            price = input("Enter a price: ")
                            if price.isdigit():
                                search_critera.update({'price': int(price)})
                                break
                            else:
                                print("Invalid input. Please enter a valid price")
                    # get color validate input
                    elif choice == "6":
                        while 1:
                            color = input("Enter a color: ")
                            if color.isalpha():
                                search_critera.update({'color': color})
                                break
                            else:
                                print("Invalid input. Please enter a valid color")
                    # get transmission validate input
                    elif choice == "7":
                        while 1:
                            transmission = input("Enter a transmission: ")
                            if transmission in ['Automatic', 'Manual', 'CVT', 'Hybrid', 'Electric']:
                                search_critera.update({'transmission': transmission})
                                break
                            else:
                                print("Invalid input. Please enter a valid transmission")
                    # get engine validate input
                    elif choice == "8":
                        while 1:
                            engine = input("Enter a engine: ")
                            if engine.isalpha():
                                search_critera.update({'engine': engine})
                                break
                            else:
                                print("Invalid input. Please enter a valid engine")
                    # get number of owners validate input
                    elif choice == "9":
                        while 1:
                            owners = input("Enter a number of owners: ")
                            if owners.isdigit():
                                search_critera.update({'owners': int(owners)})
                                break
                            else:
                                print("Invalid input. Please enter a valid number of owners")
                    # get vin validate input
                    elif choice == "10":
                        while 1:
                            vin = input("Enter a vin: ")
                            if vin.isalnum() and len(vin) == 17:
                                search_critera.update({'vin': vin})
                                break
                            else:
                                print("Invalid input. Please enter a valid vin")
                    # get title validate input
                    elif choice == "11":
                        while 1:
                            title = input("Enter a title: ")
                            if title in ['Clean', 'Salvage', 'Rebuilt']:
                                search_critera.update({'title': title})
                                break
                            else:
                                print("Invalid input. Please enter a valid title")
                    # get condition validate input
                    elif choice == "12":
                        while 1:
                            condition = input("Enter a condition: ")
                            if condition in ['Excellent', 'Good', 'Fair', 'Poor']:
                                search_critera.update({'condition': condition})
                                break
                            else:
                                print("Invalid input. Please enter a valid condition")
                    # get customer name validate input
                    elif choice == "13":
                        while 1:
                            name = input("Enter a name: ")
                            if name.isalpha():
                                search_critera.update({'name': name})
                                break
                            else:
                                print("Invalid input. Please enter a valid name")
                    # get customer phone validate input
                    elif choice == "14":
                        while 1:
                            phone = input("Enter a phone number: ")
                            if not phone[3] == "-" and phone[7] == "-":
                                print("Invalid phone number")
                            else:
                                search_critera.update({'phone': phone})
                                break
                    # get customer email validate input
                    elif choice == "15":
                        while 1:
                            email = input("Enter an email: ")
                            if not "@" in email and "." in email:
                                print("Invalid email")
                            else:
                                search_critera.update({'email': email})
                                break
                    else:
                        print("Invalid input. Please enter a valid number")
                for purchase in fn.search_purchases(search_critera):
                    fn.print_purchase(purchase)
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
                    # current_user.set_password(new_password)
                    fn.change_password(current_user, new_password)
                    print("Password changed.")
                    break
                except ValueError as e:
                    print(e)
                    break
            # exit
            elif user_settings_selection == 2:
                break
    # admin settings
    elif selection == 5 and isinstance(current_user, cd.Admin):
        while 1:
            print("Admin Settings".center(50, "-"))
            print("1. Add a new user")
            print("2. Remove a user")
            print ("3. Exit")
            # get admin settings selection, validate input
            while 1:
                admin_settings_selection_candidate = str(input("Enter selection: "))
                if not admin_settings_selection_candidate.isdigit():
                    print("Invalid input. Please enter a number between 1 and 3.")
                    continue
                else:
                    admin_settings_selection = int(admin_settings_selection_candidate)
                    break
            # add a new user
            if admin_settings_selection == 1:
                print("Add a New User".center(50, "-"))
                fn.create_user()
            # remove a user
            elif admin_settings_selection == 2:
                print("Remove a User".center(50, "-"))
                user_list = fn.search_users({})
                if user_list == [] or user_list == [current_user]:
                    print("No users found.")
                    continue
                for user in user_list:
                    if not user.get_username() == current_user.get_username() or not user.get_password() == current_user.get_password():
                        print(f"{user.get_username()}")
                while True:
                    user_to_remove_candidate = str(input("Enter username to remove or type 0 to exit: "))
                    if user_to_remove_candidate == "0":
                        break
                    else:
                        for user in user_list:
                            if user.get_username() == user_to_remove_candidate:
                                user_to_remove = user
                                try:
                                    query = {"username": user_to_remove.get_username(), "password": user_to_remove.get_password()}
                                    db = fn.connect_to_mongo()
                                    db['user'].delete_one(query)
                                    print("User removed.")
                                    break
                                except ValueError as e:
                                    print(e)
                                    break
                        else: # move continue here
                            print("Invalid input. Please enter a valid username.")
                            continue
                        break
            # exit
            elif admin_settings_selection == 3:
                break
    else:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue