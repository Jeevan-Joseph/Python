print("select a number:")
print("\n 1.login \n 2.register \n 3.dashboard \n 4.exit")

while True:
    a=int(input("Enter a number:"))
    if(a==1):
        username=input("Enter the username:")
        password=input("Enter password:")
        print(username,password)
    elif(a==2):
        Name=input("Enter name:")
        email=input("Enter email:")
        print(Name,email)
    elif(a==3):
        print("Welcome to Dashboard")
    elif(a==4):
        exit()
    else:
        pass
    
