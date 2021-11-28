student=[]

import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class qeydiyyat():

    def _init_(self, name, surname, email, phone, password, brief_info):
        
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.password = password
        self.brief_info = brief_info

    def show (self):
        print(f'{self.name}  {self.surname}  {self.email}  {self.phone}  {self.password}  {self.brief_info}')

    def user_name(self):
        self.name=input(str(" adi daxil edin: "))
        if self.name == "":
            print("error")
        else:
            return
    
    def user_surname(self):
        self.name == input(str(" soyad daxil edin : "))
        if self.surname == "":
            print("error")
        else:
            return

    def user_email(self):
        self.email == input(str(" mail daxil edin : "))
        if(re.fullmatch(regex, self.email)):
            return
        else:
            print("error")

    def detect_numbers(self):
        self.phone == input(int('nomre daxil edin : +994 '))

    def user_password(self):
        self.password=input(str('parolu daxil et : '))
        val = True
        
        if len(self.password) <= 8:
            print('Minimum 8 xarakterden ibaret olmalidir qaqash')
            val = False
            
        if len(self.password) >= 20:
            print('Maksimum 20 xarakterden ibaret olmalidir')
            val = False
            
        if not any(char.isdigit() for char in self.password):
            print('Password should have at least one numeral')
            val = False
            
        if not any(char.isupper() for char in self.password):
            print('Password should have at least one uppercase letter')
            val = False
            
        if not any(char.islower() for char in self.password):
                print('Password should have at least one of the symbols $@#')
                val = False
        if val:
            return val

    def user_brief_info(self):
        self.brief_info=input(str(" qisa melumat daxil edin : "))
        if self.brief_info == "":
            print("error")
        else:
            return

class daxil_ol():

    print("nese")
