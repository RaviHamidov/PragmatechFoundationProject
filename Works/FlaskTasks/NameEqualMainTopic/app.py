import data_base

def add_user(user_name):
    data_base.connect("pul")
    print("Pul tapildi.")
    data_base.disconnect("pul")

add_user("admin")