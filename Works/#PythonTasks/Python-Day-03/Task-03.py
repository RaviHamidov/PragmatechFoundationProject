Name=[
    'Git',
    'Github',
    'Html',
    'Css',
    'Js',
    'Python',
    'Flask',
    'Sql',
    'Django'
]

def ShowMeNames():
    for i in range(len(Name)):
        print(i,Name[i])
def WhichIsPlusOne():
    for i in range(len(Name)):
        if i%2==0:
            print(i,Name[i])

def SortList():
    Name.sort()
    ShowMeNames()

def FindWhereIsE():
    for Info in Name:
        if Info.find('e')!=-1:
            print(f'{Info} sozde e var ! ')
        else:
            print(f'{Info} sozde e yoxdur ! ')
FindWhereIsE()