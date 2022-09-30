


class Bank:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts


class Customer:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName


class Account:
    def __init__(self, balance, customer):
        self.balance = balance
        self.customer = customer


# Create customer
customer1 = Customer("Rasmus", "Kibshede")

# Create accounts
account1 = Account(100, customer1)
account2 = Account(400, customer1)
account3 = Account(800, customer1)


# Create a bank
bank = Bank("Bank", [account1, account2])


bank.accounts.append(account3)


print(bank.accounts[2].balance)












