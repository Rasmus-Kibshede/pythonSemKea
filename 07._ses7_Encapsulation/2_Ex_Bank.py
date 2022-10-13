class Bank:
    def __init__(self, name):
        self.name = name
    
    @property
    def accounts(self):
        return self.__accounts
    
    @accounts.setter
    def accounts(self, accounts):
        self.__accounts = accounts



class Customer:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age


class Account:
    def __init__(self, balance, customer):
        self.balance = balance
        self.customer = customer


# Create customer
customer1 = Customer("Rasmus", "Kibshede", 29)

# Create accounts
account1 = Account(100, customer1)
account2 = Account(400, customer1)
account3 = Account(800, customer1)


# Create a bank
bank = Bank("Bank")

bank.accounts = [account1, account2]


bank.accounts.append(account3)


print(bank.accounts[2].customer.firstName)





