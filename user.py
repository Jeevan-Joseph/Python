class User:
    def __init__(self,name,password,email):
        self.username = name
        self.password = password
        self.email = email
        self.bal = 0

    def welcome(self):
        print(f"Welcome {self.username}")
        print(f"Your password is: {self.password}")
        print(f"Email id: {self.email}")

    def balance(self):
        print(f"balance: {self.bal}")

def create_user():
    name = input("Enter name: ")
    email = input("Enter email id: ")
    password = input("Enter password: ")

    return User(name,password,email)
   
user1 = create_user()
user1.balance()
user2 = create_user()
user2.bal=100
user2.balance()

#list1 = ["flight","flower","flag"] --> fl
#list2 = ["dog","dam","dad"] --> d
#list3 = ["cricket","football","hockey"]--> ""
#

