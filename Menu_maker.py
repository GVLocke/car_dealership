import class_definitions as cd



def password_unlock():
   password = input("Enter password: ")
   if password == "opensaysame": 
       return True
   else:
       print("Wrong password.")
       return False

     
if password_unlock():
  
  while (1):
    
    print("option 1: Display User")
    print("option 2: ")

    option = input()






    if option == 1:
      N = input("Enter name: ")

      UserAndy = cd.User("Andy", "555-555-5555", "koernera@jbu.edu")
      if N == 'Andy' or N== 'andy':
        UserAndy.display_user()

      UserJames = cd.User("James", "666-666-6666", "keysj@jbu.edu")
      if N== 'James' or N == 'james':
        cd.User.display_user()

      else:
        print("Not a user")




    
    
  