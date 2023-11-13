class Bank:
    def __init__(self, acc, name, type):
        self.acc = acc
        self.name = name
        self.type = type
        self.bal = 0

    def deposit(self, depos):
        self.bal = self.bal + depos

    def withdraw(self, withd):
        if self.bal < withd:
            print("Insufficient Balance")
        else:
            self.bal = self.bal - withd
        print("Current balance is", self.bal)

    def display(self):
        print("Account Number: ", self.acc)
        print("Account Holder: ", self.name)
        print("Account Type: ", self.type)
        print("Account Balance:", self.bal)


acc = int(input("Enter the account number: "))
name = input("Enter the name of the account holder: ")
type = input("Enter the type of the account: ")
depos = int(input("Enter the amount to deposit: "))

obj = Bank(acc, name, type)
obj.deposit(depos)
obj.display()
withd = int(input("Enter the amount to withdraw: "))
obj.withdraw(withd)
