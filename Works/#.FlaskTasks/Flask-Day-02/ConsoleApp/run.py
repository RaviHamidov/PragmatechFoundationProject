from oop import qeydiyyat, student, showallusers

while True:

    emr = input(str("Yeni user daxil olunsun: (Y/N) "))
    if emr == "Y":
        username=input(str("Insert the name of user: "))

        usersurname=input("Insert the surname of user: ")

        useremail= input("Insert the email of User: ")

        userphone=input("Insert the number of user: ")

        userpassword=input("Insert the password of user: ")

        userinfo=input("Insert the info about the user: ")

        user=qeydiyyat(username, usersurname, useremail, userphone, userpassword, userinfo)
        student.append(user)
        showallusers()

    else:
        break