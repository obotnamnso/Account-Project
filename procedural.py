# defining a function
def create_account(account_number, balance):
    return {"account_number": account_number, "balance": balance}

# Retrive the acc balance
def get_balance(account):
    return account['balance']

# deposite money, account balance increases
def deposite(account, amount):
     account['balance'] += amount

# Withdraw, check if funds are sufficient
def withdraw(account, amount):
    if amount <= account['balance']:
        account['balance'] -= amount
    else:
        print('Insufficient funds.')

# Use name to know which account is which
def tranfer(from_account, to_account, amount):
    if amount <= from_account['balance']:
        withdraw(from_account, amount)
        deposite(to_account, amount)
        print('Transfer successful !')
    else:
        print('Insufficient funds')

# Using the functions define above
account1 = create_account('12345', 1000)
account2 = create_account('12346', 500)

tranfer(account1, account2, 300)

print(f'Account 1 balance: {get_balance(account1)}')
print(f'Account 2 balance: {get_balance(account2)}')