# Bank account and managing the balance

class Account:
    # property: account_number, balance
    # methods: get_balance, withdrawal, deposite

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.amount = balance
        pass
    def get_balance(self):
        return self.balance
    
    def deposite(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balancce -= amount
        else:
            print('Insufficient Balance')


    