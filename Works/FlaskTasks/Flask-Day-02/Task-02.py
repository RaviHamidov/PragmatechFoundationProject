import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

class register():
    
    #------------------------------------------------------------------------

    def _init_(self, name, surname, email, number, password, brief_info):

        self.name = name
        self.surname = surname
        self.email = email
        self.number = number
        self.password = password
        self.brief_info = brief_info

    #------------------------------------------------------------------------

    def user_name(self):
        self.name=input(str("Enter your name: "))
        if self.name != "" :
            print("Succesful !")
        else:
            print("Error, Please enter your name, Beacuse it's necessary !")
            return self.name

    #------------------------------------------------------------------------

    def user_surname(self):
        self.surname=input(str("Enter your surname: "))
        if self.surname != "":
            print("Succesful !")
        else:
            print("Error, Please enter your surname, Beacuse it's necessary !")
            return self.surname

    #------------------------------------------------------------------------

    def user_email(self):
        self.email=input(str("Enter your email: "))
        if (re.search(regex,self.email)):
            print("Succesful !")
        else:
            print("Error, Please write your e-mail correctly !")
            return self.email
    
    #------------------------------------------------------------------------

    def user_number(self):
        self.number=input(str("Enter your number : +994 "))
        val = True

        if len(self.number) != 9:
            print("Error, The number must be 9 digits")
            val
            
        if not all(char.isdigit() for char in self.number):
            print("Error, Please just the number")
            val

        if self.number.startswith("50",0,2):
            print("The operation was completed successfully !")
            val

        elif self.number.startswith("51",0,2):
            print("The operation was completed successfully !")
            val

        elif self.number.startswith("55",0,2):
            print("The operation was completed successfully !")
            val

        elif self.number.startswith("99",0,2):
            print("The operation was completed successfully !")
            val

        elif self.number.startswith("70",0,2):
            print("The operation was completed successfully !")
            val

        elif self.number.startswith("77",0,2):
            print("The operation was completed successfully !")
            val

        else:
            print("Error, You may be using an external network. Please use an internal network !")
            val=False
           
    #------------------------------------------------------------------------    

    def user_password(self):
        self.password=input(str("Enter your password: "))
        val = True
        
        if len(self.password) <= 8:
            print("Must consist of at least 8 characters !")
            val = False
            
        if len(self.password) >= 20:
            print("Must consist of a maximum of 20 characters !")
            val = False
            
        if not any(char.isdigit() for char in self.password):
            print("There must be an absolute number inside !")
            val = False
            
        if not any(char.isupper() for char in self.password):
            print("Must be at least one uppercase letter !")
            val = False

        if len(self.password.islower()) >= 2:
            print("Must be at least two lowercase letter !")
            val = False

        if val:
            return val

    #------------------------------------------------------------------------ 

    def brief_info(self):
        self.info=input(str("Write a brief description of yourself: "))

    #------------------------------------------------------------------------ 

def ready():
    while True:
        show = register()
        show.user_name()
        show.user_surname()
        show.user_email()
        show.user_password()
        show.user_number()
        show.brief_info()