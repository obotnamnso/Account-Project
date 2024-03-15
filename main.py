from account import Account
from transaction import Transaction

# instances of the Account class
account1 = Account('1234501', 1000)
account2 = Account('1234502', 2000)
account3 = Account('1234503', 3000)

# Making transfer 
Transaction.transfer(account1, account2, 500)
Transaction.transfer(account3, account2, 500)

account1_balance = account1.get_balance()
account2_balance = account2.get_balance()
account3_balance = account3.get_balance()

print(f'Account 1 balance {account1_balance}')
print(f'Account 2 balance {account2_balance}')
print(f'Account 3 balance {account3_balance}')