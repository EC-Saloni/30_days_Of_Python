# Practice Project - Bank Account System- 
                #    Features: deposit, withdraw, check balance- Use classes, exceptions, and file I/O

class InsufficientBalanceError(Exception):
    def __init__(self, amount,balance):
        message = f"Insufficient Balance ${balance} to withdraw ${amount}"
        super().__init__(message)

class BankAccountSystem:
    def __init__(self,acc_no,acc_holder,balance=0):
        self.acc_no = acc_no
        self.acc_holder = acc_holder
        self.balance = float(balance)

    def read_account(file_name):
        accounts = []
        try:
            with open(file_name,"r") as file:
                for line in file:
                    acc_no,acc_holder,balance = line.strip().split(";")
                    accounts.append(BankAccountSystem(acc_no,acc_holder,float(balance)))
                    return accounts
        except FileNotFoundError:
            print("File not found.")
            return []
        
    def write_acc(file_name,account):
        with open(file_name,"a") as file:
            file.write(f"{account.acc_no};{account.acc_holder};{account.balance}\n")


    def deposite(self,amount):
         self.balance += amount
         return self.balance
    
    def withdraw(self,amount):
        if amount > self.balance:
           raise InsufficientBalanceError(amount,self.balance)
        else:
           self.balance -= amount
        return f"Total balance : {self.balance}"
        
    def checkBalance(self):
        return self.balance
    


file_name = "account.txt"
accounts = BankAccountSystem.read_account(file_name)

while True:
    print("1. Create account.")
    print("2. Read account.")
    print("3. Deposite money")
    print("4. Withdraw money.")
    print("5. Exit.")

    choice = input("Enter your choice:")

    if choice == '1':
        acc_no = int(input("Enter your account number: "))
        acc_holder = input("Enter your account holder's name: ")
        balance = float(input("Enter your balance: "))
        account = BankAccountSystem(acc_no,acc_holder,balance)
        BankAccountSystem.write_acc(file_name,account)
        accounts.append(account)

    elif choice == '2':
        for account in accounts:
            print(f"Account holder's name : {account.acc_holder} \n Account Number : {account.acc_no} \n Total balance : {account.balance}")

    elif choice == '3':
        amount = float(input("Enter the deposite amount: "))
        for a in accounts:
            print(a.deposite(amount))

    elif choice == '4':
        amount = float(input("Enter the withdraw amount: "))
        for a in accounts:
            try:
              print(a.withdraw(amount))
            except InsufficientBalanceError as e:
                print(e)

    elif choice == '5':
        print("Exiting the program.")
        break

    else:
        print("Invalid choise! Please enter the correct choice")
        




