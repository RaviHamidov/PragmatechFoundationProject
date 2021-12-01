def connect(db_name):
    print("{} ucun baglanti quruldu.".format(db_name))

def disconnect(db_name):
    print("{} ucun baglanti qapatildi.".format(db_name)) 

# if __name__ == "__main__":

connect("portfolio")
disconnect("portfolio")
# print("basqa careler")