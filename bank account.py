
class bankacount:
    balence = 1000
    def __init__ (self,name,balence):
        self.name = name
        self.balence = balence

    def deposite(self,amount):
        self.balence = self.balence + amount
        print(f"deposited {amount} .now your balence {self.balence}")

    def withdraw(self,amount):
        if amount > self.balence:
            print("insufiisitan funds")
        
        else:
            self.balence = self.balence - amount
            print(f"secesfull your withdraw now your balence is {self.balence}")

    def show_balence(self):
        print(f" {self.name} your current balance {self.balence}")

acc = bankacount("sumit",1000)

while True:
    print("\n====== BANK MENU ======")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter deposit amount: "))
        acc.deposite(amount)
        
    elif choice == 2:
        amount= int(input("your withdraw ammount : "))
        acc.withdraw(amount)
     
    elif choice == 3:
        acc.show_balence()

    elif choice == 4:
        print(" EXIT ")
        break
    else:
        print("Invalid Choice! Please try again.")
