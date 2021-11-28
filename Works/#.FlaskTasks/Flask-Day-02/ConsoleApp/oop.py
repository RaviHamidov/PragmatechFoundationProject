students=[]

class Student:

    def __init__(self,_ad,_soyad):
        self.ad=_ad
        self.soyad=_soyad
        students.append(self)
        
    def Goster(self):
        print(f'{self.ad}-{self.soyad} \n')
    
    def AddToData(self):
        file=open('data.txt','a')
        file.write(f'{self.ad}|{self.soyad}\n')

def showStudents():

    for s in students:
        s.AddToData()

showStudents()
