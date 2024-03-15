# Facilitating transfers between account 
from account import Account

class Transaction:
    def transfer(from_account, to_account, amount):
        if amount <= from_account.get_balance():
            from_account.withdrawal(amount)
            to_account.deposite(amount)
            print("Successful Transaction")
        else:
            print("Unsuccessful Transaction, Insufficient Funds")
            