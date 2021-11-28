from oop import Student,students,showStudents

while True:

    print("""   
    - esas menu
        - qeydiyyat ucun 1 e basin .
        - profile daxil olmaq ucun 2 e basin .
        - programdan cxmaq ucun esc e basn .
   """)

    emr = int(input('istediyin emelyatin nomresini qeyd ele ! :'))

    if emr == '1':

        ad = input('Telebenin adi : ')
        soyad = input('Telebenin soyadi : ')
        email = input('Telebenin emaili : ')
        password = input('Telebenin passwordu : ')
        phone = input('Telebenin phoneu : ')

        stud = Student(ad,soyad,email,password,phone)

        stud.AddToData()

        students.append(stud)
        
    else:
        break
        