users = []

def show_profile():

    for user in users:
        print(f'''{user["name"]} 
                  {user["surname"]}
                  {user["email"]}
                  {user["phone"]}
                  {user["password"]}
                  {user["brief_information"]}''')

def enter_profile():

    email=input('type email: ')
    password=input('type password: ')

def register():

    name=input('user name : ')
    surname=input('user surname: ')
    email=input('user email: ')
    phone=input('user phone: ')
    password=input('user password: ')
    brief_information=input('brief_information: ')

    user={
        'name':name,
        'surname':surname,
        'email':email,
        'phone':phone,
        'password':password,
        'brief_information':brief_information
    }
    users.append(user)

print("""   
    - Main menu
        - type 1 to register .
        - type 2 to enter the profile .
        - type 3 to left the program .
   """)
#     - Əsas menu
#         - Qeydiyyatdan keç
#             - Ad (doldurulması zəruridir)
#             - Soyad (doldurulması zəruridir)
#             - Email (doldurulması zəruridir)
#                 - Email olub olmaması yoxlanılmalıdır. Əks halda error mesajı çıxmalıdır ekrana
#             - Telefon (doldurulması zəruri deyil)
#                 - Sadəcə rəqəmlər daxil edilə bilməlidir. Əks halda error mesajı verilməlidir.
#                 - +994 ifadəsi aftamatik olaraq yazılmalıdır telefon nömrəsinin önünə. 
#                 - Telefon nömrəsi sadəcə Azərbaycan GSM şirkətlərinin prefixləri ilə daxil edilməlidir (55,50 və s)
#                 - Daxil edilən rəqəm sayı 7-dən yuxarı ola bilməz
#             - Password
#                 - Minimum 8 xarakterdən ibarət olmalıdır
#                 - Daxilində mütləq minium 2 kiçik və 1 böyük hərf olmalıdır
#                 - Minimum 1 ədəd rəqəm olmalıdır
#             - Qisa məlumat
#         - Daxil ol
#             - istifadəçi email və passwordunu daxil edir
#                 - üç dəfə səhv məlumat daxil edildiyi zaman qeydiyyat bölməsinə yönləndirmə edilməlidir
#             - Bu məlumatlara uyğun istifadəçi varsa 
#                 - istifadəçi haqqında olan bütün məlumatlar ekranda görünməlidir
#                 - ESC düyməsinə basanda profildən çıxın əsas menuye qayıtmalıdır
#         - ESC düyməsinə basılanda proqramdan çıxmalıdır