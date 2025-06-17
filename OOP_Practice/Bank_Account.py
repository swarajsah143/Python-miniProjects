class BankAccount:

    def __init__(self,Initial_Amnout,AccName):
        self.Balance=Initial_Amnout
        self.AccName=AccName
        print(f"Account Name '{self.AccName}' has been created with the initial amount {self.Balance:.2f}\n")

    def get_balance(self):
        print(f"Account : {self.AccName}\nCurrent_Balance = {self.Balance}")

    def deposit(self, Amount):
        self.Balance+=Amount
        print("Amount Deposited.")
        self.get_balance()

    def viableTransaction(self,Amount):
        if self.Balance>=Amount:
            return 
        else:
            raise BaseException(f"Sorry, account '{self.AccName}' has only {self.Balance} amount.")

    def withdraw(self,Amount):
        try:
            self.viableTransaction(Amount)
            self.Balance-=Amount
            print('\nWithdraw Complete.')
            self.get_balance()
        except BaseException as error:
            print(f"Withdraw interrupted: {error}")

    def transfer(self,Amount,AccName):
        try:
            print('\n **********\n\n Beginning Transfer.....🚀')
            self.viableTransaction(Amount)
            self.withdraw(Amount)
            AccName.deposit(Amount)     # Nabil.deposite(300) ---> Go to deposite() taking all the data of Nabil
            print("\nTransfer Complete ✅\n\n**********")
        except BaseException as error:
            print(f"Transaction Failed❌.{error}")


