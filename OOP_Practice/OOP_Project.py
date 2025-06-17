from Bank_Account import *

Nabil= BankAccount(23000,'Nabil')
SBI= BankAccount(3000,'SBI')

# SBI.deposit(500)
# SBI.withdraw(300)

SBI.transfer(100,Nabil)