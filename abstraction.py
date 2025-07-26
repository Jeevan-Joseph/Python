class Parent:
    def __init__(self,name):
        self.name = name
        self._age = 20
        self.__balance = 0

    def getName(self):
        print(f"Welcome {self.name}")

    def getBalance(self):
        print(f"balance {self.__balance}")

parent = Parent("Anish")

parent.getName()
print(parent._age)
parent.getBalance()

        