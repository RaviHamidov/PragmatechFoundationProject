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

    #------------------------------------------------------------------------

    def show_all_info (self):

        print(f'{self.name}  {self.surname}  {self.email}  {self.phone}  {self.password}  {self.brief_info}')

    #------------------------------------------------------------------------

    def user_name(self):

        self.name=str(input(" adi daxil edin: "))
        if self.name == "":
            print("error")
        else:
            return
    
    #------------------------------------------------------------------------

    def user_surname(self):

        self.name == str(input(" soyadi daxil edin: "))
        if self.surname == "":
            print("error")
        else:
            return

    #------------------------------------------------------------------------

    def user_email(self):

        self.email == str(input(" mail daxil edin: "))
        if(re.fullmatch(regex, self.email)):
            return
        else:
            print("error")

    #------------------------------------------------------------------------

    def detect_numbers(self):

        print(''' uygun prefixi daxil edin 
                        * bakcell - 55
                        * azercel - 50
                        * nar - 70 ''')
        
        while True:

            self.phone == int(input('nomre daxil edin : '))
            
            if self.phone != "55" or "50" or "70":
                print("Sefh daxil edilib nomre")

            else:
                print(f'{ +994} {self.phone}')

    #------------------------------------------------------------------------

    def user_password(self):

        self.password = str(input(" parolu daxil edin: "))
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

    #------------------------------------------------------------------------

    def user_brief_info(self):

        self.brief_info=input(str(" qisa melumat daxil edin : "))
        if self.brief_info == "":
            print("error")
        else:
            return

    #------------------------------------------------------------------------

class daxil_ol():

    def find_user():
        print()

qaropka = qeydiyyat("elmar","memmedov","hhh@gmail.com","287367984617","ajnkdnekfj","ewfweFRWEF")
qaropka.detect_numbers()