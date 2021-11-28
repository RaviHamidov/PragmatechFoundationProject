student=[]

import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class registration():
    def _init_(self, name, surname, email, phone, password, brief_info):
        self.name=name
        self.surname=surname
        self.email=email
        self.phone=phone
        self.password=password
        self.brief_info=brief_info

    def show (self):
        print(f'{self.name}  {self.surname}  {self.email}  {self.phone}  {self.password}  {self.brief_info}')

    def user_name(self):
        self.name=input(str("Adi daxil edin: "))
        if self.name == "" :
            print(self.name)
        else:
            print('Bu xana bosh olmaz')
    
    def user_surname(self):
        self.name=input(str("Familiyani daxil edin: "))
        if self.surname == "":
            print("error")
        else:
            print("basin burax") 


    def user_email(self):
        self.email=input(str("Insert the email: "))
        if(re.fullmatch(regex, self.email)):
            print("Valid Email")
        else:
            print("Invalid Email")

    def detect_numbers(self):
        numerrr=input(str("type a number: +994 "))