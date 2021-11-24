users=[]

id=1

def createUser():

    ad=input('Istifadi adı: ')
    soyad=input('Istifadi soyadı: ')
    email=input('Istifadi emaili: ')
    
    global id

    user={
        'id':id,
        'ad':ad,
        'soyad':soyad,
        'email':email
    }
    users.append(user)

    id+=1


def showAllUsers():
    for user in users:
        print(f'{user["id"]}.{user["ad"]} - {user["soyad"]} ')


def deleteUser():
    silinecekOlanElementinIdsi=int(input('Silmek istediyiniz elementin id nomresini daxil edin : '))
    for user in users:
        if silinecekOlanElementinIdsi==user['id']:
            users.remove(user)


def updateUser():
    id=int(input('Melumati deyisecek olan istifadecinin id-i daxil edin: '))
    for user in users:
        if id==user['id']:
            yeniAd=input('Yeni adi daxil edin :')
            user['ad']=yeniAd
            
              
print("""    
   - Yeni istifadeci yaratmaq ucun 1 yazin
   - Istifadecileri gormek ucun 2 yazin 
   - Istifadecini silmek ucun 3 yazin
   - Istifadeci melumatini deyismek ucun 4 yazin
   - Proqramdan cixmaq ucun 5 yazin    
   """)



while True:
    emr = int(input('Istediyiniz emeliyyatin nomresini qeyd edin : '))
    if emr == 1:
        createUser()
    elif emr == 2:
        showAllUsers()
    elif emr == 3:
        deleteUser()
    elif emr == 4:
        updateUser()
    else:
        break