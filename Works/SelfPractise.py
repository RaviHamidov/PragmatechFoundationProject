## I started learn python for zero to hero 

# StepOne " Python tutorial for beginners "

print("I love pizza")
print("It's really good!")

# StepTwo " How Variables work in python "

firstName = "I love"
lastName = "pizza"
fullName = firstName + " " + lastName
 
print(fullName)
name = "Coder"
print("Hello " + name)
print(type(name))

age = 17 #before
age += 1 #after

print(age)
print(type(age))

age = 17
print(age)
print(type(age)) 

print("Your age is :" + age) #Before that is right

age += 1

print("Your age is :" + age) #After that is false 

# Because age is int data tye but first text is str data type you can't do it , you need to convert age variable to string data type  

print("Your age is :" + str(age) )

height = 42.0
print("Your love pizza cm is : " + str(height)+"cm")
print(type(height))

human = False 
print(human)
print(type(human))

human = "False" 
print(human)
print(type(human))

human = "True"
print("Realy that is a pizza? :" + str(human)) 

# StepThree " Multiple assignment in Python "

name = "Pizza"
length = "36"+ " " + "cm"
kind = "Mozarella"

name, length, kind = "Pizza", "36"+ " " + "cm", "Mozarella"

print(name)
print(length)
print(kind)

pizzaMozarella = "35"+" "+"Azn"
pizzaItaliano = "35"+" "+"Azn"
pizzaMix = "35"+" "+"Azn"
pizzaVegi = "35"+" "+"Azn"

pizzaMozarella = pizzaItaliano = pizzaMix = pizzaVegi = "35"+" "+"Azn"

print(pizzaMozarella)
print(pizzaItaliano)
print(pizzaMix)
print(pizzaVegi)

# StepFour " String Methods in Python "

pizza = "italiano"

print(len(pizza))
print(pizza.find("o"))
print(pizza.capitalize())
print(pizza.upper())
print(pizza.lower())
print(pizza.isdigit())
print(pizza.isalpha())
print(pizza.count("a"))
print(pizza.replace("i","a"))
print(pizza.replace("a","i"))
print(pizza*3)

# StepFive " Type casting in Python"

pizzaTotal = 5 #int
pizzaLength = 15.0 #float
pizzaType = "Thin" #str

print(pizzaTotal)
print(pizzaLength)
print(pizzaType)

pizzaLength = int(pizzaLength)
print(pizzaLength)

print(int(pizzaLength))

# StepSix " User Input "

name = input("What is your name? :")
age = int(input("How old are you? :"))
height = float(input("How tall are you? :"))

print("Hello " + name)
print("You are " + str(age) + " years old")
print("You are " + str(height) + "cm tall")

# StepSeven " Math Functions "

import math

pi = 3.14
x = 5
y = 3
z = 2

# print(round(pi))
# print(math.ceil(pi)
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(pi))
# print(max(x,y,z))
print(min(x,y,z))

# StepEight " String slicing "

name = "Mozarella Pizza"

first_name = name[2]

print(first_name) # result z

first_name = name[0:9]
last_name = name[10:]
funny_name = name[0:15:2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funny_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])

# StepNine " if statement "

age = int(input("Balacanin nece yasi var ? : "))

if age == 100 :
    print("Sen deme bir ayagi cuxurda imis sjsjsjsjsj :(")
elif age >= 18 :
    print("Yaxci yaslaridi de heyatin dadini cxarsin ;)")
elif age <= 10 :
    print("Onda denen emi ona padarka alacaq ;)")
else :
    print("Yeke kisi olsun")

# StepTen " Logical Operators (and,or,not)"

temp = int(input("Qeqes colde hava necedir? :"))

if temp >= 20 and temp <= 40 :
    print("ala bomba kimi hava var cix cole top oynyaq sjsjsjsj.")
    print("ala gelde derem sene narahat olma e stadionun pulunu verejem men ;)")
elif temp < 20 or temp > 0 :
    print("Nem e brat belede yeni cox yaxci deyl vezyet ruscadi")
    print("Qal evde koduvu yaz sjjsjssjsjsjs !")

temp = int(input("Qeqes colde hava necedir? :"))

if not temp >= 20 and temp <= 40 :
    print("ala bomba kimi hava var cix cole top oynyaq sjsjsjsj.")
    print("ala gelde derem sene narahat olma e stadionun pulunu verejem men ;)")
elif not temp < 20 or temp > 0 :
    print("Nem e brat belede yeni cox yaxci deyl vezyet ruscadi")
    print("Qal evde koduvu yaz sjjsjssjsjsjs !")

# StepEleven " While loop in Python"

while 1 == 1:
    name = print("I really love pizza !")

name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)

name = None

while not name:
    name = input("Enter your name: ")

print("Hello " + name)

# StepTwelve " For loop in Python"

import time 

for i in range(10):
    print(i+1)

for i in range(50,100+1,2):
    print(i)

for i in "Pizza Italiano":
    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Heri men!")

# StepThreeteen " Nested loop in Python"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end = "")
    print()

# StepFourteen " Loop Control in Python"

while True :
    name = input("Tez advi yaz ba frldaq eleme ha yosa cekpot vermerem ! :")
    if name != "":
        print("Buyur buda cekpotun : Tebrikler spcka chopu qazandin !")
        break

phone_number = "+994-55-496-27-87"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1,21):

    if i == 13:
        pass
    else:
        print(i)

for num in range (1,6):
    if num % 2 == 0 :
        continue
    print(num)

# StepFiveteen " list in Python"

food = ["pizza","hamburger","hotdog","spaghetti","pudding"]

food[0] = "sushi"

food.append("ice cream")
food.remove("hotdog")
food.pop()
food.insert(0,"cake")
food.sort()
food.clear()

for x in food:
    print(x)