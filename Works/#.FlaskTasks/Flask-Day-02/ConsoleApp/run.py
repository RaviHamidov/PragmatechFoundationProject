from oop import Student,students,showStudents

while True:

    emr = input('Yeni telebe yaradilsin mi (Y/N) :')

    if emr == 'Y':

        ad = input('Telebenin adi:')
        soyad = input('Telebenin soyadi:')

        stud = Student(ad,soyad)

        stud.AddToData()

        students.append(stud)
        
    else:
        break
        