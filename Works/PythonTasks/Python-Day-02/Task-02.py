test=[
    {
        'id':1,
        'sual':'Bu gun ayin necesidir?',
        'cavablar':[1,2,3,4],
        'duzgunCavab':42
    },
    {
        'id':2,
        'sual':'List hansi dillerde istifade olunur',
        'cavablar':['Python','Js','C','C++'],
        'duzgunCavab':42
    },
     {
        'id':3,
        'sual':'Pythonda nece nov data tipi var?',
        'cavablar':[1,2,3,4],
        'duzgunCavab':42
    },
    {
        'id':4,
        'sual':'En bomba texnologiya hansidir?',
        'cavablar':['HTML',"CSS","JS","Python"],
        'duzgunCavab':42
    }  
]

def ShowMeQuestion(QuestionNumber):
    print(test[QuestionNumber]['sual'])
    ResultNumber=0
    for Result in test[QuestionNumber]['cavablar']:
        print(f'{ResultNumber}: {Result}')
        ResultNumber+=1

def CheckQuestion(QuestionNumber):
    CmResult=int(input('Cavabinizin nomresini qeyd edin: '))
    if CmResult==test[QuestionNumber]['duzgunCavab']:
        print('Sen Mohtesemsen')
    else:
        print('Sansini bir daha yoxla')

def Quiz(QuestionNumber):
    ShowMeQuestion(QuestionNumber)
    CheckQuestion(QuestionNumber)

Quiz(0)  

sual=0

while True:
    emr=input('Novbeti suala cavab vermek isteyirsenmi? (Y/N) :')
    if emr=='Y':
        Quiz(sual)
        sual+=1
    elif sual>len(test):
        break
    else:
        break